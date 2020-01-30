from Inputer import inputer
from Show_Log import log
from Order_Submit import submit
from Show_User_Report import userreport
from Manager_Report import  managerreport

def Main():
    print("What part of User_Interface do you want to use ? ( inputer , log_viewer , OrderSubmit , UserReport , ManagerReport) ")
    part = input(' > ')
    if (part not in ['inputer', 'log_viewer', 'OrderSubmit' , 'UserReport' , 'ManagerReport']):
        print("your input is incorrect , please try again !")
        Main()
    elif (part == 'inputer'):
        inputer()
    elif (part == 'log_viewer'):
        log()
    elif (part == 'OrderSubmit'):
        submit()
    elif (part =='UserReport'):
        userreport()
    elif (part == 'ManagerReport'):
        managerreport()



if __name__ == '__main__':
    Main()
