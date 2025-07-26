from langchain_core.prompts import ChatPromptTemplate
from langchain.api_manager import ApiKeyManager


def create_translation_chain():
    """创建并返回一个翻译链"""
    # 使用ApiKeyManager获取OpenAI实例
    api_manager = ApiKeyManager()
    llm = api_manager.get_openai()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("user", "{text}")
    ])

    return prompt | llm

