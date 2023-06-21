from modules import Program

class Client:
    def __init__(self, process: str):
        self.process: str = process
        
        Is_Running_Result: bool = Program.is_running(task_name=process)
        print(Is_Running_Result)

if __name__ == "__main__":
    Client_Instance: object = Client(process="Spotify.exe")