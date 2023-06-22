import pygetwindow

class Watcher:
    def __init__(self) -> None:
        for window in pygetwindow.getAllWindows():
            print(window.title())