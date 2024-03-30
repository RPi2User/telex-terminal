import os
import twCli
import twTTY

c: twCli.cli = twCli.cli()
t: twTTY.tty = twTTY.tty()

class parser():

    def parse(self, _in: str ) -> str:
        _out: str = ""
        _prompt: str = "/"
        match _in.upper():          # Quick and dirty hack!
            case '?': t._write(c.help())
            case 'HELP': t._write(c.help())
            case 'USE': t._write(c.usage())
            case 'USAGE': t._write(c.usage())
            case 'DATE': t._write(c.date())
            case 'BYE': c.exit()
            case 'DEBUG': t._write(c.debug(), single_slash=True)
            case 'CLEAR': t._write("\n\n\n\n\n\n\n\n\n")
            case 'CLS': t._write("\n\n\n\n\n\n\n\n\n")
            case 'CAL': t._write(c.cal())
            case 'CALENDAR' : t._write(c.cal())
            case 'W': t._write(c.w())
            case 'PS': t._write(c.psa())
            case 'UNAME': t._write(c.uname())
            case 'SSH': c.ssh()
            case 'LCL': c.local()
            case 'LOCAL': c.local()
            case '': pass
            
            case other: t._write("CNF: '" + _in + "' TRY 'HELP'")
            
        if _out != "" : t._write(_out)
        t.prompt(_prompt)
    
    def __init__(self) -> None:
        pass