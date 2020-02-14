from flask import Blueprint, jsonify,request
from PSIOT.NVR.data_access import get_NVR
from PSIOT.NVR.data_access import get_NVR_where
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

# def get_NVR_Detail(CAMERA_ID,Camera,Camera_Loc,Record_id):
@NVR.route("/NVR_Records",methods=['GET'])
def NVR_Records():

    ID_NVR = request.args.get('ID_NVR')    
    NVR = request.args.get('NVR')   
    NVR_Loc = request.args.get('NVR_Loc')   
    print(NVR_Loc)
    if ID_NVR is None:
        ID_NVR =""
    if NVR is None:
        NVR=""
    if NVR_Loc is None:
        NVR_Loc =""

    result = get_NVR_where(ID_NVR,NVR,NVR_Loc)
    # data = result.to_dict(orient='records') 
    return jsonify(result)
