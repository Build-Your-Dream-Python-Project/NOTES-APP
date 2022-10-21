import os
import datetime
import json


os.mkdir("Notes") if "Notes" not in os.listdir() else None
os.mkdir("Note Config") if "Note Config" not in os.listdir() else None

if "App Config.txt" not in os.listdir():
    file_config = open("App Config.txt","w+")
    file_config.write("1")
    file_config.close()

file_config = open("App Config.txt","r+")
count = int(file_config.read())
def read():
    _ = open("App Config.txt", "r+")
    _1 = _.read()
    _.close()
    return _1

def write(text):
    _ = open("App Config.txt", "r+")
    _.write(text)
    _.close()

def clear():
    _ = open("App Config.txt", "w+")
    _.close()

def config(note_id,**kwargs):
    print(note_id)
    __file_name = f"{os.getcwd()}/Note Config/{note_id}.json"
    __f =open(__file_name,"r+")
    data = json.load(__f)
    for i in kwargs:
        data[i] = kwargs[i]

    with open(__file_name, 'w') as outfile:
        outfile.write(str(data).replace("'", '"'))

def get_config(note_name):
    __file_name = f"{os.getcwd()}/Note Config/{[i for i in os.listdir(fr'{os.getcwd()}/Note Config') if i[:len(note_name)]== note_name][0]}"
    __f = open(__file_name, "r+")
    data = json.load(__f)
    __f.close()
    return data

def create_note(note_name):
    global count
    t = datetime.datetime.now()
    file_config.truncate(4)
    count += 1
    note_file = open(f"{os.getcwd()}/Notes/{f'{count:0>5}'}.txt","w+")
    config_file = open(f"{os.getcwd()}/Note Config/{f'{count:0>5}'}.json","w+")
    config_file.write("{}")
    note_file.close()
    config_file.close()
    write(f"{count:0>5}")
    config(f"{count:0>5}",id =f"{count:0>5}",name=note_name,created_at = [t.minute,t.hour,t.day,t.month,t.year])


