
import mysql.connector as con

def connecntionDb():
    db = con.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '22032002',
        database = 'db_apotek'
    )
    return db