import os
import twCli
import twTTY

c: twCli.cli = twCli.cli()
t: twTTY.tty = twTTY.tty()

class parser():

    def parse(self, _in: str ) -> str:
        _out: str = ""
        _prompt: str = "/"
        match _in:
            case '?': t._write(c.help(""))
            case str(x) if 'help' in x: t._write(c.help(_in), single_slash=True)
            case 'use': t._write(c.usage())
            case 'usage': t._write(c.usage())
            case 'whoami': t._write(c.whoami())
            case 'date': t._write(c.date())
            case 'bye': c.exit()
            case 'debug': t._write(c.debug(), single_slash=True)
            case 'clear': t._write("\n\n\n\n\n\n\n\n\n")
            case 'cls': t._write("\n\n\n\n\n\n\n\n\n")
            case 'cal': t._write(c.cal())
            case 'calendar' : t._write(c.cal())
            case 'w': t._write(c.w())
            case 'ps': t._write(c.psa())
            case 'uname': t._write(c.uname())
            case 'ssh': c.ssh()
            case 'lcl': c.ptyTest()
            case 'local': c.local()
            case '': pass

            case other: t._write("CNF: '" + _in + "' TRY 'HELP'")
            
        if _out != "" : t._write(_out)
        t.prompt(_prompt)
    
    def __init__(self) -> None:
        pass