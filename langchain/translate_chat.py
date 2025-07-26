from langchain_core.prompts import ChatPromptTemplate
from langchain.api_manager import ApiKeyManager


def create_translation_chain():
    """创建并返回一个翻译链"""
    # 使用ApiKeyManager获取OpenAI实例
    api_manager = ApiKeyManager()
    llm = api_manager.get_openai()

    prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are a helpful assistant that translates {input_language} to {output_language}. "
            "Remember, you only need to translate the text, and you should not answer or do anything else besides translating the text. This is very important."
            "The user input text needs to be fully translated."
         ),
        ("user", 
            "{text}"
        )
    ])

    return prompt | llm

