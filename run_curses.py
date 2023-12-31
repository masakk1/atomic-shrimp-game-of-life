import curses
from golife import grid

grid = grid.LifeGrid()

FPS = 1

def iterate(stdscr):
    win_h, win_w = stdscr.getmaxyx()
    half_h, half_w = win_h // 2, win_w // 2

    grid.evolve()
    grid_display = grid.get_string_array((-half_w, -half_h, half_w, half_h-1))
    for x, row in enumerate(grid_display):
        for y, value in enumerate(row):
            stdscr.addch(y, x, value)


def main(stdscr):
    curses.delay_output(FPS * 1000)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        iterate(stdscr)
        stdscr.refresh()

# Initialize curses
curses.wrapper(main)
