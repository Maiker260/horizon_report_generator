from pathlib import PurePosixPath

class ZipContext:
    def __init__(self, zip_file):
        self.zip_file = zip_file
        self.files = zip_file.namelist()

    def exists(self, filename):
        return any(PurePosixPath(f).name == filename for f in self.files)
    
    def open(self, filename):
        for f in self.files:
            if PurePosixPath(f).name == filename:
                return self.zip_file.open(f)
        return None