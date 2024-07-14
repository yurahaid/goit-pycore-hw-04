import sys
from pathlib import Path
from colorama import Fore

from task_3.dir_dumper import dump_dir


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "invalid input, provide directory name as first argument")
        exit(1)

    path = sys.argv[1]
    try:
        path_to_dir = Path(path)
        if not path_to_dir.is_dir():
            print(Fore.RED + "invalid input, provide directory name as first argument")
            exit(1)
    except Exception as err:
        print(Fore.RED + f"invalid input, provide directory name as first argument, error {err}")
        exit(1)

    dump_dir(Path(path))


if __name__ == '__main__':
    main()
