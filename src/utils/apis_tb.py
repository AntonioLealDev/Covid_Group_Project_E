# apis_tb.py 
# Creator: Alejandro Balseiro
# Last review: 22/01/2021 by Javier Olcoz


import pandas as pd
import numpy as np
import json
import requests

class Apis:

    def checker(self, url_complete):
        """
        @Alex
        Function that helps us to make the call to the server to recieve the appropiate data:
            Inputs:
                url_complete    : url to check

            Output:
                r               : response of the call, if the request, have succeded, it returns "True", if found an error, returns "False"
        
        """
    
        try:
            r = requests.get(url=url_complete)
            r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx, or timeout
        
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError):
            return False
        else:
            return True

    def conection_error(self):
        """
        @Alex
        Function that checks the so and return the last json given data:
            Output:
                resp_json        : Json file with the information requested
        
        """
        print("error in the response, proceed to open the newest copy of the file given")

        import os
        path = os.path.dirname(os.path.dirname(os.path.dirname( __file__ )))
        camino = path + os.sep + "data" + os.sep + "jsonpaalexjaviyantonio.json"

        with open(camino, 'r+') as outfile:
            resp_json = json.load(outfile)
        
        return resp_json

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
        url_complete = url_b+url_add["group_id"]+psw["group_id"]
        token = self.checker(url_complete)
        if token == True:
            token = requests.get(url=url_complete)
            token = token.json()
            url_complete = url_b+url_add["token"]+token["token"]
            resp_json = self.checker(url_complete)
            if resp_json == True:
                resp_json = requests.get(url=url_complete)
                resp_json = resp_json.json()
            else:
                resp_json = self.conection_error()
        else:
            resp_json = self.conection_error()
        
        return resp_json
