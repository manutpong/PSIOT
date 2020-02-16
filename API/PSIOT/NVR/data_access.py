import pandas as pd
from PSIOT.utils.mysql_connect import CON_MYSQL


def get_NVR():
    CONSQL = CON_MYSQL()
    sql = "SELECT * FROM main_device"
    result = CONSQL.query(sql)    
    print(result)
    return result

# def get_NVR(CAMERA_ID,camera,camera_Loc,Description,Record_id){
#     CONSQL = CON_MYSQL()
#     sql = "SELECT * FROM main_device"
#     sql += " where CAMERA_ID = %s"
#     sql += " and camera = %s"

# # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
# }
