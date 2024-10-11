from services.files import FileUtilities
from services.results import DefinitionEntryResult
from typing import List

class DefinitionParser:

    def __init__(self, definition_file: str):
        self.__definition_file = definition_file

    @property
    def definition_file(self):
        return self.__definition_file
    

    def parse(self) -> List[DefinitionEntryResult]:
        
        result:List[DefinitionEntryResult] = []

        #read the file
        entries = FileUtilities().read_character_file(self.definition_file)

        for entry in entries:
            result.append(DefinitionEntryResult(entry))

        return result
