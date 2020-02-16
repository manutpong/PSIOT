import pandas as pd
import ctypes
# from PSIOT.utils.mysql_connect import CON_MYSQL


def GetCARD():
    hllDll = ctypes.WinDLL ("..\\API\\PSIOT\\DLL\\License61-62\\scapi_ope.dll")
    # CONSQL = CON_MYSQL()
    # sql = "SELECT * FROM main_device"
    # result = CONSQL.query(sql)    
    # print(result)
    # return result
