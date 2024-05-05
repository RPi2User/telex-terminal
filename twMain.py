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
        if twTTY._rx_buffer == "":
            tty._write()
            tty._read()
            print("[RX-CLS] " + twTTY._rx_buffer)
        else:
            print("[PARSING] " + twTTY._rx_buffer)
            p.parse(twTTY._rx_buffer)
            twTTY._rx_buffer = "" # WIP for DEBUG purposes


if __name__== "__main__":
    main()
