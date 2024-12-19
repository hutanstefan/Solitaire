SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 800
CARD_WIDTH, CARD_HEIGHT = 160, 240
FPS = 60

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
RANKS = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']

PHOTO_WIDTH = 2178
PHOTO_HEIGHT = 1216

DATA = {
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "fps": FPS,
    "photo_width": PHOTO_WIDTH,
    "photo_height": PHOTO_HEIGHT,
    "colors": {
        "green": GREEN,
        "white": WHITE,
        "black": BLACK
    },
    "deck": {
        "suits": SUITS,
        "ranks": RANKS
    }
}
