from flask import Blueprint, jsonify,request
from PSIOT.NVR.data_access import get_NVR
from PSIOT.NVR.data_access import get_NVR_where
from PSIOT.NVR.data_access as db
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
    #---------------------------------------------------------------

@NVR.route('/add_NVR', methods=['POST'])
def add_NVR():
    Vnvr = request.json.get('NVR', None).
    Vnvr_loc = request.json.get('NVR_LOC', None)
    Vdescription = request.json.get('DESCRIPTION', None)
    #---------------------------------------------------------------
    result = db.Insert_NVR(Vnvr,Vnvr_loc,Vdescription)
    result = {
                'code':200,
                'data':{
                    'USERID' : ,
                    'EMTAILTOKEN' : ,
                    'EMAIL' : 
                },
                "message": {
                            "en": "success",
                            "th": "สำเร็จ"
                        }
                }   
    return jsonify(result), 200
