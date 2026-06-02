import re
from pathlib import PurePosixPath

class ZipContext:
    def __init__(self, zip_file):
        self.zip_file = zip_file
        self.files = zip_file.namelist()

        self._names = [PurePosixPath(f).name for f in self.files]
        self._names_set = set(self._names)

        self._file_lookup = {
            PurePosixPath(f).name: f for f in self.files
        }

    def exists(self, filename):
        return filename in self._names_set
    
    def exists_dir(self, dirname):
        dirname = dirname.rstrip("/") + "/"
        return any(dirname in f for f in self.files)

    def exists_pattern(self, pattern):
        regex = re.compile(pattern)
        return any(regex.match(name) for name in self._names)
    
    def find_pattern(self, pattern):
        regex = re.compile(pattern)

        return [
            name for name in self._names if regex.match(name)
        ]
    
    def open(self, filename):
        full_path = self._file_lookup.get(filename)

        if full_path:
            return self.zip_file.open(full_path)

        return None