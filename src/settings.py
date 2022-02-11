import os


BASE_DIR = os.getcwd()

database = os.path.join(BASE_DIR, 'database')

datalist = os.listdir(database)
