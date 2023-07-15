from package.services.base_service import *
from package.services.database import crud
from package.services.database.models import Process
from package.services.tasks.invoices_process import execute_process

@service_handler
def get_processes():
    return crud.get_processes()

@service_handler
def get_process(id:int):
    return crud.get_process(id)

@service_handler
def start_process(process_key:str, params:dict):
    process = Process() 
    process.process_key = process_key
    process = crud.save_process(process)
    execute_process(process, params)
