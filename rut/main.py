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
    display.display_pane(pane)
    try:
        while True:
            controller.send_key(display.get_input())
    except:
        display.end()
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
