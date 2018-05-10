# coding: UTF-8
import requests
# import urllib.request, urllib2.error
# import urllib2
import mysql.connector
from bs4 import BeautifulSoup

def deconnect(title):
    # coding:utf-8

    try:
        # test-server
        dbh = mysql.connector.connect(
            host='localhost',
            port=3306,
            db='itmonoserver',
            user='root',
            # authentication_string='root'
        )

        # develop-server

        stmt = dbh.cursor(buffered=True)
        insert_sql = "INSERT INTO item (uid , code , name , kakaku) VALUES (%s, %s, %s, %s)"
        insert_data = (3, 3, title, 3)
        stmt.execute(insert_sql, insert_data)
        dbh.commit()

        stmt.close()
        dbh.close()

    #    rows = stmt.fetchall()

    except (mysql.connector.errors.ProgrammingError) as e:
        print (e)



# アクセスするURL
# url = "http://www.nikkei.com/"
url = "https://www.yodobashi.com/category/19531/38009/38053/"

#url2 = "https://mainichi.jp/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
r = requests.get(url)
# html = urllib2.urlopen(url)
#html2 = urllib2.urlopen(url2)

# htmlをBeautifulSoupで扱う
# content_type_encoding = 'UTF-8'
# content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
# soup = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)
soup = BeautifulSoup(r.content, 'html.parser')


# soup = BeautifulSoup(r.content, "html.parser")
# soup = BeautifulSoup(html, "html.parser")
#soup2 = BeautifulSoup(html2, "html.parser")


# 最初のh1タグ取得
# div = soup.div
# print(div)  # <h1 class="one">H1_String</h1>

# h1タグの属性を取得
# print(div.attrs)  # {'class': ['one']}

# h1タグのclassを取得
# print(h1['class'])  # ['one']

# h1タグのタグ名を取得
# print(div.name)  # h1

# elems = soup.select('#listContents')
# for elem in elems:
#     print(elem)



elem_class = soup.select('.inner .pName p')
# TODO 全角文字列がunicode出力される
print(elem_class)

# 最初のpタグ取得
# print(soup.p)  # <p>おすすめ商品</p>

# divタグの次のpタグ取得
# print(soup.div.p)  # <p>とってもキュートな商品。</p>

# divタグの次のpタグの内部テキストを取得
# print(soup.div.p.string)  # とってもキュートな商品。


# div = soup.find_all("div")
#
# syohin_mei = ""
# string0_ = ""
# string_ = ""
# for tag in div:
#     try:
#         string0_ = tag.get("class")
#         string_ = tag.get("class").pop(0)
#         if string_ in "pName":
#             syohin_mei = tag.string
#             break
#     except:
#         pass
#
#     print syohin_mei
#     print string0_
#     print string_



# タイトル要素を取得し出力する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
# print soup.title.string
#print soup2.title.string

#deconnect(unicode(soup2.title.string, 'utf_8'))

