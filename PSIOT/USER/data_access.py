import pandas as pd
from PSIOT.utils.mysql_connect import CON_MYSQL




def get_user(username,password):
    CONSQL = CON_MYSQL()
    Tuple = ()
    sql = "SELECT * FROM user "
    sql += "where username = %s and password = %s"
    Tuple = (username,password)
    print("SQL = "+sql)
    print(Tuple)
    result = CONSQL.data_query(sql,Tuple)
    print(result)
    return result

