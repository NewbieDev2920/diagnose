#!/usr/bin/python3

import json
from datetime import datetime
from models.Medic import Medic
from utils.idGenerator import new_id
from database.CrudOp import MedicCrudOp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
medic_crud_op = MedicCrudOp(app,db)

on = True

def readf(path : str) -> str:
    f_data = None
    with open(path) as f:
        f_data = f.read()
        f.close()
    return f_data

def exit() -> None:
    global on
    on = False

def help_commands() -> None:

    print('### HELP SECTION #################\n')
    for k,v in descriptions.items():
        print(k + ' - ' + v + '\n')
    print('##################################')

def new_medic() -> None:
    print('### NEW MEDIC ####################\n')

    i_id = new_id()
    
    i_fullname = input('Fullname : ')
    print('\n')
    
    i_email = input('Email : ')
    print('\n')
    
    i_cellphone = input('Cellphone : ')
    print('\n')

    i_user = input('User : ')
    print('\n')

    i_password = input('Password : ')
    print('\n')

    i_register_date = datetime.now()
    print('\n')
    
    print('##################################')

    medic = Medic(id = i_id, fullname = i_fullname, email = i_email, cellphone = i_cellphone,
                   user = i_user, password = i_password,register_date = i_register_date)
    
    MedicCrudOp.create_medic(medic)

def search_medic() -> None:
    print('### SEARCH MEDIC ####################\n')

    print('select query method \n  1. ID \n  2. FULLNAME')

    incorrect_input : bool = True
    while incorrect_input:
        query_method : str = input('$ > ')
        if query_method == '1' or query_method == '2':
            incorrect_input = False
        else:
            print('Incorrect input, select 1 or 2')

    if query_method == '1':

        print('Introduce the id')

        entry = input('$ > ')

        entry_argument = entry.rsplit()

        if entry_argument[0] == '/file':
            path = entry_argument[1]
            medic = medic_crud_op.get_medic(readf(path))
            print(medic)
        else:
            medic = medic_crud_op.get_medic(entry)
            print(medic)
    else:
        pass

    print('#####################################')
    
def debug_list_all_medics() -> None:
    print(MedicCrudOp.debug_get_all_medic())
  
commands = {
    "exit" : exit,
    "help" : help_commands,
    "new medic" : new_medic,
    "search medic" : search_medic,
    "list medic" : debug_list_all_medics
}

descriptions_f = open('utils/descriptions.json','r')
descriptions = json.load(descriptions_f)
descriptions_f.close()


print('###---%%%---###--- (DIAGNOSE ADMIN) ---###---%%%---###')

while on:

    print('enter a command \n')
    userinput = input('$ > ')

    if userinput in commands.keys():
        commands[userinput]()
    else:
        print('The command does not exists.\n')
        
    
    
    
        
         

        
