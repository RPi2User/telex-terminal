import os
import subprocess
#import twSSH
import twTTY

tty = twTTY.tty()

class cli:
    
    def debug(self) -> None:
        print(self.cmd("ps", "-a", "-u", "-x"))

    def __init__(self) -> None:
        pass

    def cmd(*_cmd) -> str:
        return str(subprocess.check_output(*_cmd, universal_newlines=True))
    
    def w(self) -> str:
        print(self.cmd("ps", "-a", "-u", "-x"))
        return str(subprocess.check_output("w", universal_newlines=True))
    
    def psa(self) -> str:
        return str(subprocess.check_output(["ps", "-a"], universal_newlines=True))
    
    def date(self) -> str:
        return str(subprocess.check_output("date", universal_newlines=True))
    
    def cal(self) -> str:
        return str(subprocess.check_output(["ncal", "-w", "-b", "-h"], universal_newlines=True))
    
    def uname(self) -> str:
        return str(subprocess.check_output(["uname", "-a"], universal_newlines=True))
    
#    def ssh(self, _host: str, _user: str, _pass: str, local: bool | None) -> None:
#        twSSH.init(_host, _user, _pass)
#        _prompt: str = ""
#        while True:
#            if local:
#                _prompt = ".lcl:/ "
#            else:
#                _prompt = _user + "." + _host + ":/ "
#            tty.prompt(_in=_prompt)
#            _cmd: str = tty._read(err_prompt=_prompt)
#            if 'exit' in _cmd.lower():
#                twSSH.exit()
#                breakutilities
        self.ssh(_host="localhost", _user="telex", _pass="telex", local=True)
    
    def debug(self) -> str:
        return """
  `.::///+:/-.        --///+//-:``    florian@FLORIAN-MAIN 
 `+oooooooooooo:   `+oooooooooooo:    -------------------- 
  /oooo++//ooooo:  ooooo+//+ooooo.    OS: openSUSE Tumbleweed x86_64 
  `+ooooooo:-:oo-  +o+::/ooooooo:     Host: MS-7B79 2.0 
   `:oooooooo+``    `.oooooooo+-      Kernel: 6.7.5-1-default 
     `:++ooo/.        :+ooo+/.`       Uptime: 4 hours, 42 mins 
        ...`  `.----.` ``..           Packages: 3354 (rpm), 18 (flatpak) 
     .::::-``:::::::::.`-:::-`        Shell: bash 5.2.26 
    -:::-`   .:::::::-`  `-:::-       Resolution: 1920x1200, 1920x1200, 1920x1200 
   `::.  `.--.`  `` `.---.``.::`      DE: Cinnamon 6.0.0 
       .::::::::`  -::::::::` `       WM: Mutter (Muffin) 
 .::` .:::::::::- `::::::::::``::.    WM Theme: Linux Mint (Menta) 
-:::` ::::::::::.  ::::::::::.`:::-   Theme: Menta [GTK2/3] 
::::  -::::::::.   `-::::::::  ::::   Icons: Adwaita [GTK2/3] 
-::-   .-:::-.``....``.-::-.   -::-   Terminal: gnome-terminal 
 .. ``       .::::::::.     `..`..    CPU: AMD Ryzen 7 3700X (16) @ 3.600GHz 
   -:::-`   -::::::::::`  .:::::`     GPU: NVIDIA GeForce RTX 2070 SUPER 
   :::::::` -::::::::::` :::::::.     Memory: 8385MiB / 32029MiB 
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

    def help(_helppage: str) -> str:
        try:
            _page: str = _helppage.split(' ')[1]
        except:
            pass
        match _helppage:
            case "help": return "help"
            case "short": return "help-short"
            case "lan": return "lan"
            case "wlan": return "wlan"
            case "misc": return "misc"
            case "seq": return "sequences"
        return """
SHORT   : LONG          : DESCRIPTION
--------:---------------:-----------------------------------------
?       : HELP          : SHOWES THIS HELP FILE
USE     : USAGE         : PRINT SMALL HELP FILE
DATE    : ------------- : PRINT DATE / TIME
CAL     : CALENDAR      : SHOW SYSTEM CALENDAR
IP      : IPCONFIG      : SHOW CURRENT SYSTEM IP CONFIGURATION
NETC    : NETWORKCONFIG : START NETWORK CONFIGURATION WIZARD
ERR     : ERROR         : DISCARD CURRENT CMD / BACK TO PROMPT
ECHO    : ------------- : ECHOES CURRENT LINE
BYE     : ------------- : SYSTEM SHUTDOWN"""

cli.debug(cli)