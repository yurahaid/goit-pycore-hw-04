def read_file(path: str) -> list[str]:
    """Read file and handle any errors"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as err:
        print(f"Can`t read file {path}, error: {err}")

        return []