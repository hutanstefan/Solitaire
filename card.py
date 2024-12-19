class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def draw(self, surface, pos, card_back, card_sprites):
        if self.face_up:
            sprite = card_sprites[f"{self.rank}_{self.suit}"]
            surface.blit(sprite, pos)
        else:
            surface.blit(card_back, pos)
