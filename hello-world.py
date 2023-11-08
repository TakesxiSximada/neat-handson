import curses

stdscr = curses.initscr()                # 画面を初期化する
stdscr.addch(0, 0, "😃")                 # 1文字表示する
stdscr.addstr(0, 2, " < Hello, world!")  # 文字列を表示する
stdscr.refresh()                         # 画面の変更を反映する
stdscr.getch()                           # 入力を待ち受ける
curses.endwin()                          # cursesを終了する
