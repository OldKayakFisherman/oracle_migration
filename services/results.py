class DefinitionEntryResult:

    def __init__(self, line_entry):
        self.__line_entry: str = line_entry
        self.__column_name: str = None
        self.__nullable:bool = True
        self.__data_type: str = None
        self.parse()

    @property
    def column_name(self) -> str:
        return self.__column_name
    
    @property
    def nullable(self) -> bool:
        return self.__nullable
    
    @property
    def data_type(self) -> str:
        return self.__data_type

    def parse(self):
        
        self.__column_name = self.__line_entry.split(" ")[0]
        self.__nullable = (self.__line_entry.find("NOT NULL") == -1)
        self.__data_type = self.translate_data_type(self.__line_entry)    



    def translate_data_type(self, value: str):

        result = "str"

        if value.lower().find("number") > -1:
            result = "int"
        
        if value.lower().find("date") > -1:
            result = "datetime"

        return result


