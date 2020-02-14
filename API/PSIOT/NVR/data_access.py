import pandas as pd
from PSIOT.utils.mysql_connect import CON_MYSQL


def get_NVR():
    CONSQL = CON_MYSQL()
    sql = "SELECT * FROM main_device"
    result = CONSQL.query(sql)    
    print(result)
    return result

def get_NVR_where(ID_NVR,NVR,NVR_LOC):
    CONSQL = CON_MYSQL()
    Tuple = ()
    sql = "SELECT * FROM main_device"
    if ID_NVR != "" or NVR != "" or NVR_LOC != "":
        sql += " where" 
        if ID_NVR != "": 
            if len(Tuple) != 0:
                sql += " and "   
            sql += " ID_NVR = %s"
            Tuple = (*Tuple,"{}".format(ID_NVR))
        if NVR != "":
            if len(Tuple) != 0:
                sql += " and "   
            sql += " NVR like %s"
            Tuple = (*Tuple,"%{}%".format(NVR))
        if NVR_LOC != "":
            if len(Tuple) != 0:
                sql += " and "   
            sql += " NVR_LOC like %s"
            Tuple = (*Tuple,"%{}%".format(NVR_LOC))
    recordTuple = Tuple
    print("SQL = "+sql)
    print(recordTuple)
    result = CONSQL.data_query(sql,recordTuple)
    print(result)
    return result

def add_NVR(ID_NVR,NVR,NVR_LOC,DESCRIPTION):
    CONSQL = CON_MYSQL()

    sql = "insert into main_device (NVR,NVR_LOC,DESCRIPTION)"
    sql += " VALUES (%s, %s, %s)"
    if NVR != "" :
        recordTuple = (NVR,NVR_LOC,DESCRIPTION)
        CONSQL.insert_query(sql,recordTuple)

# def get_NVR(CAMERA_ID,camera,camera_Loc,Description,Record_id){
#     CONSQL = CON_MYSQL()
#     sql = "SELECT * FROM main_device"
#     sql += " where CAMERA_ID = %s"
#     sql += " and camera = %s"

# # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
# }
