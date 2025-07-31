class NPC:
    __id: int
    __gen: int
    __name: str

    def __init__(self, name:str = ''):
        self.__id = 0
        self.__gen = 0
        self.__name = name
    
    def __eq__(self, value):
        if not isinstance(value, NPC):
            return False
        
        return self.__id == value.__id
    
    def __hash__(self):
        return self.__id
    
    def __repr__(self):
        return f'NPC({self.__id}, {self.__name if self.__name != '' else 'nobody'}, g {self.__gen})'
    
    def get_gen(self):
        return self.__gen
    
    def set_gen(self, gen: int):
        self.__gen = gen
    
    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        self.__id = id
    
    def get_name(self) -> str:
        return self.__name