from pygame import font


class Label():
    def __init__(self, name, font, text, pos_x, pos_y):
        self.name = name
        # Text Properties
        self.font = font
        self.text = text
        # Coordinates
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, screen):
        return screen.blit(font.Font.render(self.font, self.text, True, (128, 128, 128)), (self.pos_x, self.pos_y))
    
    def update(self, screen):
        return screen.blit(font.Font.render(self.font, self.text, True, (128, 128, 128)), (self.pos_x, self.pos_y))