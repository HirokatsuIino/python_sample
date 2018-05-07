# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/"
url2 = "https://mainichi.jp/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)
html2 = urllib2.urlopen(url2)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
soup2 = BeautifulSoup(html2, "html.parser")

# タイトル要素を取得し出力する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
print soup.title.string
print soup2.title.string


