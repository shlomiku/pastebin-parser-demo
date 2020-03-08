import simple_pastebin_parser


if __name__ == '__main__':
    for paste in simple_pastebin_parser.get_posts(True, 30):
        # print("href: ", href)
        print("Title: ", paste.Title)
        print("Author: ", paste.Author)
        print("date: ", paste.Date)
        print(paste.Content)
        print("*" * 20)
        print("*" * 20)
