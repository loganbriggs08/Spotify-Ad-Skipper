import time
import pygetwindow

from modules import Program

class Watcher:
    def start(self) -> None:
        """Start watching for advertisements to close and then reopen spotify."""
        
        while True:
            for window in pygetwindow.getAllWindows():
                if window.title == "Advertisement":
                    print("ad is running?")
                
                time.sleep(1)