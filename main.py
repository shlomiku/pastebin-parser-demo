import json
import redis

from os.path import exists, join
from os import getcwd, mkdir

import simple_pastebin_parser

OUTPUT_FOLDER = join(getcwd(), "OUTPUT")
r = redis.StrictRedis(host='192.168.99.100', port=6377, db=2)


def create_output_folder_if_doesnt_exist():
    if not exists(OUTPUT_FOLDER):
        mkdir(OUTPUT_FOLDER)


def does_paste_file_already_exist(paste):
    filename = "{}.json".format(paste.id)
    file_path = join(OUTPUT_FOLDER, filename)
    return exists(file_path)


def store_paste_date_to_disk(paste):
    data = paste.get()
    data["Date"] = str(data["Date"])
    filename = "{}.json".format(paste.id)
    file_path = join(OUTPUT_FOLDER, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def store_paste_to_redis(paste):
    data = paste.get()
    data["Date"] = str(data["Date"])
    r.hmset(paste.id, data)


if __name__ == '__main__':
    create_output_folder_if_doesnt_exist()
    for paste in simple_pastebin_parser.get_pastes(should_stream=True, sampling_frequency=60*2):
        if not does_paste_file_already_exist(paste):
            store_paste_date_to_disk(paste)
            store_paste_to_redis(paste)
