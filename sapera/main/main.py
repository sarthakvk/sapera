#main script for the application, Will change in future when structure of project become complex
import json
from sapera import BASE_DIR
import os


def update_data():
    os.system('bash {x}/sapera/scraper/updater.sh {x}'.format(x = BASE_DIR)) #calling the updater.sh

def load_data():
    pass