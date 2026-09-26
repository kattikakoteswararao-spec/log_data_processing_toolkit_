def read_txt(file_path: str) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def write_txt(file_path: str, lines: list[str]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
            