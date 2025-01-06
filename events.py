import pygame
import sys


def handle_events(DATA, piles, selected_card_ref, screen):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_card = selected_card_ref[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, pile in enumerate(piles):
                    if pile:
                        pile_x = DATA["piles_coord"][i]["x"]
                        card_width = DATA["card_width"]

                        if pile_x <= mouse_x <= pile_x + card_width:
                            card = pile[-1]

                            if card.face_up:
                                pile.pop()
                                selected_card_ref[0] = card
                            else:
                                card.face_up = True
                            break
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected_card_ref[0] = None
                break
        if selected_card:
            selected_card.x = mouse_x
            selected_card.y = mouse_y
            selected_card.draw_drag_card(screen)
