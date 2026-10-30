import sys
from pathlib import Path
from colorama import Fore, Style


# recursively prints folder structure: folders in green, files in blue
def draw_tree(path, level=0):
   
    path = Path(path)
    if path.is_dir() and path.exists() and level == 0:
        print(Fore.GREEN + path.name + "/" +  Style.RESET_ALL)
        level+=1


    try:
        for el in path.iterdir():
            if el.is_dir():
                print("   " * level + Fore.GREEN + el.name + "/" +  Style.RESET_ALL)
                draw_tree(el, level+1)
            else:
                print("   " * level + Fore.BLUE + el.name +  Style.RESET_ALL)

    except NotADirectoryError:
        print(f"{path} is not a directory")
    except FileNotFoundError:
        print(f"{path} not found")



        
if __name__ == "__main__":
    try:
        draw_tree(sys.argv[1])
    except IndexError:
        print("please write python task3.py and path to desired directory!")