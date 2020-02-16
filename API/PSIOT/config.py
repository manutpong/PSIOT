import os
import datetime

class Config:
    MYSQL_HOST = 'psiot.blogdns.com'
    MYSQL_USER = 'admin'
    MYSQL_PASS = 'Ps123456'
    MYSQL_DB     = 'psiot'
    SECRET_KEY = '4aoqSpq9gPW9DBLbfplpyfDGlumCoB5b'
    JWT_SECRET_KEY = '5KqXLIvagLqVqtSix9IvPZGfLeFWuKRE'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    PORT='8081'


    # SAP_ASHOST = '10.1.200.58'
    # SAP_SYNR = '00'
    # SAP_CLIENT = '350'
    # SAP_USER = 'fiit'
    # SAP_PASSWD = 'mfudev'
    # SECRET_KEY = '4aoqSpq9gPW9DBLbfplpyfDGlumCoB5b'
    # JWT_SECRET_KEY = '5KqXLIvagLqVqtSix9IvPZGfLeFWuKRE'
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    # PORT='8081'


 