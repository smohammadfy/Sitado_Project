from Inputer import inputer
from Show_Log import log


def Main():
    print("What part of User_Interface do you want to use ? ( inputer , log_viewer , ...) ")
    part = input(' > ')
    if (part not in ['inputer', 'log_viewer']):
        print("your input is incorrect , please try again !")
        Main()
    elif (part == 'inputer'):
        inputer()
    elif (part == 'log_viewer'):
        log()


if __name__ == '__main__':
    Main()
