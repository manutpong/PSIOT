from flask import Blueprint, jsonify,request
from PSIOT.NVR.data_access import get_NVR

# import datetime

NVR = Blueprint('NVR', __name__)

@NVR.route("/NVR_Record",methods=['GET'])
def NVR_Record():
    # name= request.args.get('name')    
    # surname = request.args.get('surname')
    # if name is None:
    #     name =""
    # if surname is None:
    #     surname=""
    result = get_NVR()
    # data = result.to_dict(orient='records') 
    return jsonify(result)

