import curses
from curses import wrapper
import time as T
import random as R

sentences = [
    "The quick brown fox jumps over the lazy dog near the riverbank on a sunny afternoon.",
    "A gentle breeze whispered through the trees as the sun set beyond the distant hills.",
    "She opened the door to find a mysterious letter waiting on the welcome mat.",
    "The old clock on the wall ticked steadily, marking the quiet moments of the evening.",
    "John couldn't believe his luck when he found a rare coin hidden under the park bench.",
    "The cat sat on the windowsill, watching the raindrops slide down the glass pane.",
    "In the quiet library, the only sound was the soft turning of pages from a nearby table.",
    "Sarah smiled as she walked through the bustling city, feeling the energy of the crowd around her.",
    "The soft glow of the lanterns lit up the pathway as they walked towards the old village.",
    "A sudden flash of lightning lit up the sky, followed by the rumble of distant thunder.",
]

print(len(sentences))


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
    displayed_text = sentences[R.randint(0, 9)]
    current_char = []
    wpm = 0
    correct_char = 0
    stdscr.clear()
    stdscr.addstr(displayed_text)
    stdscr.refresh()
    start = T.time()
    stdscr.addstr(4, 0, f"WPM:{int(wpm)}")
    stdscr.nodelay(True)
    while True:
        end = T.time()
        time_per_char = max(end - start, 1)
        cpm = len(current_char) / (time_per_char / 60)
        wpm = cpm / 5  # avg word of 5char
        stdscr.addstr(4, 0, f"WPM:{int(wpm)}")
        try:
            char = stdscr.getkey()
        except:
            continue
        stdscr.clear()
        stdscr.addstr(displayed_text)
        if ord(char) == 8:
            if len(current_char) > 0:
                current_char.pop()
            else:
                pass
        else:
            current_char.append(char)
        if len(current_char) >= len(displayed_text) or ord(char) == 27:
            break
        user_sentence = ""
        for i in current_char:
            user_sentence += i
        for i in range(len(user_sentence)):
            if user_sentence[i] == displayed_text[i]:
                stdscr.addstr(0, i, user_sentence[i], curses.color_pair(1))
            else:
                stdscr.addstr(0, i, user_sentence[i], curses.color_pair(2))
    for i, j in zip(user_sentence, displayed_text):
        if i == j:
            correct_char += 1

    return wpm, correct_char


def end_game(stdscr):
    result = typing_test(stdscr)
    wpm = int(result[0])
    correct_char = result[-1]
    stdscr.clear()
    stdscr.addstr(5, 20, "Game Finished")
    stdscr.addstr(6, 20, f"WPM={wpm}")
    stdscr.addstr(7, 20, f"Correct letter={correct_char} letters")
    stdscr.addstr(8, 20, "Press any key to exit the score board")
    stdscr.nodelay(False)
    stdscr.getkey()


def main_gameplay(stdscr):
    while True:
        mode = mainmenu(stdscr)
        if mode in ("Y", "y"):
            end_game(stdscr)
        else:
            break


wrapper(main_gameplay)
