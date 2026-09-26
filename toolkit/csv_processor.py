import csv


def read_csv(file_path: str) -> list[dict]:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)