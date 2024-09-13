import curses
from curses import wrapper


def mainmenu(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to word per minute game\n")
    stdscr.addstr("press Y to start(any other key to leave)\n")
    stdscr.refresh()
    mode = stdscr.getkey()
    return mode


def typing_test(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    displayed_text = "Hello My name is Ronish Makaju"
    current_char = []
    stdscr.clear()
    stdscr.addstr(displayed_text)
    stdscr.refresh()
    while True:
        char = stdscr.getkey()
        stdscr.clear()
        stdscr.addstr(displayed_text)
        if ord(char) == 8:
            current_char.pop()
        else:
            current_char.append(char)
        if len(current_char) > len(displayed_text) or ord(char) == 27:
            break
        user_sentence = ""
        for i in current_char:
            user_sentence += i
        for i in range(len(user_sentence)):
            if user_sentence[i] == displayed_text[i]:
                stdscr.addstr(0, i, user_sentence[i], curses.color_pair(1))
            else:
                stdscr.addstr(0, i, user_sentence[i], curses.color_pair(2))


def printsome(stdscr):
    a = stdscr.getkey()

    print(f"a={a}=")
    print(ord(a))


wrapper(typing_test)
