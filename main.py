from simple_pastebin_parser.simple_pastebin_parser import get_posts


if __name__ == '__main__':
    for post in get_posts(True, 30):
        # print("href: ", href)
        print("Title: ", post.title)
        print("Author: ", post.author)
        print("date: ", post.date)
        print(post.code)
        print("*" * 20)
        print("*" * 20)
