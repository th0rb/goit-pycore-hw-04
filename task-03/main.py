import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def display_tree(directory_path: str, margin=0):
    directory = Path(directory_path)

    if not directory.is_dir():
        print (Fore.RED + f"Директорія не існує або не є директорією: {directory_path}")
        return 
    
    for item in directory.iterdir():
        if item.is_dir():
            print(" " * (margin + 2) + Fore.YELLOW + f"📂 {item.name}/")
            display_tree(item, margin + 4)

        elif item.is_file():
            print(" " * (margin + 2) + Fore.BLUE + f"📄 {item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати лише один аргумент - шлях до директорії.")
        sys.exit(1)
    
    path = sys.argv[1]
    display_tree(path)