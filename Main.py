from Inputer import inputer
from Show_Log import log
from Order_Submit import submit


def Main():
    submit()
    print("What part of User_Interface do you want to use ? ( inputer , log_viewer , OrderSubmit ...) ")
    part = input(' > ')
    if (part not in ['inputer', 'log_viewer', 'OrderSubmit']):
        print("your input is incorrect , please try again !")
        Main()
    elif (part == 'inputer'):
        inputer()
    elif (part == 'log_viewer'):
        log()
    elif (part == 'OrderSubmit'):
        submit()


if __name__ == '__main__':
    Main()
