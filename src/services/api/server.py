from flask import Flask, request, render_template
import os
import json

def def_camino(file_name):
    """
        @Alex
        Path definition for data folder to operate the path
            Input   : Name of the file to create the path
    """
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    camino = os.path.join(fileDir, './Covid_Group_Project_E/data/'+file_name)
    camino = os.path.abspath(os.path.realpath(camino))
    
    return camino

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    return "Welcome to Group E server"

@app.route('/group_id', methods=['GET']) #This one is the is to get the password
def group_id():
    x = request.args['password'] #el password es N
    if x == "E80":
        return '{"token":"E107750842"}' #El contenido es "S"
    else:
        return "No es el identificador correcto"

@app.route('/token_id', methods=['GET']) #This one is the is to get the password, so we need to put here
def token_id():
    x = request.args['password'] #el password es N
    path = def_camino("json_own.json")
    print(path)
    json_own = read_json(path)
    if x == "E107750842":
        return json_own #El contenido es "S"
    else:
        return "No es el identificador correcto"

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    print("SERVER_RUNNING", SERVER_RUNNING)
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")

if __name__ == "__main__":
    main()