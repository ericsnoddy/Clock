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
# clock12 = dict(zip(range(12), range(0, 360, 30)))  # for hours: (key=0, val=0), (1, 30), ..., (key=11, val=330)
clock60 = dict(zip(range(60), range(0, 360, 6)))   # for mins/secs: (0, 0), ..., (59, 354)

font = pg.font.SysFont(FONT, DGTL_FONTSIZE)
img = pg.image.load('img/bg_cutout.png').convert_alpha()
bg = pg.image.load('img/bg4.jpg').convert()
bg_rect = bg.get_rect(center=RES)
dx, dy = 1, 1

def get_clock_pos(clock_dict, clock_hand, hand_type):
    x = HALF_W + RADII[hand_type] * cos(radians(clock_dict[clock_hand]) - (pi / 2))  # subtract 90 degs b/c pygame polar coords begin at the right
    y = HALF_H + RADII[hand_type] * sin(radians(clock_dict[clock_hand]) - (pi / 2))
    return x, y

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()

    # set bg
    dx *= -1 if bg_rect.left > 0 or bg_rect.right < WIDTH else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < HEIGHT else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    win.blit(bg, bg_rect)
    win.blit(img, (0, 0))

    # get datetime info
    t = datetime.now()
    # converting 'hour' to minutes past because hour hand needs to traverse through all the numbers
    # eg, 19:54 -> 19 % 12 = 7 * 5 = 35 + 54//12 = 35 + 4 = 39 % 60 = 39. The hour hand needs to point to 39.
    hour, min, sec = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

    # draw analog clock face
    for digit, pos in clock60.items():
        if not digit % 3 and not digit % 5:  # if divisible by 3 and 5 (0, 15, 30, 45)
            radius = 20
        elif not digit % 5: # if divisible by 5 and not a number from step above (5, 10, 20, ... 55)
            radius = 8
        else:  # not divisible (all other numbers)
            radius = 2
        pg.draw.circle(win, 'gainsboro', get_clock_pos(clock60, digit, 'digit'), radius, 7)


    # draw analog clock hands
    pg.draw.circle(win, 'darkslategray', (HALF_W, HALF_H), RADIUS, CLOCK_EDGE_W)
    pg.draw.line(win, 'green', (HALF_W, HALF_H), get_clock_pos(clock60, hour, 'hour'), HOUR_HAND_W)
    pg.draw.line(win, 'yellow', (HALF_W, HALF_H), get_clock_pos(clock60, min, 'min'), MIN_HAND_W)
    pg.draw.line(win, 'magenta', (HALF_W, HALF_H), get_clock_pos(clock60, sec, 'sec'), SEC_HAND_W)
    pg.draw.circle(win, 'white', (HALF_W, HALF_H), 8)
    
    # draw digital clock
    # time_render = font.render(f'{t:%H:%M:%S}', True, 'forestgreen', 'orange')
    # win.blit(time_render, (0, 0))

    # draw arc
    sec_angle = -radians(clock60[t.second]) + pi / 2
    pg.draw.arc(win, 'magenta', 
                (HALF_W - RADIUS_ARC, HALF_H - RADIUS_ARC, 2 * RADIUS_ARC, 2 * RADIUS_ARC),
                pi / 2, sec_angle, 8)

    pg.display.flip()
    pg.display.set_caption(f'{clock.get_fps(): .1f}')
    clock.tick(FPS)