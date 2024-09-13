import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 30, "Hello World")
    stdscr.refresh()
    stdscr.getkey()


def multiple_line(stdcr):
    stdcr.addstr(3, 0, "welcome to curses")
    stdcr.refresh()
    stdcr.getkey()
    stdcr.clear()
    stdcr.addstr(4, 0, "exit the curses")
    stdcr.getkey()


def move_cursor(stdcr):
    stdcr.move(5, 10)
    stdcr.addstr("Hello")
    stdcr.getkey()


def main1(stdscr):
    stdscr.clear()

    # Add text to the screen buffer
    stdscr.addstr(0, 0, "This will be displayed")

    # Refresh the screen to show the changes
    stdscr.refresh()

    # Wait for a key press
    stdscr.getkey()


def main2(stdscr):
    stdscr.clear()

    # Add text to the screen buffer
    stdscr.addstr(0, 0, "This will NOT be displayed")

    # Notice there's no stdscr.refresh() here

    # Wait for a key press
    stdscr.getkey()


def close(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to Curses\npress q to exit")
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "q" or key == "Q":
            break


def window(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to menu\n")
    stdscr.addstr("option1\n")
    stdscr.addstr("option 2\n")
    stdscr.addstr("quit")
    while True:
        key = stdscr.getkey()
        stdscr.clear()
        if key == "1":
            stdscr.addstr("1")
        elif key == "2":
            stdscr.addstr("2")
        elif key == "q" or key == "Q":
            break
        else:
            stdscr.addstr("invalid option")


def color(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.addstr(10, 30, "Hello World", curses.color_pair(1))

    stdscr.getkey()
    stdscr.addstr(10, 30, "Hello World", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()


def overright(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)
    stdscr.clear()
    stdscr.addstr(1, 0, "hello my name is ronish")
    stdscr.refresh()
    c = 0
    while c < 25:
        char = stdscr.getkey()
        stdscr.addstr(1, c, char, curses.color_pair(1))
        c += 1


wrapper(overright)
