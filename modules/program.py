import psutil

class Program:
    def is_running(task_name: str) -> bool:
        """Check if a program is running and return True/False.

        Args:
            task_name (str): The name the program should be running as.

        Returns:
            bool: If program is running or not
        """
        
        for program in psutil.process_iter():
            print(program.name())