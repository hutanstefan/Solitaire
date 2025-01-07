
def draw_table(DATA, screen, piles, deck1, deck2):
    screen.fill(DATA["colors"]["green"])

    for i, pile in enumerate(piles):
        x = DATA["piles_coord"][i]["x"]
        y = DATA["piles_coord"][i]["y"]

        for card in pile:
            if card:
                card.draw_in_pile(screen, (x, y), DATA["card_back"], DATA["card_sprites"])
                y += 20

    deck1_pos = DATA["Deck_coord"][0]
    for i, card in enumerate(deck1):
        if i == 0:  # Doar primul card, ca reprezentare vizuală a deck-ului
            card.draw_in_pile(screen, (deck1_pos["x"], deck1_pos["y"]), DATA["card_back"], DATA["card_sprites"])

    # Desenează deck2
    deck2_pos = DATA["Deck_coord"][1]
    for i, card in enumerate(deck2):
        if i == 0:
            card.draw_in_pile(screen, (deck2_pos["x"], deck2_pos["y"]), DATA["card_back"], DATA["card_sprites"])


def draw_dragged_cards(screen, selected_card_refs, mouse_x, mouse_y):
    y_offset = 0
    for card in selected_card_refs:
        card.x = mouse_x
        card.y = mouse_y + y_offset
        card.draw_drag_card(screen)
        y_offset += 20
