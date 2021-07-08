#!/usr/bin/python3

import sys
import random

import googletrans

lang = list(googletrans.LANGUAGES)


def check_version():
    if int((googletrans.__version__)[0]) < 4:
        print("This program needs googletrans version at least 4.0.0-rc1.")
        exit(1)


def parse_args():
    ret = {"count": 10,
           "dest": "zh-CN",
           "intl": False,
           "lbl": False}
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
    return ret


def translate(translator: googletrans.Translator, text: str, count: int, dest: str):
    temp_text = text
    for i in range(count):
        to_what = random.choice(lang)
        temp_text = translator.translate(temp_text, dest=to_what).text
    return translator.translate(temp_text, dest).text


def do_translate(tr: googletrans.Translator, content: str, line_by_line: bool, count: int, dest: str):
    if line_by_line:
        for i in content:
            print(translate(translator=tr, text=content, count=count, dest=dest))
    else:
        print(translate(translator=tr, text=content, count=count, dest=dest))


def main():
    check_version()

    args = parse_args()
    url = ["translate.google.cn"]
    count = args["count"]
    dest = args["dest"]
    line_by_line = args["lbl"]
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
