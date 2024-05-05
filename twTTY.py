import txDevED1000SC as ed1000
import twTTY_DEBUG
import time
import re

_tty: ed1000.TelexED1000SC = ed1000.TelexED1000SC()
#_tty: twTTY_DEBUG.tty_debug = twTTY_DEBUG.tty_debug()

_rx_buffer: str = ""
_tx_buffer: str = ""
_current_trailer: str = ""

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
        print("[tx] " + _tx_buffer)
        if _tx_buffer != "":
            _tx_buffer += _current_trailer
            _tx_buffer = self._write_conv(_tx_buffer)
            if single_slash: 
                _tx_buffer = _tx_buffer.replace('//', '/')
            for c in _tx_buffer:
                _tty.write(c, "a")
        _tx_buffer = ""
        
    
    def _read(self) -> None:
        _rx_buffer: str = ""
        while True:
            try:
                time.sleep(.25)
                _rx_buffer += _tty.read()
            except:
                pass
            if 'err' in _rx_buffer.lower():
                _rx_buffer = ""
                _tx_buffer += "\r\n"
            if '\n' in _rx_buffer:
                break
            time.sleep(.2)
        _rx_buffer = _rx_buffer.replace("\r", "") \
                                .replace("\n", "") \
                                .replace(">", "") \
                                .replace("<", "")
        _rx_buffer = self._read_conv(_rx_buffer)
        print("[rx] " + _rx_buffer)

    def prompt(self, _in: str) -> None:
        _tty.write('\r', "a")
        _tty.write('\n', "a")
        for c in _in:
            _tty.write(c, "a")
        
    def init(self) -> None:
        _tty._check_commands('\x1bA')
        time.sleep(.1)
        _tx_buffer = "CRT0 READY"
        self._write()
        self.prompt("/")


    def exit(self) -> None:
        _tx_buffer = "BYE"
        self._write()
        time.sleep(.5)
        _tty._check_commands('\x1bZ')
        _tty.exit()
        exit(0)
