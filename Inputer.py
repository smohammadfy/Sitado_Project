from DB_Connection import *
from colorama import Fore


def inputer():
    cur, conn = connect()
    print("what do you want to do?(insert,...)")
    job = input(" > ")
    if (job == 'insert'):
        sql = "INSERT INTO "
        insert(sql, cur, conn)


def conn_closer(conn):
    conn.close()


def insert(sql, cur, conn):
    user = '("Name","Last_Name","User_id","Phone_Number","Age")'
    print("which table do you want to insert?(Users,Menu,Shops,Transporter)")
    table = input(" > ")
    if (table not in ['Users', 'Menu', 'Shops', 'Transporter']):
        print("Table name is Invalid !")
        return insert(sql, cur, conn)
    else:
        if (table == 'Users'):
            sql = sql + '"' + table + '"' + user + 'VALUES(%s,%s,%s,%s,%s)'
            print('Enter Name :')
            name = input(' > ')
            print('Enter Last Name :')
            lastname = input(' > ')
            print('Enter User_id :')
            userid = int(input(' > '))
            print('Enter phone number :')
            phonenumber = int(input(' > '))
            print('Enter Age :')
            age = int(input(' > '))
            try:
                cur.execute(sql, (name, lastname, userid, phonenumber, age))
                conn.commit()
                print(Fore.BLUE + "Successful!")
            except (Exception,) as error:
                print(Fore.RED + "ERROR : ")
                print(error)
