import binascii

from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from apps.utils.crypto import SymmetricEncryption, H2_hash_function

CE_bp = Blueprint('CE', __name__, url_prefix='/ce')
api = Api(CE_bp)

CE_parser = reqparse.RequestParser()
CE_parser.add_argument('Flag',
                       type=str,
                       required=True,
                       help='Must provide the Flag (Flag=1: CE starts the conversation with MH;'
                            'Flag=0, CE receives c2 from MH)',
                       location=['form', 'args'])
CE_parser.add_argument('c2',
                       type=str,
                       location=['form', 'args'])

class CESecureCommunicationWithMHApi(Resource):
    def get(self):
        pass

    def post(self):
        args = CE_parser.parse_args()
        flag = args.get('Flag')

        # flag == "0", CE starts the conversation with MH.
        if flag == "0":
            data = {
                "status": 200,
                "msg": "CE starts the conversation with MH.",
                "Flag": "0"
            }

            return data

        # flag == "1", CE will receive the c2 from MH and then decrypt c2 as m2 in order to get (r1, t2)
        if flag == "1":
            c2 = args.get('c2')
            print('c2: ', c2)
            c2 = binascii.unhexlify(c2.encode('utf-8'))
            encryptor = SymmetricEncryption()
            nounce = 'ymNIaotdN3EQPMHpl+gZTkhYNQqGu7eHUG+MBAIbfOE='
            m2 = encryptor.decryption(c2, nounce).decode('utf-8')
            # m2 = str(r1) + ' ' + str(t2) + ' ' + str(DMi) + ' ' + H2
            m2_list = m2.split(' ')
            # r1
            r1 = m2_list[0]
            # t2
            t2_date = m2_list[1]
            t2_time = m2_list[2]
            t2 = t2_date + ' ' + t2_time
            # DMi
            DMi = m2_list[-2]
            # H2
            H2 = m2_list[-1]

            temp = r1 + t2 + DMi
            res = H2_hash_function(temp)

            if res == H2:
                data = {
                    "status": 200,
                    "r1": r1,
                    "t2": t2,
                    "Flag": "1"
                }
            else:
                data = {
                    "status": 400,
                    "msg": "Auth is failed."
                }

            return data

api.add_resource(CESecureCommunicationWithMHApi, '/CE2MH')
