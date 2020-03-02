# from pyrfc import Connection
import mysql.connector
import pandas as pd
from flask import current_app
from mysql.connector import Error

class CON_MYSQL(object):
    def __init__(self):
        self.host = current_app.config['MYSQL_HOST']
        self.user = current_app.config['MYSQL_USER']
        self.passwd = current_app.config['MYSQL_PASS']
        self.db = current_app.config['MYSQL_DB']
        self._connection = None
        self._cursor = None
        self.connect()

    def __del__(self):
        self.disconnect()

    def connect(self):        
        try:
            self._connection = mysql.connector.connect(
                host= self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.db
            )
            if self._connection.is_connected():
                db_Info = self._connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self._cursor = self._connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)
      

    @property
    def get_cursor(self):
        return self._connection.cursor()

    def disconnect(self):
        self._connection.close()



    # def query(self, sql, params=None):
    def query(self, sql):
        try:
            self._cursor.execute(sql)
            myresult = self._cursor.fetchall()
            return myresult

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if  self._connection.is_connected():
                self._connection.close()
                self._cursor.close()
                print("MySQL connection is closed")
    
    # recordTuple =(CAMERA_ID,Camera,Camera_Loc,Record_id)
    # result = CON_MYSQL.query(sql,recordTuple)
    
    def data_query(self, sql,recordTuple):
        try:
            print(sql)
            print(recordTuple)
            # self._cursor = self._cursor(buffered=True)
            self._cursor.execute(sql,recordTuple)
            myresult = self._cursor.fetchall()
            return myresult

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if  self._connection.is_connected():
                self._connection.close()
                self._cursor.close()
                print("MySQL connection is closed")

    def insert_query(self, sql,recordTuple):
        try:
            print(sql)
            print(recordTuple)
            # self._cursor = self._cursor(buffered=True)
            self._cursor.execute(sql,recordTuple)
            self._connection.commit()
            print(self._cursor.rowcount, "record inserted.")
            return self._cursor.rowcount

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if  self._connection.is_connected():
                self._connection.close()
                self._cursor.close()
                print("MySQL connection is closed")
  
    def Update_query(self, sql,recordTuple):
        try:
            print(sql)
            print(recordTuple)
            # self._cursor = self._cursor(buffered=True)
            self._cursor.execute(sql,recordTuple)
            self._connection.commit()
            print(self._cursor.rowcount, "record Updates.")
            return self._cursor.rowcount

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if  self._connection.is_connected():
                self._connection.close()
                self._cursor.close()
                print("MySQL connection is closed")