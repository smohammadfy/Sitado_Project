from DB_Connection import *
from colorama import Fore


def managerreport():
    cur, conn = connect()
    print("Please Enter Report id :")
    report_id = str(input(' > '))
    report_id = report_id.__str__()
    report_id = "'" + report_id + "'"
    report = 'SELECT * from ' + '"' + 'Report' + '"' + ' where ' + '"' + 'report_id' + '"' + ' = ' + report_id
    try:
        cur.execute(report)
        report_recorde = cur.fetchall()
        print(Fore.YELLOW)
        print("Out put Order is : Profit , Cost , Price , singel_price , report_id")
        print(report_recorde)
    except (Exception,) as error:
        print(Fore.RED + "ERROR : ")
        print(error)
    finally:
        conn.close()
