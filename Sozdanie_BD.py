import sqlite3
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student
                  (id integer,name text, vuz text, idstudaka integer, kurs integer,
                   gruppa text, tel  text, datarojdeniya text)
               """)
