from DB_Connection import *
from colorama import Fore


def inputer():
    cur, conn = connect()
    print("what do you want to do?(insert,delete,update,end)")
    job = input(" > ")
    if (job == 'insert'):
        sql = "INSERT INTO "
        insert(sql, cur, conn)
    elif (job == 'delete'):
        sql = "DELETE FROM "
        delete(sql, cur, conn)
    elif (job == 'update'):
        sql = "UPDATE "
        update(sql, cur, conn)
    elif (job == 'end'):
        conn_closer(conn)


def conn_closer(conn):
    conn.close()


def update(sql, cur, conn):
    print("which table do you want to update?(Users,Menu,Shops,Transporter)")
    table = input(" > ")
    if (table not in ['Users', 'Menu', 'Shops', 'Transporter']):
        print("Table name is Invalid !")
    else:
        sql = sql + '"' + table + '" '
        print('Enter command :')
        print('hint : SET "User_id" = 21295131 WHERE "User_id" = 21295132')
        command = input(' > ')
        sql = sql + command
        try:
            cur.execute(sql)
            conn.commit()
            print(Fore.BLUE + "Successful!")
        except (Exception,) as error:
            print(Fore.RED + "ERROR : ")
            print(error)


def delete(sql, cur, conn):
    print("which table do you want to delete?(Users,Menu,Shops,Transporter)")
    table = input(" > ")
    if (table not in ['Users', 'Menu', 'Shops', 'Transporter']):
        print("Table name is Invalid !")
        return delete(sql, cur, conn)
    else:
        sql = sql + '"' + table + '" '
        print('Enter condition :')
        print('hint : Where "User_id" = 21295131')
        condition = input(' > ')
        sql = sql + condition
        try:
            cur.execute(sql)
            conn.commit()
            print(Fore.BLUE + "Successful!")
        except (Exception,) as error:
            print(Fore.RED + "ERROR : ")
            print(error)


def insert(sql, cur, conn):
    user = '("Name","Last_Name","User_id","Phone_Number","Age")'
    menu = '("Item_id","Item_Name","Item_Price")'
    shop = '("Shop_id","Shop_Name","Shop_items","Shop_prices")'
    transporter = '("Name","Last_Name","Transporter_id","phonenumber")'
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
        elif (table == 'Menu'):
            sql = sql + '"' + table + '"' + menu + 'VALUES(%s,%s,%s)'
            print('Enter Item id :')
            Item_id = input(' > ')
            print('Enter Item Name :')
            Item_Name = input(' > ')
            print('Enter Item_Price :')
            Item_Price = int(input(' > '))
            try:
                cur.execute(sql, (Item_id, Item_Name, Item_Price))
                conn.commit()
                print(Fore.BLUE + "Successful!")
            except (Exception,) as error:
                print(Fore.RED + "ERROR : ")
                print(error)
        elif (table == 'Transporter'):
            sql = sql + '"' + table + '"' + transporter + 'VALUES(%s,%s,%s,%s)'
            print('Enter Name :')
            Name = input(' > ')
            print('Enter Last Name :')
            Last_Name = input(' > ')
            print('Enter Transporter id :')
            Transporter_id = int(input(' > '))
            print('Enter phone number :')
            PhoneNumber = int(input(' > '))
            try:
                cur.execute(sql, (Name, Last_Name, Transporter_id, PhoneNumber))
                conn.commit()
                print(Fore.BLUE + "Successful!")
            except (Exception,) as error:
                print(Fore.RED + "ERROR : ")
                print(error)
        elif (table == 'Shops'):
            sql = sql + '"' + table + '"' + shop + 'VALUES(%s,%s,%s,%s)'
            print('Enter Shop id :')
            Shop_id = input(' > ')
            print('Enter Shop Name :')
            Shop_Name = input(' > ')
            print('Enter Shop Items :')
            print('( hint :input must be like this  {"chicken","labster","meat"} )')
            Shop_items = input(' > ')
            print('Enter Item_Prices :')
            print('( hint :input must be like this  {20000,10000000,500} )')
            Shop_prices = input(' > ')
            try:
                cur.execute(sql, (Shop_id, Shop_Name, Shop_items, Shop_prices))
                conn.commit()
                print(Fore.BLUE + "Successful!")
            except (Exception,) as error:
                print(Fore.RED + "ERROR : ")
                print(error)
