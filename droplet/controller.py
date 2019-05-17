from .utilities import Directories


class Divide(Directories):
    def __init__(self, path):
        super().__init__(path)
        directories = self.traverse_directories()
        for i in directories:
            Directories.determine_format(i)
