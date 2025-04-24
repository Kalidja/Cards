from datetime import datetime
from pathlib import Path
class Logger:
    def __init__(self, game_name: str) -> None:
        self.game_name = game_name

    def open_logger(self):
        path = Path(
            __file__).resolve().parent / "GamesResults" / f"{self.game_name}_{datetime.now().strftime("%Y_%m_%dT%H_%M_%S_%f")}.txt"
        self._file = open(path, "w")

    def close_logger(self) -> None:
        if self._file:
            self._file.close()
        else:
            raise Exception("No file opened.")

    def log(self, value: str, empty_row: bool = False, level: int = 0) -> None:
        try:
            if empty_row:
                self._file.write("\n")
            self._file.write("  " * level + f"{value}\n")
        except Exception as e:
            print(e)
