import twParser
import twTTY
import twBuffer
from time import sleep

p: twParser.parser = twParser.parser()
tty: twTTY.tty = twTTY.tty()


def main():
    tty.init()              # Establish Connection to Teletype
    while True:             # Main Loop
        sleep(0.5)          # Wait for Hardware to init / settle down
        twBuffer._trailer="/"   # Current trailer / prompt is "/"
        if twBuffer._rx == "":  # When nothing is received, write buffer
            tty._write()        # Write current buffer
            tty._read()         # read back from TTY
        else:
            print("[PARSING] " + twBuffer._rx)  # DEBUG
            p.parse(twBuffer._rx)               # Parse given input
            twBuffer._rx = "" # WIP for DEBUG purposes, clear input

if __name__== "__main__":
    main()
