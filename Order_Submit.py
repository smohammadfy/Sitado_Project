from DB_Connection import *
from colorama import Fore
from datetime import datetime

def submit():
    cur, conn = connect()
    menu = "Select * from " + '"' + 'Menu' + '"'
    order = []
    order_temp = []
    isuser = is_user()
    print(Fore.YELLOW + "Menu Of Sitado : \n")
    try:
        cur.execute(menu)
        menu_record = cur.fetchall()
        for row in menu_record:
            print(row)
    except (Exception,) as error:
        print(Fore.RED + "ERROR : ")
        print(error)
    order = order + get_order()
    call_to_order = True
    while (call_to_order is True):
        print("Do you have any order ?(yes,no)")
        anyorder = input(' > ')
        if (anyorder not in ['yes', 'no']):
            print("invalid input ! Do you have any order ? (yes,no)")
            anyorder = input(' > ')
        if (anyorder == 'yes'):
            order_temp = get_order()
            order = order + order_temp
            call_to_order = True
        elif (anyorder == 'no'):
            call_to_order = False
    print("your order is :")
    print(order)
    order_prices, total_price = get_price_of_order(cur, conn, order)
    print("your order prices is :")
    print(order_prices)
    print("total price of order is :")
    print(total_price)
    if (isuser):
        submit_order_in_User_Order(cur, conn, order , total_price , order_prices)
    elif (not isuser):
        submit_order_in_NameLessOrder(cur, conn, order , total_price , order_prices)


def is_user():
    print("Are you a user of Sitado ?(yes/no)")
    isuser = input(' > ')
    if (isuser not in ['yes', 'no']):
        print("invalid input ! try Again")
        is_user()
    elif (isuser == 'yes'):
        return True
    elif (isuser == 'no'):
        return False


def get_order():
    print(Fore.WHITE + "What do you want to order ? (please enter name of menu item)")
    order_id = input(' > ')
    print("How many of that items do you want ?")
    order_number = int(input(' > '))
    order = []
    for i in range(order_number):
        order.append(order_id)
    return order



def submit_order_in_User_Order(cur, conn, order , total_price , order_prices):


def submit_order_in_NameLessOrder(cur, conn, order , total_price , order_prices):
    transporter_needed  = False
    insert = 'INSERT into ' + '"' + 'NameLessOrder' + '"' + 'Values(%s,%s,%s,%s,%s,%s)'
    print("please input an id for this order : ")
    order_id = input(' > ')
    print("please Enter An Address(if you serve here say no)")
    Address = input(' > ')
    if(Address == 'no'):
        transporter_needed = False
        Address = 'serve here'
    else:
        transporter_needed = True
        dt = datetime.now()
    try:
        cur.execute(insert,(total_price,order_id,order_prices,order,Address,dt,))
    except (Exception,) as error:
        print(Fore.RED + "ERROR : ")
        print(error)

def get_price_of_order(cur, conn, order):
    get_price = 'SELECT' + '"' + 'Item_Price' + '"' + 'from ' + '"' + 'Menu' + '" ' + 'WHERE' + '"' + 'Item_Name' + '" ' + '= %s'
    singel_order = ''
    order_price = []
    price = 0
    total_price = 0
    for i in range(order.__len__()):
        singel_order = order[i]
        try:
            cur.execute(get_price, (singel_order,))
            price = cur.fetchone()
            for row in price:
                order_price.append(row)
        except (Exception,) as error:
            print(Fore.RED + "ERROR : ")
            print(error)
    for i in range(order_price.__len__()):
        total_price += order_price[i]
    return order_price, total_price
