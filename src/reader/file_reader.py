import re
from pathlib import PurePosixPath

class ZipContext:
    def __init__(self, zip_file):
        self.zip_file = zip_file
        self.files = zip_file.namelist()

        self._names = [PurePosixPath(f).name for f in self.files]

    def exists(self, filename):
        return any(PurePosixPath(f).name == filename for f in self.files)
    
    def exists_dir(self, dirname):
        dirname = dirname.rstrip("/") + "/"
        return any(dirname in f for f in self.files)

    def exists_pattern(self, pattern):
        regex = re.compile(pattern)
        return any(regex.match(name) for name in self._names)
    
    def open(self, filename):
        for f in self.files:
            if PurePosixPath(f).name == filename:
                return self.zip_file.open(f)
        return None