import sys, traceback

from rut.controller import Controller
from rut.pane import Pane
from rut.tui import Tui

def main():
    if len(sys.argv) == 2:
        pane = Pane(path=sys.argv[1])
    else:
        pane = Pane()
    display = Tui(pane)
    controller = Controller(pane)
    try:
        while True:
            display.display_pane(pane)
            controller.send_key(chr(display.get_input()))
    except:
        display.end()
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
