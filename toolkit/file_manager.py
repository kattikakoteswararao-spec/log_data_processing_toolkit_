class FileManager:
    def __init__(self, file_path, mode="r"):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(
            self.file_path,
            self.mode,
            encoding="utf-8"
        )
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        print("File closed successfully")

        return False