#import txDevED1000SC as ed1000
import twTTY_DEBUG
import time
import re

# _tty: ed1000.TelexED1000SC = ed1000.TelexED1000SC()
_tty: twTTY_DEBUG.tty_debug = twTTY_DEBUG.tty_debug()

lut: dict[str, str] = {
    '\n': '\r\n',
    '!': '/?',
    '"': "'",
    '$': '/4',
    '%': '/5',
    '&': '/6',
    '*': '/+',
    '|': '/:',
    ';': '/,',
    '<': '/lt',
    '>': '/gt',
    '_': '/-',
    '`': "'",
    '´': "'",
    '#': '/ht',
    '@': '/at',
    'Ä': 'AE',
    'Ö': 'OE',
    'Ü': 'UE',
    'ä': 'ae',
    'ö': 'oe',
    'ü': 'ue'
}

class tty():

    
    def _write_conv(self, _in: str) -> str:
        out = _in.upper()
        for key, value in lut.items():
            out: str = out.replace(key, value)
        return out

    def _read_conv(self, _in: str) -> str:
        out: str = _in.lower()
        for key, value in lut.items():
            out = out.replace(value, key)
        out = self._read_conv_slashPBE(out)
        return out
    
    def _read_conv_slashPBE(self, _in: str) -> str:
        s: str = _in.lower()

        matches = list(re.finditer(r'\/[a-z]', s))[::-1]
        for match in matches:
            i=match.span()[0]
            checki = s[i-1] != "/"
            if checki:
                s = s[:i] + s[i+1].upper() + s[i+2:]
        s = s.replace("//", "/")

        matches = list(re.finditer(r'\/\/[a-z]', s))[::-1]
        for match in matches:
            slash = match.span()[0]
            capital = match.span()[1] -1
            s = s[:slash+1] + s[capital].upper() + s[capital + 1:]
        return s

    def _write(self, _out: str, single_slash: bool = False) -> None:
        _out = self._write_conv(_out)
        if single_slash: _out = _out.replace('//', '/')
        for c in _out:
            _tty.write(c, "a")
        
    
    def _read(self, err_prompt: str) -> str:
        _out: str = ""
        while True:
            try:
                _out += _tty.read()
            except:
                pass
            if 'err' in _out.lower():
                _out = ""
                self.prompt(err_prompt)
            if '\n' in _out.lower():
                break
            time.sleep(.2)
        _out = _out.replace("\r", "") \
                    .replace("\n", "") \
                    .replace(">", "") \
                    .replace("<", "")
        _out = self._read_conv(_out)
        return _out
        

    def prompt(self, _in: str) -> None:
        _tty.write('\r', "a")
        _tty.write('\n', "a")
        for c in _in:
            _tty.write(c, "a")
        
    def init(self) -> None:
        _tty._check_commands('\x1bA')
        time.sleep(.1)
        self._write("CRT0 READY")
        self.prompt("/")


    def exit(self) -> None:
        self._write("BYE")
        time.sleep(.5)
        _tty._check_commands('\x1bZ')
        _tty.exit()
        exit(0)