from DB_Connection import *
from colorama import Fore

def log():
    cur, conn = connect()
    sql = "Select * from "
    print(
        "which table_log do you want to see?(Users,Menu,NameLessOrder,Report,Shop_Rest_Order,UserOrder,User_Report,Shops,Transporter)")
    table = input(" > ")
    if (table not in ['Users', 'Menu', 'Shops', 'Transporter', 'NameLessOrder', 'Report', 'Shop_Rest_Order',
                      'UserOrder', 'User_Report']):
        print("Table name is Invalid !")
    else:
        sql = sql + '"' + table + '_Log' + '"'
        try:
            cur.execute(sql)
            record = cur.fetchall()
            print(Fore.BLUE + "Successful!")
            for row in record:
                print(row)
        except (Exception,) as error:
            print(Fore.RED + "ERROR : ")
            print(error)
