from file_reader import file_reader

def total_salary(path: str) -> tuple:
    file_rows = file_reader.read_file(path)


    total = calc_total(file_rows)

    avg_salary = 0
    if len(file_rows) > 0:
        avg_salary = total/len(file_rows)

    return total, avg_salary

def calc_total(file_rows: list[str]) -> int:
    total = 0

    for row in file_rows:
        splitted_row = row.split(',')
        # check if row format is correct
        if len(splitted_row) != 2:
            print(f"Invalid row format, row should contains employee name and salary splitted by coma")
            return 0

        total += int(splitted_row[1])

    return total