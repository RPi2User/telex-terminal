import twBuffer
import txDevED1000SC as ed1000
import twTTY_DEBUG
import time
import re

_tty: ed1000.TelexED1000SC = ed1000.TelexED1000SC()
#_tty: twTTY_DEBUG.tty_debug = twTTY_DEBUG.tty_debug()

lut: dict[str, str] = {
    '\n': '\r\n',
    '!': '/?',
    '"': "'",
    '$': '/us',
    '%': '/pc',
    '&': '/)',
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
        out = _in.replace('/', '//')
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

    def _write(self, single_slash: bool = False) -> None:
        if twBuffer._tx != "":
            print("[tx] " + twBuffer._tx)                   # DEBUG Purpose
            twBuffer._tx += twBuffer._trailer               # Append trailer, maybe a cr-lf is mandatory!
            twBuffer._tx = self._write_conv(twBuffer._tx)   # Convert via LUT
            if single_slash: 
                twBuffer._tx = twBuffer._tx.replace('//', '/')  # Slash Conversion
            for c in twBuffer._tx:                          # Write char for char to Hardware
                _tty.write(c, "a")
        twBuffer._tx = ""                                   # Clear buffer
        
    
    def _read(self) -> None:
        twBuffer._rx = ""
        while True:
            try:
                time.sleep(.25)
                twBuffer._rx += _tty.read()
            except:
                pass
            if 'err' in twBuffer._rx.lower():
                twBuffer._rx = ""
                twBuffer._tx += "\r\n"
            if '\n' in twBuffer._rx:
                break
            time.sleep(.2)
        twBuffer._rx = twBuffer._rx.replace("\r", "") \
                                    .replace("\n", "") \
                                    .replace(">", "") \
                                    .replace("<", "")
        twBuffer._rx = self._read_conv(twBuffer._rx)
        

    def prompt(self, _in: str) -> None: # Is this needed?
        _tty.write('\r', "a")
        _tty.write('\n', "a")
        for c in _in:
            _tty.write(c, "a")
        
    def init(self) -> None:
        _tty._check_commands('\x1bA')   # Establish Connection to TTY
        time.sleep(.1)                  # Wait
        twBuffer._tx += "CRT0 READY\r\n"    # Append CRT0 READY
        self.prompt("/")


    def exit(self) -> None:
        twBuffer._tx = "BYE"
        self._write()
        time.sleep(.5)
        _tty._check_commands('\x1bZ')
        _tty.exit()
        exit(0)
