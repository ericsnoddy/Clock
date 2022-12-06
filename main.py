# std lib
from datetime import datetime
from math import radians, pi, sin, cos

# reqs
import pygame as pg

# local
from config import *


# pygame init
pg.init()
win = pg.display.set_mode(RES)
clock = pg.time.Clock()

# aggregate tuples 1-to-1 as keys in a dictionary - values will be angles to rotate from start
clock12 = dict(zip(range(12), range(0, 360, 30)))  # for hours: (key=0, val=0), (1, 30), ..., (key=11, val=330)
clock60 = dict(zip(range(60), range(0, 360, 6)))   # for mins/secs: (0, 0), ..., (59, 354)

font = pg.font.SysFont(FONT, DGTL_FONTSIZE)

def get_clock_pos(clock_dict, clock_hand):
    x = HALF_W + RADIUS * cos(radians(clock_dict[clock_hand])) - pi / 2  # subtract 90 degs b/c pygame polar coords begin at the right
    y = HALF_H + RADIUS * sin(radians(clock_dict[clock_hand])) - pi / 2
    return x, y

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()

    win.fill('black')
    t = datetime.now()
    hour, min, sec = t.hour % 12, t.minute, t.second
    # draw clock
    pg.draw.circle(win, 'darkslategray', (HALF_W, HALF_H), RADIUS, CLOCK_EDGE_W)
    pg.draw.line(win, 'magenta', (HALF_W, HALF_H), get_clock_pos(clock60, sec), SEC_HAND_W)

    time_render = font.render(f'{t:%H:%M:%S}', True, 'forestgreen', 'orange')
    win.blit(time_render, (0, 0))

    pg.display.flip()
    pg.display.set_caption(f'{clock.get_fps(): .1f}')
    clock.tick(FPS)