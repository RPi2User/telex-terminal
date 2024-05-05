import os
import twCli
import twTTY
import twBuffer

c: twCli.cli = twCli.cli()
t: twTTY.tty = twTTY.tty()

class parser():

    def parse(self, _in: str ) -> str:
        _out: str = ""
        _prompt: str = "/"
        match _in:
            case '?': twBuffer._tx += c.help("")
            case str(x) if 'help' in x: twBuffer._tx += c.help(_in)
            case 'use': twBuffer._tx += c.usage()
            case 'usage': twBuffer._tx += c.usage()
            case 'whoami': twBuffer._tx += c.whoami()
            case 'date': twBuffer._tx += c.date()
            case 'bye': c.exit()
            case 'debug': twBuffer._tx += c.debug()
            case 'clear': twBuffer._tx += "\n\n\n\n\n\n\n\n\n"
            case 'cls': twBuffer._tx += "\n\n\n\n\n\n\n\n\n"
            case 'cal': twBuffer._tx += c.cal()
            case 'calendar' : twBuffer._tx += c.cal()
            case 'w': twBuffer._tx += c.w()
            case 'ps': twBuffer._tx += c.psa()
            case 'uname': twBuffer._tx += c.uname()
            case 'ssh': c.local()
            case 'lcl': c.local()
            case 'local': c.local()
            case '': pass

            case other: twBuffer._tx += "CNF: '" + _in + "' TRY 'HELP'"
            
        if _out != "" : twBuffer._tx += _out
        t.prompt(_prompt)
    
    def __init__(self) -> None:
        pass