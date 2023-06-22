from typing import Union 
from modules import Program

class Client:
    def __init__(self, process: str) -> None:
        self.process: str = process
        
        is_running: bool = Program.is_running(task_name=process)
        
        print(is_running)

if __name__ == "__main__":
    Client_Instance: object = Client(process="Spotify.exe")