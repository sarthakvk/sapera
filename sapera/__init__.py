import os
import sys

from .main import main


def entry_point():
    """Entry point for the application
        activate by command sapera in terminal
    """
    args = sys.argv[1:]
    if os.name == 'nt':#for windows
        os.system('cls')
    else:#linux or mac
        os.system('clear')
    print("Hello There!")
    print(
        "I'm currently in devlopment, you can help me develop faster by contributing :)"
    )
    print("visit: https://github.com/sarthakchaudhary13/sapera")
    print()
    print("Meanwhile here's a algorithm you can learn today")
    print("-" * 25)
    data = main.random_generator()
    print("Name :" + data["name"])
    print("Algorithm Type: " + data["algo_type"])
    print("Link to the Solution: " + data["link"])
