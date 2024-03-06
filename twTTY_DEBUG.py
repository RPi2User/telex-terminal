# DEBUG-Replacement for ed1000sc.py
class tty_debug:
    
    def write(self, _in: str, _arg: str | None) -> None:
        print(_in, end="")
        
    def read(self) -> str:
        return input() + "\n"
    
    def _check_commands(self, _in: str) -> None:
        print("[TTY_CMD] " + repr(_in))
        
    def exit(self) -> None:
        pass