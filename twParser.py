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
            case '?': twTTY._tx_buffer += c.help("")
            case str(x) if 'help' in x: twTTY._tx_buffer += c.help(_in)
            case 'use': twTTY._tx_buffer += c.usage()
            case 'usage': twTTY._tx_buffer += c.usage()
            case 'whoami': twTTY._tx_buffer += c.whoami()
            case 'date': twTTY._tx_buffer += c.date()
            case 'bye': c.exit()
            case 'debug': twTTY._tx_buffer += c.debug()
            case 'clear': twTTY._tx_buffer += "\n\n\n\n\n\n\n\n\n"
            case 'cls': twTTY._tx_buffer += "\n\n\n\n\n\n\n\n\n"
            case 'cal': twTTY._tx_buffer += c.cal()
            case 'calendar' : twTTY._tx_buffer += c.cal()
            case 'w': twTTY._tx_buffer += c.w()
            case 'ps': twTTY._tx_buffer += c.psa()
            case 'uname': twTTY._tx_buffer += c.uname()
            case 'ssh': c.ssh()
            case 'lcl': c.local()
            case 'local': c.local()
            case '': pass

            case other: twTTY._tx_buffer += "CNF: '" + _in + "' TRY 'HELP'"
            
        if _out != "" : twTTY._tx_buffer += _out
        t.prompt(_prompt)
    
    def __init__(self) -> None:
        pass