from config import GREEN, CARD_WIDTH
from sprites import load_card_sprites

CARD_SPRITES, CARD_BACK = load_card_sprites("cardset.jpg")


def draw_table(screen, piles):
    screen.fill(GREEN)

    x_offset = 50
    y_offset = 150
    for pile in piles:
        x = x_offset
        y = y_offset
        for card in pile:
            card.draw(screen, (x, y), CARD_BACK, CARD_SPRITES)
            y += 20
        x_offset += CARD_WIDTH + 20
