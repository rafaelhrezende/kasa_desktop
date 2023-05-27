from package.services.base_service import *

def get_processes(token):
    return request_kasa_service(token, RequestMethods.GET, f'processes/')

def get_process(token, id:int):
    return request_kasa_service(token, RequestMethods.GET, f'processes/{id}')

def new_process(token, process_key:str, params:dict):
    body = {
        "process_key": process_key,
        "params":  [{'name': param, 'value': params[param]} for param in params] 
    }
    return request_kasa_service(token, RequestMethods.POST, f'processes/', body = body)
        