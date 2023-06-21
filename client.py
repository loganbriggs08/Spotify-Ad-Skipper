from modules import Program

class Client:
    def __init__(self):
        Program.is_running("Spotify.exe")
    
if __name__ == "__main__":
    Client_Instance: object = Client()