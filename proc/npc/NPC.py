class NPC:
    __name: str
    __gender: str
    __id: str

    def __init__(self, id: str, gender: str, name: str):
        self.__id = id
        self.__gender = gender
        self.__name = name

    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> str:
        return self.__id
