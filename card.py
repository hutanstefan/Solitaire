import pygame
from config import DATA


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False
        self.color = self.assign_color()
        self.x = 0
        self.y = 0
        self.scale = (DATA["card_width"], DATA["card_height"])

    def assign_color(self):
        if self.suit in ['hearts', 'diamonds']:
            return "Red"
        elif self.suit in ['clubs', 'spades']:
            return "Black"

    def draw_in_pile(self, surface, pos, card_back, card_sprites):
        if self.face_up:
            sprite = card_sprites[f"{self.rank}_{self.suit}"]
            scaled_sprite = pygame.transform.scale(sprite, self.scale)
            surface.blit(scaled_sprite, pos)
        else:
            scaled_back = pygame.transform.scale(card_back, self.scale)
            surface.blit(scaled_back, pos)

    def draw_drag_card(self, surface):
        sprite = DATA["card_sprites"][f"{self.rank}_{self.suit}"]
        scaled_sprite = pygame.transform.scale(sprite, self.scale)
        if self.x and self.y:
            draw_x = self.x - self.scale[0] // 2
            draw_y = self.y - self.scale[1] // 2
            surface.blit(scaled_sprite, (draw_x, draw_y))

    def print_card(self):
        print(self.suit, self.rank, self.face_up, self.color)
