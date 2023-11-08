import random
import time
import curses
import itertools


stdscr = curses.initscr()

goal = [12, 20]
stdscr.addch(goal[0], goal[1], "🍪")

current = [10, 10]
stdscr.addch(current[0], current[1], "😃")

i = 0
stdscr.addstr(0, 0, f"age: {i:>4}")
stdscr.refresh()
stdscr.getch()

for i in itertools.count(start=1):
    stdscr.addstr(0, 0, f"age: {i:>4}")
    stdscr.addch(current[0], current[1], " ")
    
    axis = random.choice([0, 1])
    move = random.choice([-1, 1])

    # 画面外への移動を制限    
    if current[axis] + move >= 1:  
        current[axis] += move
    
    if current == goal:
        stdscr.addch(current[0], current[1], "😍")
        stdscr.refresh()
        break
    
    stdscr.addch(current[0], current[1], "😃")
    stdscr.refresh()
    time.sleep(0.1)

stdscr.getch()
curses.endwin()
