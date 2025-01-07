import pygame
import sys
import math

selected_card_refs = None
last_pile_index = None
last_card_from_deck = None


def handle_events(DATA, screen, piles, deck1, deck2):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    global selected_card_refs
    global last_pile_index
    global last_card_from_deck

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
                deck1_x = DATA["Deck_coord"][0]["x"]
                deck1_y = DATA["Deck_coord"][0]["y"]
                deck2_x = DATA["Deck_coord"][1]["x"]
                deck2_y = DATA["Deck_coord"][1]["y"]
                card_width = DATA["card_width"]
                card_height = DATA["card_height"]

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
                            card_index = math.ceil((mouse_y - DATA["piles_coord"][i]["y"]) / 20)

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
                invalid_move = True
                for i, pile in enumerate(piles):
                    if pile:
                        pile_x = DATA["piles_coord"][i]["x"]
                        card_width = DATA["card_width"]

                        if pile_x <= mouse_x <= pile_x + card_width:
                            card = pile[-1]

                            if card.face_up:
                                pile.extend(selected_card_refs)
                                selected_card_refs = None
                                invalid_move = False

                if invalid_move and selected_card_refs:
                    if last_pile_index:
                        piles[last_pile_index].extend(selected_card_refs)
                        selected_card_refs = None
                        break
                    if last_card_from_deck:
                        deck1.insert(0, selected_card_refs[0])
                        selected_card_refs = None
                        break

    if selected_card_refs:
        from draw import draw_dragged_cards
        draw_dragged_cards(screen, selected_card_refs, mouse_x, mouse_y)
