class SimulationError(Exception):
    __message: str
    def __init__(self, message: str):
        self.__message = message
        super().__init__(message)
    
    def get_message(self) -> str:
        return self.__message