import twParser
import twTTY

p: twParser.parser = twParser.parser()
tty: twTTY.tty = twTTY.tty()


def main():
    tty.init()
    while True:
        twTTY._rx_buffer = tty._read(err_prompt="/")
        if twTTY._rx_buffer == "":
            tty._write(twTTY._tx_buffer)
            continue
        if twTTY._rx_buffer.__contains__("\n"):
            p.parse(twTTY._rx_buffer)


if __name__== "__main__":
    main()
