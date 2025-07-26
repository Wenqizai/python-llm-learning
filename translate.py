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
        
        # 等待结果返回
        # result = chain.invoke({
        #     "input_language": "zh-CN",
        #     "output_language": "en-US",
        #     "text": text
        # })
        
        # 流式输出结果
        stream = chain.stream({
            "input_language": "zh-CN",
            "output_language": "en-US",
            "text": text
        })
        
        for chunk in stream:
            print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    main() 