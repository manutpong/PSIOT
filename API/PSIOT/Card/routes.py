from flask import Blueprint, jsonify,request
from PSIOT.Card.data_access import GetCARD
# import datetime

CARD = Blueprint('CARD', __name__)

@CARD.route("/GetCARD",methods=['GET'])
def GetCARD():
    # name= request.args.get('name')    
    # surname = request.args.get('surname')
    # if name is None:
    #     name =""
    # if surname is None:
    #     surname=""
    result = GetCARD()
    # data = result.to_dict(orient='records') 
    return jsonify(result)

