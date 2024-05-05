import twParser
import twTTY
from time import sleep

p: twParser.parser = twParser.parser()
tty: twTTY.tty = twTTY.tty()


def main():
    tty.init()
    while True:
        sleep(0.5)
        twTTY._current_trailer="/"
        twTTY._rx_buffer = tty._read()
        if twTTY._rx_buffer == "":
            tty._write()
        else:
            print("[PARSING] " + twTTY._rx_buffer)
            p.parse(twTTY._rx_buffer)


if __name__== "__main__":
    main()
