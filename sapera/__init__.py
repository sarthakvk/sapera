import os
import sys

from .main import main


def entry_point():
    """Entry point for the application
        activate by command sapera in terminal
    """
    args = sys.argv[1:]  # todo add [options]
    if os.name == "nt":  # for windows
        os.system("cls")

    else:  # linux or mac
        os.system("clear")

    if len(args) == 1:
        if args[0] in ("run", "r"):
            print("Here's an Algorithm of the Day")
            print("-" * 30)
            data = main.random_generator()
            print("Name :" + data["name"])
            print("Algorithm Type: " + data["algo_type"])
            print("Link to the Solution: " + data["link"])

        elif args[0] in ("update", "u"):
            print("Running Script...")
            main.update_data_info()

        elif args[0] in ("help", "h"):
            print("Usage:")
            print("\tsapera <command>\n")
            print("Commands:")
            print("\trun\t\t->\tRun sapera")
            print("\tr\t\t->\talias for run")
            print("\tupdate\t\t->\tupdate sapera")
            print("\tu\t\t->\talias for update")
            print("\tupdate run\t->\tupdate the database then run")
            print("\tu r\t\t->\talias for update run")
            print("\thelp\t\t->\topens help")
            print("\th\t\t->\talias for help")

        else:
            print('sapera: unknown command "', *args, '"')
            print("see: 'sapera help' or 'sapera h'.")

    elif len(args) == 2:
        if (args[0] in ("update", "u") and args[1] in ("run", "r")) or (
                args[0] in ("run", "r") and args[1] in ("update", "u")):
            print("Running Script...")
            main.update_data_info()
            print("Here's an Algorithm of the Day")
            print("-" * 30)
            data = main.random_generator()
            print("Name :" + data["name"])
            print("Algorithm Type: " + data["algo_type"])
            print("Link to the Solution: " + data["link"])

        else:
            print('sapera: unknown command "', *args, '"')
            print("see: 'sapera help' or 'sapera h'.")

    elif len(args) == 0:
        print("Usage:")
        print("\tsapera <command>\n")
        print("Commands:")
        print("\trun\t\t->\tRun sapera")
        print("\tr\t\t->\talias for run")
        print("\tupdate\t\t->\tupdate sapera")
        print("\tu\t\t->\talias for update")
        print("\tupdate run\t->\tupdate the database then run")
        print("\tu r\t\t->\talias for update run")
        print("\thelp\t\t->\topens help")
        print("\th\t\t->\talias for help")
    else:
        print('sapera: unknown command "', *args, '"')
        print("see: 'sapera help' or 'sapera h'.")
