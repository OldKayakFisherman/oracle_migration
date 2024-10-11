import os
from pathlib import Path

class PathResolver:

    def get_current_dir(self, source):
        return os.path.dirname(os.path.realpath(source))

    def get_parent_dir(self, source):
        return Path(os.path.dirname(os.path.realpath(source))).parent
    

class FileUtilities:

    def read_binary_file(self, path):
        
        result = None

        with open(path, 'rb') as f:
            result = f.readlines()

        return result

    def read_character_file(self, path):
        
        result = None

        with open(path, 'r') as f:
            result = f.readlines()

        return result

    def does_file_exist(self, file) -> bool:
        return os.path.exists(file)
    
    def delete_file(self, file) -> None:
        if self.does_file_exist(file):
            os.remove(file)
