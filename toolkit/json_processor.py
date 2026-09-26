import json


def read_json(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(file_path: str, data: list[dict]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        