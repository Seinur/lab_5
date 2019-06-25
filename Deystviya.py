import sqlite3
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()


def function():
    print("До изменений:")
    for row in cursor.execute("SELECT * FROM student"):
        print(row)
    dele=input("1-удалить запись, 0-добавить,3- редактирование \n")
    if dele is '1':
        i=int(input("Введите запись, которую хотите удалить(по id) \n"))
        cursor.execute("DELETE FROM student WHERE id =?",(i,))
        conn.commit()
    elif dele is '0':
        print("Введите запись ")
        id=int(input("id(int!) \n"))
        name = input("name  \n")
        vuz = input("vuz  \n")
        idstudaka =int( input("idstudaka(int1!)  \n"))
        kurs = input("kurs  \n")
        gruppa = input("gruppa  \n")
        tel = input("tel  \n")
        datarojdeniya = input("datarojdeniya  \n")
        cursor.execute('''INSERT INTO student (id,name, vuz, idstudaka,
                   kurs, gruppa, tel,datarojdeniya) VALUES (?,?,?,?,?,?,?,?)''',
                   (id,name, vuz, idstudaka,kurs, gruppa, tel,datarojdeniya))
        conn.commit()
    elif dele=='3':
        i1=int(input("Введите номер записи, которую хотите отредактировать \n"))
        i=input("Введите поле, которое хотитет отредакитровать \n")
        i2=input("Введите то, на что хотите изменить запись \n")
        cursor.execute("""UPDATE student SET  {0} = ? WHERE id = ?""".format(i),(i2,i1))
        conn.commit()
    print("После изменений ")
    for row in cursor.execute("SELECT * FROM student"):
        print(row)
    print("Запустить программу еще раз? 1-да 0-нет")
    answer=input()
    if answer is '1':
        function()


function()