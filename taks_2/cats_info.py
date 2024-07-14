from file_reader import file_reader


def get_cats_info(path: str) -> list[dict]:
    file_rows = file_reader.read_file(path)
    cats_info = []

    for row in file_rows:
        splitted_row = row.split(',')

        # check if row format is correct
        if len(splitted_row) != 3:
            print(f"Invalid row format {splitted_row}")

            return []

        cats_info.append(create_cat_item(splitted_row))

    return cats_info


def create_cat_item(cat_info: list[str]) -> dict:
    return {
        "id": cat_info[0],
        "name": cat_info[1],
        "age": cat_info[2].strip()
    }
