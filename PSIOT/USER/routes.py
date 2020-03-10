from flask import Blueprint, jsonify,request
from PSIOT.USER.data_access import get_user
# import datetime

USER = Blueprint('USER', __name__)


@USER.route("/user",methods=['GET'])
def user():
    username = request.args.get('username')    
    password = request.args.get('password')   
    if username is not None and password is not None:
        result = get_user(username,password)
    return jsonify(result)
    #---------------------------------------------------------------
