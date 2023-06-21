from typing import Union 
from modules import Program

error_type: type = Union[None, dict[any]]

class Client:
    def __init__(self, process: str) -> error_type:
        self.process: str = process
        
        Is_Running_Result: bool = Program.is_running(task_name=process)
        
        if Is_Running_Result == False:
            return {"error": f"{process} has to be open for this to work."}
        else:
            print("Spotify is running")

if __name__ == "__main__":
    Client_Instance: object = Client(process="Spotify.exe")
    
    if Client_Instance is not None:
        print(f"[ERROR] {Client_Instance}")