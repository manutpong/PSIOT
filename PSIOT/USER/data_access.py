import pandas as pd
from PSIOT.utils.mysql_connect import mysql_connect




def get_user(username,password):
    CONSQL = mysql_connect()
    Tuple = ()
    sql = "SELECT * FROM user "
    sql += "where username = %s and password = %s"
    if username is None :  
        username = ""    
    if password is None :  
        password = ""
    Tuple = (username,password)
    print("SQL = "+sql)
    print(Tuple)
    result = CONSQL.query(sql,Tuple)
    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    print(result)
    return result

