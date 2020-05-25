import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .main import main
def entry_point():
    """Entry point for the application
        activate by command sapera in terminal
    """
    args = sys.argv[1:]

    print("Hello There!")
    print("I'm currently in devlopment, you can help me develop faster by contributing :)")
    print("visit: https://github.com/sarthakchaudhary13/sapera")
    # main.update_data()