from flask import Blueprint, jsonify,request
from PSIOT.NVR.data_access import get_NVR
from PSIOT.NVR.data_access import get_NVR_where
from PSIOT.NVR.data_access import Insert_NVR
# import datetime

NVR = Blueprint('NVR', __name__)

@NVR.route("/NVR_Record",methods=['GET'])
def NVR_Record():
    result = get_NVR()
    return jsonify(result)

@NVR.route("/NVR_Records",methods=['GET'])
def NVR_Records():
    ID_NVR = request.args.get('ID_NVR')    
    NVR = request.args.get('NVR')   
    NVR_Loc = request.args.get('NVR_Loc')   
    if ID_NVR is None:
        ID_NVR =""
    if NVR is None:
        NVR=""
    if NVR_Loc is None:
        NVR_Loc =""
    result = get_NVR_where(ID_NVR,NVR,NVR_Loc)
    return jsonify(result)
    #---------------------------------------------------------------

@NVR.route('/add_NVR', methods=['POST'])
def add_NVR():
    Vnvr = request.args.get('NVR')
    Vnvr_loc = request.args.get('NVR_LOC')
    Vdescription = request.args.get('DESCRIPTION')
    if Vnvr is None :  
        Vnvr = ""
    if Vnvr_loc is None :  
        Vnvr_loc = ""    
    if Vdescription is None :  
        Vdescription = ""
    #---------------------------------------------------------------
    result = Insert_NVR(Vnvr,Vnvr_loc,Vdescription)
    if result > 0:
        result = {
                    'code':200,
                    'data':{
                        'USERID' : "",
                        'EMTAILTOKEN' : "",
                        'EMAIL' : ""
                    },
                    "message": {
                                "en": "success",
                                "th": "สำเร็จ"
                            }
                    }   
    return jsonify(result), 200
Update_nve

@NVR.route('/update_NVR', methods=['PUT'])
def add_NVR():
    VID_nvr = request.args.get('ID_NVR')
    Vnvr = request.args.get('NVR')
    Vnvr_loc = request.args.get('NVR_LOC')
    Vdescription = request.args.get('DESCRIPTION')
    if VID_nvr is not None :
        if Vnvr is None :  
            Vnvr = ""
        if Vnvr_loc is None :  
            Vnvr_loc = ""    
        if Vdescription is None :  
            Vdescription = ""
        #---------------------------------------------------------------
        result = Insert_NVR(VID_nvr,Vnvr,Vnvr_loc,Vdescription)
        if result > 0:
            result = {
                        'code':200,
                        'data':{
                            'USERID' : "",
                            'EMTAILTOKEN' : "",
                            'EMAIL' : ""
                        },
                        "message": {
                                    "en": "success",
                                    "th": "สำเร็จ"
                                }
                        }   
        return jsonify(result), 200
