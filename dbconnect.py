
'''
import MySQLdb as my

    # MariaDB connect
    # con = my.connect(host='mysql108.phy.lolipop.lan', port=3306, user='LAA0752660', password='itmoserver', database='LAA0752660-itmoserver', use_unicode=True, charset='utf8')
    con = my.connect(host='localhost', user='root', authentication_string='NULL',  database='itmonoserver', use_unicode=True, charset='utf8')
    cursor = con.cursor()
    statement = "select * from item"
    cursor.execute(statement)
    records = cursor.fetchall()
    con.close()

    for record in records:
        print(record[0] + record[1])




'''
'''

from six.moves.urllib.parse import urlparse
#from urllib.parse import urlparse
import mysql.connector

url = urlparse('mysql://user:pass@localhost:3306/dbname')

conn = mysql.connector.connect(
    host = url.hostname or 'localhost',
    port = url.port or 3306,
    user = url.username or 'root',
    password = url.password or '',
    database = url.path[1:] or 'itmonoserver'
)
'''

# coding:utf-8
import mysql.connector

try:
    # con = my.connect(host='mysql108.phy.lolipop.lan', port=3306, user='LAA0752660', password='itmoserver', database='LAA0752660-itmoserver', use_unicode=True, charset='utf8')
    # con = my.connect(host='localhost', user='root', authentication_string='NULL',  database='itmonoserver', use_unicode=True, charset='utf8')

#test-server
    dbh = mysql.connector.connect(
            host='localhost',
            port=3306,
            db='itmonoserver',
            user='root',
            # authentication_string='root'
        )

#develop-server

    stmt = dbh.cursor(buffered=True)


    sql = "select count(*) from item"

    print(sql)

    stmt.execute(sql)
    rows = stmt.fetchall()

    for row in rows:
        print(row[0])


    sql2 = "SELECT item.* FROM item"
    print(sql2)

    stmt.execute(sql2)
    rows = stmt.fetchall()

    for row in rows:
        print(rows)

    insert_sql = "INSERT INTO item (uid , code , name , kakaku) VALUES (%s, %s, %s, %s)"
    insert_data = (2, 2, 2222, 5040)
    stmt.execute(insert_sql, insert_data)
    dbh.commit()

    stmt.close()
    dbh.close()

#    rows = stmt.fetchall()


except (mysql.connector.errors.ProgrammingError) as e:
    print (e)