RES = WIDTH, HEIGHT = 1200, 675  # adjusting will break bg
FPS = 20
HALF_W, HALF_H = WIDTH // 2, HEIGHT // 2  # adjusting will break bg
RADIUS = HALF_H - 50  # adjusting will break bg
CLOCK_EDGE_W = 5  
FONT = 'Verdana'
DGTL_FONTSIZE = 60
CLOCK_COLOR = 'darkslategray'
SEC_HAND_COLOR = 'magenta'
MIN_HAND_COLOR = 'black'
HOUR_HAND_COLOR = 'black'
SEC_HAND_W = 3
MIN_HAND_W = 7
HOUR_HAND_W = 10
RADII = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARC = RADIUS + 8