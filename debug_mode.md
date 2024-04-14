# Debug Capabilities of this Project.

This is a part of the technical literature of this discomboulated project.

## twTTY_DEBUG.py

twTTY_DEBUG was written in need of a Telex-Machine / Teletype.
This class will transform your typical Terminal into a Teletype.

### Differences real TTY <-> twTTY_DEBUG

By default a teletype is character based.
So this Software listens to a `\n`-Keypress. My SEL LO 3000 has a `return` key.
This sends `\r\n` via the Line-Adaptor-Module (LAT).

After every output from twTTY a `prompt` is added.
This is a string with `\r\n` appended.

The default prompt is `/\r\n`. This three chars are the absolute minimum, this software creates.

twTTY_DEBUG has three major Methods:

- twTTY_DEBUG.write() -> Prints output via `python.print` to terminal
- twTTY_DEBUG.read() -> Reads input via `python.input` from Terminal
- twTTY_DEBUG._check_commands() -> Prints Commands for Line initiation / termination to Terminal.
- twTTY_DEBUG.exit() -> does nothing, no session is terminated


Regardless the python-default `print` and `input` is line based.

## Enter debug mode

Edit twTTY.py:

1. add `import twTTY_DEBUG`
2. create Object `_tty` with `_tty: twTTY_DEBUG.tty_debug = twTTY_DEBUG.tty_debug()`
3. Comment out `_tty: ed1000.TelexED1000SC = ed1000.TelexED1000SC()`

Run program


## Leave debug mode

Revert Changes from Chapter "Enter debug mode"