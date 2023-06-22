from typing import Union 
from modules import Program, Logging

class Client:
    def __init__(self, process: str) -> None:
        self.process: str = process
        
        is_running: bool = Program.is_running(task_name=process)
        
        if is_running == True:
            program_object: object = Program.information(task_name=process)
            
            if program_object == None:
                Logging.error(f"{process} couldn't be found in the process list..")
            else:
                Logging.success(f"{program_object.name()} has been found sucessfully..")
        else:
            Logging.error(f"{process} couldn't be found in the process list..")

if __name__ == "__main__":
    Client_Instance: object = Client(process="Spotify.exe")