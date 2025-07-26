from langchain.translate_chat import create_translation_chain

def main():
    # 创建翻译链
    chain = create_translation_chain()
    
    # 简单的交互式翻译
    print("翻译助手 (输入'q'退出)")
    while True:
        text = input("\n请输入要翻译的文本: ")
        if text.lower() == 'q':
            break
        
        result = chain.invoke({
            "input_language": "zh-CN",
            "output_language": "en-US",
            "text": text
        })
        
        print(f"\n翻译结果: {result.content}")

if __name__ == "__main__":
    main() 