from pygame import rect, draw
import constants


class Town():
    def __init__(self, name, level, pos_x, pos_y):
        self.name = name
        # Level and Size
        self.level = level
        self.size = self.level * constants.TOWN_DIMENSIONS
        # Position
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Hitbox
        self.hitbox = rect.Rect(
            self.pos_x, self.pos_y,
            self.size, self.size
        )
        # Supply Bonus
        self.supply_bonus = self.size

    def draw(self, screen):
        return draw.rect(screen, constants.TOWN_BASE_COLOR, self.hitbox, 0)
    
    def resupply(self):
        pass