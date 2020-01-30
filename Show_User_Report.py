from DB_Connection import *
from colorama import Fore


def userreport():
    cur, conn = connect()
    print("Enter User id :")
    userid = str(input(' > '))
    report = 'Select * from ' + '"' + 'User_Report' + '"' + 'where ' + '"' + 'User_id' + '"' + ' = ' + userid
    try:
        cur.execute(report)
        report_recorde = cur.fetchall()
        print(Fore.YELLOW)
        print(report_recorde)
    except (Exception,) as error:
        print(Fore.RED + "ERROR : ")
        print(error)
    finally:
        conn.close()
