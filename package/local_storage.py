import os 
import json

DATA_FILE_PATH = "local_data"
DATA_FILE_NAME = "data.json"

app_data = {}

def initializing_app_data():
    if os.path.exists(DATA_FILE_PATH) == False:
        os.mkdir(DATA_FILE_PATH)
    load_app_data()

def app_data_file_path():
    return os.path.join(DATA_FILE_PATH, DATA_FILE_NAME)
    
def load_app_data():
    global app_data
    with open(app_data_file_path()) as file:
        app_data = json.loads(file.read())
        
def save_to_file():
    with open(app_data_file_path(), 'w+') as outfile:
        json.dump(app_data, outfile, indent=4)         
        