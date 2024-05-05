import subprocess
import twTTY
import twBuffer
import ptyprocess
import time

"""_summary_
Still a early version of the CLI. VERY WIP!
Returns:
    _type_: CLI of twTTY-Project WIP
"""

tty = twTTY.tty()

class cli:

    _rx_buffer: str = ""
    _tx_buffer: str = ""


    def debug(self) -> None:
        print(self.cmd("ps", "-a", "-u", "-x"))

    def __init__(self) -> None:
        pass

    def cmd(*_cmd) -> str: # Just for testing
        return str(subprocess.check_output(*_cmd, universal_newlines=True))

    def w(self) -> str:
        #print(self.cmd("ps", "-a", "-u", "-x"))
        return str(subprocess.check_output("w", universal_newlines=True))
    
    def psa(self) -> str:
        return str(subprocess.check_output(["ps", "-a"], universal_newlines=True))
    
    def date(self) -> str:
        return str(subprocess.check_output("date", universal_newlines=True))
    
    def cal(self) -> str:
        return str(subprocess.check_output(["ncal", "-w", "-b", "-h"], universal_newlines=True))
    
    def whoami(self) -> str:
        return str(subprocess.check_output("whoami", universal_newlines=True))
    
    def uname(self) -> str:
        return str(subprocess.check_output(["uname", "-a"], universal_newlines=True))
    
    def local(self) -> None:
        pty_proc = ptyprocess.PtyProcessUnicode.spawn(['bash'])
        twTTY._current_trailer = ""
        time.sleep(.5)
        twBuffer._tx = pty_proc.read(8192)
        tty._write()
        _read: str = twBuffer._rx
        while(_read != "exit"):
            tty._write()
            tty._read()
            pty_proc.write(twBuffer._rx + "\n")
            time.sleep(.1)
            try: # Needed when first Command is "exit"
                twBuffer._tx = pty_proc.read(8192)
            except:
                pass


    
    def debug(self) -> str:
        return """
         1         2         3         4         5         6            
123456789012345678901234567890123456789012345678901234567890123456789

"""
    
    def exit(self) -> None:
        tty.exit()
    
    def usage(self) -> str: #TODO!
        return """
?, HELP: HELPFILE + USE, USAGE: SMALL HELP + DATE + CAL, CALENDAR +
IP, IPCONFIG + NETC, NETWORKCONFIG + ERR, ERROR + ECHO + BYE
"""

    def help(self, _helppage: str | None) -> str:
        try:
            _page: str = _helppage.split(' ')[1]
        except:
            _page = "long"
        match _page:
            case "help": return "help"
            case "short": return "help-short"
            case "lan": return "lan"
            case "wlan": return "wlan"
            case "misc": return "misc"
            case "seq": return "sequences"
            case "long": return """
SHORT   : LONG          : DESCRIPTION
--------:---------------:-----------------------------------------
?       : HELP          : SHOWES THIS HELP FILE
USE     : USAGE         : PRINT SMALL HELP FILE
WHOAMI  : ------------- : PRINT CURRENT USER
DATE    : ------------- : PRINT DATE / TIME
CAL     : CALENDAR      : SHOW SYSTEM CALENDAR
IP      : IPCONFIG      : SHOW CURRENT SYSTEM IP CONFIGURATION
NETC    : NETWORKCONFIG : START NETWORK CONFIGURATION WIZARD
ERR     : ERROR         : DISCARD CURRENT CMD / BACK TO PROMPT
ECHO    : ------------- : ECHOES CURRENT LINE
BYE     : ------------- : SYSTEM SHUTDOWN"""

cli.debug(cli)