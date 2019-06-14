from django.shortcuts import render
from lazarus.contract_config import *
from lazarus.settings import web3
from rest_framework.views import APIView

# Create your views here.

class TransferToken(APIView):
    api_view = ['POST', ]

    """
    Method Post
    Description - To transfer lazarus token to another account
    Request Parameter - Address, and API-Token-Key
    Respose Data - {}
    """

    def post(request):
        try:
            get_api_key = request.data['api-key']
            get_to_address = request.data['to_address']
            amount = request.data['amount']
            msg = ""

            try:
                contract_instance = web3.eth.contract(contract_abi, contract_address)
                result = contract_instance.call()
                unlock_status = web3.personal.unlockAccount(account_add, account_pass)

                if unlock_status:
                    transaction_hash =  contract_instance.transact({'from' : account_add}).send(get_to_address, amount, msg)
                    if transaction_hash:
                        return Response(dict({"Success" : "Token has been transfered Successfully"}), status=status.HTTP_200_OK)
                    else:
                        return Response(dict({"Info" : "Token transfer Failed"}), status=status.HTTP_404_NOT_FOUND)  
                else:
                    return Response(dict({"Info" : "Not able to unlock address"}), status=status.HTTP_404_NOT_FOUND)                
            except Exception as e:
                return Response(dict({"Info" : e}), status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response(dict({"Info" : e}), status=status.HTTP_404_NOT_FOUND)
        
