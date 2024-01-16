import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
dict_file = []

def task() -> None:
    with open(INPUT_FILENAME, "r") as file1:
        data = csv.DictReader(file1)
        for row in data:
            dict_file.append(row)

    with open(OUTPUT_FILENAME, "w") as file2:
        file2.write(json.dumps(dict_file, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
