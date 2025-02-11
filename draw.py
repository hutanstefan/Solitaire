
import pygame


def draw_text(screen, text, pos, font, color):
    """
    Draw text on the screen.

    Args:
        screen (pygame.Surface): The surface to draw the text on.
        text (str): The text to be drawn.
        pos (tuple): The (x, y) position to draw the text at.
        font (pygame.font.Font): The font to use for the text.
        color (tuple): The color of the text.
    """
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)


def draw_table(DATA, screen, piles, deck1, deck2, clubs_deck, diamonds_deck, hearts_deck, spades_deck):
    """
    Draw the game table, including piles and decks.

    Args:
        DATA (dict): A dictionary containing game configuration data.
        screen (pygame.Surface): The surface to draw the table on.
        piles (list): A list of piles of cards.
        deck1 (list): The first deck of cards.
        deck2 (list): The second deck of cards.
        clubs_deck (list): The deck of clubs.
        diamonds_deck (list): The deck of diamonds.
        hearts_deck (list): The deck of hearts.
        spades_deck (list): The deck of spades.
    """
    screen.fill(DATA["colors"]["green"])

    for i, pile in enumerate(piles):
        x = DATA["piles_coord"][i]["x"]
        y = DATA["piles_coord"][i]["y"]

        if len(pile) == 0:
            pygame.draw.rect(screen, DATA["colors"]["black"], pygame.Rect(x, y, DATA["card_width"], DATA["card_height"]), 2)

        for card in pile:
            if card:
                card.draw_in_pile(screen, (x, y), DATA["card_back"], DATA["card_sprites"])
                y += DATA["space_cards"]

    deck1_pos = DATA["deck_coord"][0]
    for i, card in enumerate(deck1):
        if i == 0:
            card.draw_in_pile(screen, (deck1_pos["x"], deck1_pos["y"]), DATA["card_back"], DATA["card_sprites"])

    deck2_pos = DATA["deck_coord"][1]
    for i, card in enumerate(deck2):
        if i == 0:
            card.draw_in_pile(screen, (deck2_pos["x"], deck2_pos["y"]), DATA["card_back"], DATA["card_sprites"])

    font = pygame.font.Font(None, 36)
    clubs_deck_pos = DATA["clubs_deck_coord"][0]
    if len(clubs_deck) == 0:
        pygame.draw.rect(screen, DATA["colors"]["black"], pygame.Rect(clubs_deck_pos["x"], clubs_deck_pos["y"], DATA["card_width"], DATA["card_height"]), 2)
        draw_text(screen, "C", (clubs_deck_pos["x"] + DATA["card_width"] // 2 - 10, clubs_deck_pos["y"] + DATA["card_height"] // 2 - 10), font, DATA["colors"]["black"])
    else:
        card = clubs_deck[-1]
        card.draw_in_deck(screen, (clubs_deck_pos["x"], clubs_deck_pos["y"]), DATA["card_sprites"])

    diamonds_deck_pos = DATA["diamonds_deck_coord"][0]
    if len(diamonds_deck) == 0:
        pygame.draw.rect(screen, DATA["colors"]["black"], pygame.Rect(diamonds_deck_pos["x"], diamonds_deck_pos["y"], DATA["card_width"], DATA["card_height"]), 2)
        draw_text(screen, "D", (diamonds_deck_pos["x"] + DATA["card_width"] // 2 - 10, diamonds_deck_pos["y"] + DATA["card_height"] // 2 - 10), font, DATA["colors"]["black"])
    else:
        card = diamonds_deck[-1]
        card.draw_in_deck(screen, (diamonds_deck_pos["x"], diamonds_deck_pos["y"]), DATA["card_sprites"])

    hearts_deck_pos = DATA["hearts_deck_coord"][0]
    if len(hearts_deck) == 0:
        pygame.draw.rect(screen, DATA["colors"]["black"], pygame.Rect(hearts_deck_pos["x"], hearts_deck_pos["y"], DATA["card_width"], DATA["card_height"]), 2)
        draw_text(screen, "H", (hearts_deck_pos["x"] + DATA["card_width"] // 2 - 10, hearts_deck_pos["y"] + DATA["card_height"] // 2 - 10), font, DATA["colors"]["black"])
    else:
        card = hearts_deck[-1]
        card.draw_in_deck(screen, (hearts_deck_pos["x"], hearts_deck_pos["y"]), DATA["card_sprites"])

    spades_deck_pos = DATA["spades_deck_coord"][0]
    if len(spades_deck) == 0:
        pygame.draw.rect(screen, DATA["colors"]["black"], pygame.Rect(spades_deck_pos["x"], spades_deck_pos["y"], DATA["card_width"], DATA["card_height"]), 2)
        draw_text(screen, "S", (spades_deck_pos["x"] + DATA["card_width"] // 2 - 10, spades_deck_pos["y"] + DATA["card_height"] // 2 - 10), font, DATA["colors"]["black"])
    else:
        card = spades_deck[-1]
        card.draw_in_deck(screen, (spades_deck_pos["x"], spades_deck_pos["y"]), DATA["card_sprites"])

    if len(clubs_deck) == 13 and len(diamonds_deck) == 13 and len(hearts_deck) == 13 and len(spades_deck) == 13:
        draw_text(screen, "You Win!", (DATA["screen_width"] // 2 - 100, DATA["screen_height"] // 2), font, DATA["colors"]["white"])


def draw_dragged_cards(DATA, screen, selected_card_refs, mouse_x, mouse_y):
    """
    Draw the cards that are being dragged by the mouse.

    Args:
        DATA (dict): A dictionary containing game configuration data.
        screen (pygame.Surface): The surface to draw the cards on.
        selected_card_refs (list): A list of selected card references.
        mouse_x (int): The x-coordinate of the mouse position.
        mouse_y (int): The y-coordinate of the mouse position.
    """
    y_offset = 0
    for card in selected_card_refs:
        card.x = mouse_x
        card.y = mouse_y + y_offset
        card.draw_drag_card(screen)
        y_offset += DATA["space_cards"]
