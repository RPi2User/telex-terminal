import twParser
import twTTY

p: twParser.parser = twParser.parser()
tty: twTTY.tty = twTTY.tty()


def main():
    tty.init()
    while True:
        p.parse(tty._read(err_prompt="/"))

if __name__== "__main__":
    main()
