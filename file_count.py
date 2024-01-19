import json
from pathlib import Path


class FileCounter:
    def __init__(self, folder: str, show_result: bool = True):
        """
        Utility class for recursively counting files by folder and suffix.

        :param folder: Folder that the files are counted in.
        :param show_result: If True prints out the result, otherwise won't.
        """
        self._dir = Path(folder)
        self._show_result = show_result
        if not self._dir.exists():
            raise FileNotFoundError(f'Directory {self._dir} not Found.')
        if not self._dir.is_dir():
            raise NotADirectoryError(f'{self._dir} is not a Directory.')
        self.file_counts = {}

    def start_count(self) -> dict:
        """
        Counts the number of files in the specified folder by file extension.

        :return: Counted folders as a dictionary.
        """
        self._count_files(self._dir)
        if self._show_result:
            print(json.dumps(self.file_counts, indent=4))
        return self.file_counts

    def _count_files(self, folder: Path) -> None:
        """
        Recursively counts files in the specified folder and updates the file_counts dictionary.

        :param folder: The path of the current folder.
        :return: None
        """
        for path in folder.rglob('*'):
            if not path.is_file():
                continue
            current_dict = self.file_counts
            for folder in path.relative_to(self._dir).parts[:-1]:
                current_dict = current_dict.setdefault(folder, {})
            ext = path.suffix.lower()
            current_dict[ext] = current_dict.get(ext, 0) + 1
