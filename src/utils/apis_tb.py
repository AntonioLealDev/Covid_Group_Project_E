# apis_tb.py 
# Creator: Alejandro Balseiro
# Last review: 22/01/2021 by Javier Olcoz


import pandas as pd
import numpy as np
import json
import requests

class Apis:

    def requester (self, url_b, url_add, psw ):
        """
        @Alex
        Function that helps us to make the call to the server to recieve the appropiate data:
            Inputs:
                url_b       : Basic url to do the request
                url_add     : Dictionary with the additional to the bassic url to perform the addecuate request
                psw         : String withe the required password to get the data

            Output:
                resp_json        : Json file with the information requested
        
        """
        token = requests.get(url=url_b+url_add["group_id"]+psw["group_id"])
        token = token.json()
        resp_json = requests.get(url=url_b+url_add["token"]+token["token"])
        return resp_json.json()
