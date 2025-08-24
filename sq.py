import pygame


class Sq(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill("WHITE")

    def __repr__(self):
        return f"Width: {self.width}, Height: {self.height}"