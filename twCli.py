import subprocess
import twSSH
import twTTY
import ptyprocess
import time

"""_summary_
Still a early version of the CLI. VERY WIP!
Returns:
    _type_: CLI of twTTY-Project WIP
"""

tty = twTTY.tty()

class cli:
    
    def debug(self) -> None:
        print(self.cmd("ps", "-a", "-u", "-x"))

    def __init__(self) -> None:
        pass

    def cmd(*_cmd) -> str: # Just for testing
        return str(subprocess.check_output(*_cmd, universal_newlines=True))
    
    def local(self) -> None:
        while True:
            tty._write("lcl:/ ", True)  # When local-mode is init. no prompt is given to inform the user
            p: subprocess = subprocess.Popen("bash", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True) #Init Thread for bash Early implementation!
            _read = tty._read("lcl:/ ") # Need Userinput to pass to bash through
            if _read() != "exit": # When Userinput = `exit` break loop
                tty_stdin: str = _read # Else pass userinput to bash
            else:
                break
            stdout, stderr = p.communicate(tty_stdin.lower()) # Get stdout / stderr
            tty._write(str(stdout + stderr)) # Append outputs and print them

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
    
    def ptyTest(self) -> None:
        pty_proc = ptyprocess.PtyProcessUnicode.spawn(['bash'])
        time.sleep(.5)
        tty._write(pty_proc.read(8192))
        _read: str = ""
        while(_read != "exit"):
            _read = tty._read("lcl:/ ")
            pty_proc.write(_read + "\n")
            time.sleep(.1)
            try: # Needed when first Command is "exit"
                _shell_read: str = pty_proc.read(8192)
            except:
                pass
            tty._write(_shell_read)



    def ssh(self, _host: str, _user: str, _pass: str, local: bool | None) -> None:
        twSSH.init(_host, _user, _pass)
        _prompt: str = ""
        while True:
            if local:
                _prompt = ".lcl:/ "
            else:
                _prompt = _user + "." + _host + ":/ "
            tty.prompt(_in=_prompt)
            _cmd: str = tty._read(err_prompt=_prompt)
            if 'exit' in _cmd.lower():
                twSSH.exit()
                break
        self.ssh(_host="localhost", _user="telex", _pass="telex", local=True)
    
    def debug(self) -> str:
        return """
         1         2         3         4         5         6            
123456789012345678901234567890123456789012345678901234567890123456789

  `.::///+:/-.        --///+//-:``  pi@raspberrypi 
 `+oooooooooooo:   `+oooooooooooo:  -------------- 
  /oooo++//ooooo:  ooooo+//+ooooo.  OS: Raspbian GNU/Linux 
  `+ooooooo:-:oo-  +o+::/ooooooo:      12 (bookworm) armv7l 
   `:oooooooo+``    `.oooooooo+-    Host: Raspberry Pi 2B   
     `:++ooo/.        :+ooo+/.`     Kernel: 6.1.0-rpi8-v7 
        ...`  `.----.` ``..         Uptime: 31 mins   
     .::::-``:::::::::.`-:::-`      Packages: 1072 (dpkg)   
    -:::-`   .:::::::-`  `-:::-     Shell: bash 5.2.15   
   `::.  `.--.`  `` `.---.``.::`    Terminal: /dev/pts/5
       .::::::::`  -::::::::` `     CPU: BCM2835 (4)@900MHz
 .::` .:::::::::- `::::::::::``::.  Memory: 544MiB / 921MiB 
-:::` ::::::::::.  ::::::::::.`:::-                           
::::  -::::::::.   `-::::::::  ::::                           
-::-   .-:::-.``....``.-::-.   -::-
 .. ``       .::::::::.     `..`..
   -:::-`   -::::::::::`  .:::::`
   :::::::` -::::::::::` :::::::.
   .:::::::  -::::::::. ::::::::
    `-:::::`   ..--.`   ::::::.
      `...`  `...--..`  `...`
            .::::::::::
             `.-::::-`

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