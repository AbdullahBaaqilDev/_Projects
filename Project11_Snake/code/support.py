from json import load, dump
from settings import *

def load_data():
    with open(f"{PROJECT_FOLDER}\\data\\data.json","r") as file:
        return load(file)

def dump_data(new_data):
    with open(f"{PROJECT_FOLDER}\\data\\data.json","w") as file:
        dump(new_data, file, indent = 4)