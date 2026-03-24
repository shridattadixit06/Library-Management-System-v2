import sqlite3
e_conn = sqlite3.connect("books\\economics_books.db")
p_conn = sqlite3.connect("books\\programming_books.db")
s_conn = sqlite3.connect("books\\science_books")
e_cursor = e_conn.cursor()
p_cursor = p_conn.cursor()
s_cursor = s_conn.cursor()

e_cmd = """CREATE TABLE IF NOT EXISTS economics(bookname TEXT, bookID TEXT PRIMARY KEY)"""
p_cmd = """CREATE TABLE IF NOT EXISTS programming(bookname TEXT, bookID TEXT PRIMARY KEY)"""
s_cmd = """CREATE TABLE IF NOT EXISTS science(bookname TEXT, bookID TEXT PRIMARY KEY)"""
e_cursor.execute(e_cmd)
p_cursor.execute(p_cmd)
s_cursor.execute(s_cmd)
e_conn.commit()
p_conn.commit()
s_conn.commit()
e_conn.close()
p_conn.close()
s_conn.close()