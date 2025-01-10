import pygame


def load_card_sprites(image_path, DATA):
    """
    Load card sprites from a sprite sheet image.

    Args:
        image_path (str): The path to the sprite sheet image.
        DATA (dict): A dictionary containing game configuration data.

    Returns:
        tuple: A dictionary of card sprites and the card back image.
    """
    CARD_WIDTH = DATA["photo_width"] // 13
    CARD_HEIGHT = DATA["photo_height"] // 5
    sprite_sheet = pygame.image.load(image_path)
    card_sprites = {}

    suits = DATA["deck"]["suits"]
    ranks = DATA["deck"]["ranks"]

    card_back = sprite_sheet.subsurface(pygame.Rect(2 * CARD_WIDTH, 4 * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))

    for row, suit in enumerate(suits):
        for col, rank in enumerate(ranks):
            x = col * CARD_WIDTH
            y = row * CARD_HEIGHT
            card_sprites[f"{rank}_{suit}"] = sprite_sheet.subsurface(pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT))

    return card_sprites, card_back
