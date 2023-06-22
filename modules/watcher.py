import os
import time
import pyautogui
import pygetwindow

from modules import Program, Logging

class Watcher:
    def start() -> None:
        """Start watching for advertisements to close and then re-open spotify."""
        
        while True:
            for window in pygetwindow.getAllWindows():                
                if window.title == "Advertisement":
                    if Program.is_running("Spotify.exe") == True:
                        Logging.success("Spotify.exe Process found with running AD..")
                        
                        if Program.kill("Spotify.exe") == True:
                            Logging.success("Spotify.exe process has been killed successfully.")
                            try:
                                os.system('cmd /k "spotify.exe"'); pyautogui.press('playpause')
                                
                                Logging.success("Spotify.exe has been started again and is now playing..")
                            except:
                                Logging.error("Spotify.exe couldn't be started again..")
                        else:
                            Logging.error("Failed to kill Spotify.exe process..")
                            
            time.sleep(0.5)

