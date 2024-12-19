import pygame
import sys
from random import shuffle
from config import DATA
from draw import draw_table
from events import handle_events

SCREEN_WIDTH = DATA["screen_width"]
SCREEN_HEIGHT = DATA["screen_height"]
FPS = DATA["fps"]
SUITS = DATA["deck"]["suits"]
RANKS = DATA["deck"]["ranks"]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solitaire")
clock = pygame.time.Clock()


def create_deck():
    from card import Card
    deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    shuffle(deck)
    return deck


deck = create_deck()
piles = [[] for _ in range(7)]

for i in range(7):
    for j in range(i + 1):
        card = deck.pop()
        if j == i:
            card.face_up = True
        piles[i].append(card)


def main():
    running = True
    while running:
        running = handle_events()

        draw_table(screen, piles)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
