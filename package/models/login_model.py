import os
import json
import package.local_storage as storage

USER_NAME_KEY = "kasa_desktop-user-name"
USER_TOKEN_KEY = "kasa_desktop-user-token"

class Login:
    def __init__(self):
        self.load_user_name()
        self.load_user_token()
        
    def save(self):
        storage.app_data[USER_NAME_KEY] = self.user_name
        storage.app_data[USER_TOKEN_KEY] = self.user_token
        storage.save_to_file()
    
    def load_user_name(self):
        self.user_name = storage.app_data.get(USER_NAME_KEY)
        print(f"Load user name from file: {self.user_name}")
    
    def load_user_token(self):
        self.user_token = storage.app_data.get(USER_TOKEN_KEY) 
        print(f"Load user name from file: [SUPRESS]")
            
    def set(self, user_name, token):
        self.user_name = user_name 
        self.user_token = token        
        
        