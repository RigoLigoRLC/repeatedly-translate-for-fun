#!/usr/bin/python3

import sys
import random

import googletrans

all_lang = list(googletrans.LANGUAGES)
safe_lang = ['zh-cn', 'zh-tw', 'en', 'eo', 'fi', 'fr', 'de', 'iw', 'hi', 'ga', 'it', 'ja',
             'mn', 'pl', 'pt', 'ru', 'es', 'th', 'uz', 'vi', 'cy']
lang = None


def check_version():
    if int((googletrans.__version__)[0]) < 4:
        print("This program needs googletrans version at least 4.0.0-rc1.")
        exit(1)


def parse_args():
    ret = {"count": 10,
           "dest": "zh-CN",
           "intl": False,
           "lbl": False,
           "safe": True}
    for i in sys.argv:
        if i.startswith("-f"):
            ret["file"] = i[2:]
        elif i.startswith("-n"):
            ret["count"] = int(i[2:])
        elif i.startswith("-d"):
            ret["dest"] = i[2:]
        elif i == "-intl":
            ret["intl"] = True
        elif i == "-lines":
            ret["lbl"] = True
        elif i == "-unsafe":
            ret["safe"] = False
    return ret


def translate(translator: googletrans.Translator, text: str, count: int, dest: str):
    temp_text = text
    for i in range(count):
        to_what = random.choice(lang)
        temp_text = translator.translate(temp_text, dest=to_what).text
    return translator.translate(temp_text, dest).text


def do_translate(tr: googletrans.Translator, content: str, line_by_line: bool, count: int, dest: str):
    if line_by_line:
        for i in content.split('\n'):
            print(translate(translator=tr, text=content, count=count, dest=dest))
    else:
        print(translate(translator=tr, text=content, count=count, dest=dest))


def main():
    random.seed()
    check_version()

    args = parse_args()
    url = ["translate.google.cn"]
    count = args["count"]
    dest = args["dest"]
    line_by_line = args["lbl"]
    global lang
    if args["safe"]:
        lang = safe_lang
    else:
        lang = all_lang
    content = ""
    use_input = False

    if args["intl"]:
        url = ["translate.google.com"]
    tr = googletrans.Translator(service_urls=url)

    if "file" in args:
        f = open(args["file"], "r", encoding="utf-8")
        content = f.read()
    else:
        use_input = True

    if use_input:
        while True:
            content = input()
            if len(content) == 0:
                return
            do_translate(tr, content, line_by_line, count, dest)
    else:
        do_translate(tr, content, line_by_line, count, dest)


if __name__ == '__main__':
    main()
