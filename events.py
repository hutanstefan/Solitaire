import pygame
import sys
import math

selected_card_refs = None
last_pile_index = None
last_card_from_deck = None


def handle_events(DATA, screen, piles, deck1, deck2, clubs_deck, diamonds_deck, hearts_deck, spades_deck):
    """
    Handle all game events, including mouse.

    Args:
        DATA (dict): A dictionary containing game configuration data.
        screen (pygame.Surface): The surface to draw the game on.
        piles (list): A list of piles of cards.
        deck1 (list): The first deck of cards.
        deck2 (list): The second deck of cards.
        clubs_deck (list): The deck of clubs.
        diamonds_deck (list): The deck of diamonds.
        hearts_deck (list): The deck of hearts.
        spades_deck (list): The deck of spades.
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    global selected_card_refs
    global last_pile_index
    global last_card_from_deck
    card_width = DATA["card_width"]
    card_height = DATA["card_height"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                deck1_x = DATA["deck_coord"][0]["x"]
                deck1_y = DATA["deck_coord"][0]["y"]
                deck2_x = DATA["deck_coord"][1]["x"]
                deck2_y = DATA["deck_coord"][1]["y"]

                if deck2_x <= mouse_x <= deck2_x + card_width and deck2_y <= mouse_y <= deck2_y + card_height:
                    if deck2:
                        card = deck2.pop()
                        card.face_up = True
                        deck1.insert(0, card)
                        break
                    else:
                        if deck1:
                            for card in deck1:
                                card.face_up = False
                            deck2.extend(deck1)
                            deck1.clear()
                        break
                if deck1_x <= mouse_x <= deck1_x + card_width and deck1_y <= mouse_y <= deck1_y + card_height:
                    if deck1:
                        selected_card_refs = [deck1.pop(0)]
                        last_card_from_deck = True
                        last_pile_index = None
                        break

                for i, pile in enumerate(piles):
                    if pile:
                        pile_x = DATA["piles_coord"][i]["x"]
                        card_width = DATA["card_width"]

                        if pile_x <= mouse_x <= pile_x + card_width:
                            card_index = math.ceil((mouse_y - DATA["piles_coord"][i]["y"]) / DATA["space_cards"])

                            card_index = min(card_index - 1, len(pile) - 1)
                            card_index = max(card_index, 0)

                            card = pile[card_index]

                            if card.face_up:
                                selected_card_refs = pile[card_index:]
                                last_pile_index = i
                                last_card_from_deck = False

                                for _ in selected_card_refs:
                                    pile.pop()

                            elif card_index == len(pile) - 1:
                                card.face_up = True
                            break
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selected_card_refs:
                clubs_deck_x = DATA["clubs_deck_coord"][0]["x"]
                clubs_deck_y = DATA["clubs_deck_coord"][0]["y"]
                diamonds_deck_x = DATA["diamonds_deck_coord"][0]["x"]
                diamonds_deck_y = DATA["diamonds_deck_coord"][0]["y"]
                hearts_deck_x = DATA["hearts_deck_coord"][0]["x"]
                hearts_deck_y = DATA["hearts_deck_coord"][0]["y"]
                spades_deck_x = DATA["spades_deck_coord"][0]["x"]
                spades_deck_y = DATA["spades_deck_coord"][0]["y"]
                invalid_move = True

                if clubs_deck_x <= mouse_x <= clubs_deck_x + card_width and clubs_deck_y <= mouse_y <= clubs_deck_y + card_height:
                    if len(selected_card_refs) == 1 and selected_card_refs[0].suit == 'clubs':
                        card = clubs_deck[-1] if clubs_deck else None
                        if selected_card_refs[0].rank == "A" or (card and selected_card_refs[0].rank == DATA["deck"]["ranks"][DATA["deck"]["ranks"].index(card.rank) + 1]):
                            clubs_deck.append(selected_card_refs[0])
                            selected_card_refs = None
                            last_pile_index = None
                            last_card_from_deck = None
                            invalid_move = False
                            break

                if diamonds_deck_x <= mouse_x <= diamonds_deck_x + card_width and diamonds_deck_y <= mouse_y <= diamonds_deck_y + card_height:
                    if len(selected_card_refs) == 1 and selected_card_refs[0].suit == 'diamonds':
                        card = diamonds_deck[-1] if diamonds_deck else None
                        if selected_card_refs[0].rank == "A" or (card and selected_card_refs[0].rank == DATA["deck"]["ranks"][DATA["deck"]["ranks"].index(card.rank) + 1]):
                            diamonds_deck.append(selected_card_refs[0])
                            selected_card_refs = None
                            last_pile_index = None
                            last_card_from_deck = None
                            invalid_move = False
                            break

                if hearts_deck_x <= mouse_x <= hearts_deck_x + card_width and hearts_deck_y <= mouse_y <= hearts_deck_y + card_height:
                    if len(selected_card_refs) == 1 and selected_card_refs[0].suit == 'hearts':
                        card = hearts_deck[-1] if hearts_deck else None
                        if selected_card_refs[0].rank == "A" or (card and selected_card_refs[0].rank == DATA["deck"]["ranks"][DATA["deck"]["ranks"].index(card.rank) + 1]):
                            hearts_deck.append(selected_card_refs[0])
                            selected_card_refs = None
                            last_pile_index = None
                            last_card_from_deck = None
                            invalid_move = False
                            break

                if spades_deck_x <= mouse_x <= spades_deck_x + card_width and spades_deck_y <= mouse_y <= spades_deck_y + card_height:
                    if len(selected_card_refs) == 1 and selected_card_refs[0].suit == 'spades':
                        card = spades_deck[-1] if spades_deck else None
                        if selected_card_refs[0].rank == "A" or (card and selected_card_refs[0].rank == DATA["deck"]["ranks"][DATA["deck"]["ranks"].index(card.rank) + 1]):
                            spades_deck.append(selected_card_refs[0])
                            selected_card_refs = None
                            last_pile_index = None
                            last_card_from_deck = None
                            invalid_move = False
                            break

                for i, pile in enumerate(piles):
                    pile_x = DATA["piles_coord"][i]["x"]

                    if pile_x <= mouse_x <= pile_x + card_width:
                        if pile:
                            card = pile[-1]

                            if card.face_up and selected_card_refs[0].color != card.color and selected_card_refs[0].rank == DATA["deck"]["ranks"][DATA["deck"]["ranks"].index(card.rank) - 1]:
                                pile.extend(selected_card_refs)
                                selected_card_refs = None
                                invalid_move = False
                        else:
                            if selected_card_refs[0].rank == "K":
                                pile.extend(selected_card_refs)
                                selected_card_refs = None
                                invalid_move = False

                if invalid_move and selected_card_refs:
                    if last_pile_index is not None:
                        piles[last_pile_index].extend(selected_card_refs)
                        selected_card_refs = None
                        break
                    if last_card_from_deck:
                        deck1.insert(0, selected_card_refs[0])
                        selected_card_refs = None
                        break

    if selected_card_refs:
        from draw import draw_dragged_cards
        draw_dragged_cards(DATA, screen, selected_card_refs, mouse_x, mouse_y)
