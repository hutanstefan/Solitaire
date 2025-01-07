from sprites import load_card_sprites

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 800
CARD_WIDTH, CARD_HEIGHT = 80, 120
FPS = 120

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']

PHOTO_WIDTH = 2178
PHOTO_HEIGHT = 1216

PILES_Y = 150

PILES_COORD = [
    {"x":  50, "y": PILES_Y},
    {"x": 150, "y": PILES_Y},
    {"x": 250, "y": PILES_Y},
    {"x": 350, "y": PILES_Y},
    {"x": 450, "y": PILES_Y},
    {"x": 550, "y": PILES_Y},
    {"x": 650, "y": PILES_Y},
]

DECK_Y = 50

START_DECK_COORD = [
    {"x":  1200, "y": DECK_Y},
    {"x":  1300, "y": DECK_Y},
]
DATA = {
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "card_width": CARD_WIDTH,
    "card_height": CARD_HEIGHT,
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
    },
    "piles_coord": PILES_COORD,
    "Deck_coord": START_DECK_COORD,
}

CARD_SPRITES, CARD_BACK = load_card_sprites("cardset.jpg", DATA)
DATA["card_sprites"] = CARD_SPRITES
DATA["card_back"] = CARD_BACK
