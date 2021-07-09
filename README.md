# repeatedly-translate-for-fun (谷歌生草机)

# 依赖（Dependencies）

`python3 (>= 3.7)`

`googletrans (>= 4.0.0-rc1)`

# 使用方法

`./main.py [-fFILE] [-nCOUNT] [-dDEST_LANG] [-intl] [-lines] [-unsafe]`

`-fFILE`: 从指定文件读取翻译内容；如不指定该选项则从输入读取，直到遇到空行。

`-nCOUNT`:在翻译回目标语言之前随机翻译的次数。默认为5。

`-dDEST_LANG`：目标语言。形如`en`、`zh-cn`、`es`等。默认为`zh-cn`。

`-intl`：使用国际版Google翻译网址`translate.google.com`。由于项目面向中国受众使用较多，默认为`translate.google.cn`。

`-lines`：逐行翻译（仅用于文件）。默认关闭。

`-unsafe`：不在作者指定的一组Google翻译支持更为完善的语言中翻译。默认关闭。

# Usage

`./main.py [-fFILE] [-nCOUNT] [-dDEST_LANG] [-intl] [-lines] [-unsafe]`

`-fFILE`: Read text for translation from FILE. if omitted, read Stdin until an empty line.

`-nCOUNT`: How many times of randomly translation before going back to DEST_LANG. 5 for default.

`-dDEST_LANG`: Destination language. Looks like `en`、`zh-cn`、`es` etc. `zh-cn` is the default.

`-intl`: Use international URL `translate.google.com`. `translate.google.cn` is the default since this project mainly
oriented to Chinese users.

`-lines`: Translate in line-by-line manner (for files onky). Disabled by default. 

`-unsafe`: Translate outside the set of languages for which Google Translate may have a better support. 
Disabled by default. 
