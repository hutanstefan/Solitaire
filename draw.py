from config import GREEN


def draw_table(DATA, screen, piles):
    screen.fill(GREEN)

    for i, pile in enumerate(piles):
        x = DATA["piles_coord"][i]["x"]
        y = DATA["piles_coord"][i]["y"]

        for card in pile:
            card.draw_in_pile(screen, (x, y), DATA["card_back"], DATA["card_sprites"])
            y += 20
