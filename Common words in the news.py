# pip3 install chardet

import chardet
import collections
import os


def forming_list_files():
    path = os.path.join(os.getcwd())
    list_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if '.txt' in f:
                list_files.append(f)
    return list_files


def detects_encoding(file):
    with open(file, 'rb') as text:
        encoding = chardet.detect(text.read())
        return encoding['encoding']


def forming_text_list(encod):
    with open(file, encoding=encod) as f:
        text_list = []
        for line in f:
            for word in line.strip().split():
                text_list.append(word)
    return text_list


def print_common_word(text_list):
    new_text_list = []
    for word in text_list:
        if len(word) > 6:
            new_text_list.append(word)
    for common_words in collections.Counter(new_text_list).most_common(10):
        print(common_words[0])
    # print('\n **********Следующий файл*********** \n')


for file in forming_list_files():
    print('\n В файле {} чаще всего встречаются следующие слова:'.format(file))
    encod = detects_encoding(file)
    text_list = forming_text_list(encod)
    print_common_word(text_list)


