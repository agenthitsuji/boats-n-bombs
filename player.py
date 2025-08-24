import pygame, constants


class Player(pygame.rect.Rect):
    def __init__(self, color: tuple, pos_x: int,  pos_y: int, width: int, height: int, border: int ):
        super().__init__(color, [pos_x, pos_y, width, height], border)
