from pathlib import Path
from colorama import Fore
def dump_dir(dir: Path, level: int = 0):
    # print dir
    print(Fore.BLUE + generate_space(level) + dir.name)
    level += 1

    for path in dir.iterdir():
        if path.is_file():
            # print file
            print(Fore.GREEN + generate_space(level) + path.name)
            continue

        if path.is_dir():
            # recursive traversal of nested directories
            dump_dir(path, level)

def generate_space(level: int) -> str:
    return level * 2 * " "

