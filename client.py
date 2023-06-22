from typing import Union 
from modules import Program

error_type: type = Union[None, dict[any]]

class Client:
    def __init__(self, process: str) -> error_type:
        self.process: str = process
        
        is_running: bool = Program.is_running(task_name=process)
        
        print(is_running)

if __name__ == "__main__":
    Client_Instance: object = Client(process="Spotify.exe")