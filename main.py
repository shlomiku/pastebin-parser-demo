import hashlib
import json
from os.path import exists, join
from os import getcwd,mkdir

import simple_pastebin_parser

OUTPUT_FOLDER = join(getcwd(), "OUTPUT")


def create_output_folder_if_doesnt_exist():
    if not exists(OUTPUT_FOLDER):
        mkdir(OUTPUT_FOLDER)


def get_paste_hash(paste):
    data = paste.get()
    data["Date"] = str(data["Date"])
    return hashlib.md5("+".join(data.values()).encode('utf-8')).hexdigest()


def does_paste_file_already_exist(paste):
    filename = "{}.json".format(get_paste_hash(paste))
    file_path = join(OUTPUT_FOLDER, filename)
    return exists(file_path)


def store_paste_date_to_disk(paste):
    data = paste.get()
    data["Date"] = str(data["Date"])
    filename = "{}.json".format(get_paste_hash(paste))
    file_path = join(OUTPUT_FOLDER, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    create_output_folder_if_doesnt_exist()
    for paste in simple_pastebin_parser.get_posts(True, 60*2):
        if not does_paste_file_already_exist(paste):
            store_paste_date_to_disk(paste)
