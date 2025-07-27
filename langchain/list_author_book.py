from chain.list_author_book_chain import  create_list_author_book_chain

def main():
    chain = create_list_author_book_chain()
    
    print("你的图书助手，请输入作者名称，输入 q 退出")
    while True:
        author = input("请输入作者名称: ")
        if author.lower() == "q":
            break
        
        # json 不适合流式输出，所以使用等待结果返回
        result = chain.invoke({"author": author})
        print("\n📚 作品列表:")
        for i, work in enumerate(result, 1):
            print(f"{i}. 《{work['title']}》")
            print(f"   📖 {work['description']}")
            print()


if __name__ == "__main__":
    main()