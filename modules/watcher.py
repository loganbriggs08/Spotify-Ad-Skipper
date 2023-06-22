import os
import time
import pygetwindow

from modules import Program, Logging

class Watcher:
    def start(self) -> None:
        """Start watching for advertisements to close and then reopen spotify."""
        
        while True:
            for window in pygetwindow.getAllWindows():
                if window.title == "Advertisement":
                    if Program.is_running("Spotify.exe") == True:
                        Logging.success("Spotify.exe Process found with running AD..")
                        
                        if Program.kill("Spotify.exe") == True:
                            Logging.success("Spotify.exe process has been killed successfully."); os.system('cmd /k "spotify.exe"')
                        else:
                            Logging.error("Failed to kill Spotify.exe process..")

                time.sleep(0.5)