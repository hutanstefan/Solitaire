import pygame
from config import DATA


class Card:
    """
    A class to represent a Solitare playing card.

    Attributes:
        suit (str): The suit of the card (e.g., 'hearts', 'diamonds').
        rank (str): The rank of the card (e.g., 'A', '2', 'K').
        face_up (bool): Whether the card is face up or face down.
        color (str): The color of the card ('Red' or 'Black').
        x (int): The x-coordinate of the card's position when is moved by the mouse.
        y (int): The y-coordinate of the card's position when is moved by the mouse.
        scale (tuple): The width and height to scale the card sprite to.
    """
    def __init__(self, suit, rank):
        """
        Initialize a Card object.

        Args:
            suit (str): The suit of the card.
            rank (str): The rank of the card.
        """
        self.suit = suit
        self.rank = rank
        self.face_up = False
        self.color = self.assign_color()
        self.x = 0
        self.y = 0
        self.scale = (DATA["card_width"], DATA["card_height"])

    def assign_color(self):
        """
        Assign the color of the card based on its suit.

        Returns:
            str: 'Red' if the suit is 'hearts' or 'diamonds', 'Black' if the suit is 'clubs' or 'spades'.
        """
        if self.suit in ['hearts', 'diamonds']:
            return "Red"
        elif self.suit in ['clubs', 'spades']:
            return "Black"

    def draw_in_pile(self, surface, pos, card_back, card_sprites):
        """
        Draw the card in a pile on the given surface.

        Args:
            surface (pygame.Surface): The screen to draw the card on.
            pos (tuple): The (x, y) position to draw the card at.
            card_back (pygame.Surface): The image to use for the back of the card.
            card_sprites (dict): A dictionary of card sprites.
        """
        if self.face_up:
            sprite = card_sprites[f"{self.rank}_{self.suit}"]
            scaled_sprite = pygame.transform.scale(sprite, self.scale)
            surface.blit(scaled_sprite, pos)
        else:
            scaled_back = pygame.transform.scale(card_back, self.scale)
            surface.blit(scaled_back, pos)

    def draw_drag_card(self, surface):
        """
        Draw the card while it is being dragged by the mouse.

        Args:
            surface (pygame.Surface): The screen to draw the card on.
        """
        sprite = DATA["card_sprites"][f"{self.rank}_{self.suit}"]
        scaled_sprite = pygame.transform.scale(sprite, self.scale)
        if self.x and self.y:
            draw_x = self.x - self.scale[0] // 2
            draw_y = self.y - self.scale[1] // 2
            surface.blit(scaled_sprite, (draw_x, draw_y))

    def draw_in_deck(self, surface, pos, card_sprites):
        """
        Draw the card in a deck on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the card on.
            pos (tuple): The (x, y) position to draw the card at.
            card_sprites (dict): A dictionary of card sprites.
        """
        sprite = card_sprites[f"{self.rank}_{self.suit}"]
        scaled_sprite = pygame.transform.scale(sprite, self.scale)
        surface.blit(scaled_sprite, pos)

    def print_card(self):
        """
        Print the card's attributes to the console for debugging purposes.
        """
        print(self.suit, self.rank, self.face_up, self.color)
