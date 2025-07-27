from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from .api_manager import ApiKeyManager


class Work(BaseModel):
    title: str = Field(description="Title of the work.(if title is en, please translate it to zh-cn, also retain the original language)")
    description: str = Field(description="Description of the work. \n (if description is en, please translate it to zh-cn, also retain the original language)")

def create_list_author_book_chain():
    api_manager = ApiKeyManager()
    llm = api_manager.get_openai(model="gpt-4o-mini", temperature=0)

    parser = JsonOutputParser(pydantic_object=Work)
    prompt = PromptTemplate(
        template="列举2部{author}的写的书或者他人对{author}的写的书。\n{format_instructions}",
        input_variables=["author"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    return prompt | llm | parser