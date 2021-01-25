import argparse
import os
import platform

def read_json(fullpath):
    """
        @Alex
        function that read a json file
            Input: 
                fullpath    : Full path of the file
            Output:
                json_readed : Jason readed

    """
    import json
    
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)

    return json_readed

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--j", type=int, help="the code", required=True)

args = vars(parser.parse_args())
if platform.system() == "Windows":
    os.system('cls')
elif platform.system() == "Darwin":
    os.system('clear')

print("####################\n")
code = args["j"]

if code == 18:
    fileDir =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname( __file__ )))) + os.sep + "reports"  + os.sep + "json_own.json"
    json_own = read_json(fileDir)
    print(json_own)
else:
    print("Error")
