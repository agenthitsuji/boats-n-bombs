from pygame import rect, image, draw, Surface, key
import constants, pygame


class Boat():
    def __init__(self, name: str, sprite: Surface, position: tuple):
        # Boat Name
        self.name = name
        # Sprite
        self.sprite = image.load("/home/yoichann/boats-and-bombs/boat.png").convert()
        self.sprite.set_colorkey((0,255,0))
        # Converting Sprite Dimensions 
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        # Boat Position
        self.pos_x, self.pos_y = position
        # Boat Hitbox as Rect
        self.hitbox = rect.Rect(
            self.pos_x, self.pos_y, 
            self.width, self.height
            )
        # Stats
        self.speed = constants.BOAT_SPEED * 2


    def draw(self, screen):
        self.update()
        return draw.rect(screen, constants.HITBOX_COLOR, self.hitbox, 1), screen.blit(self.sprite, (self.pos_x, self.pos_y))

    def move(self):
        if key.get_pressed()[pygame.K_RIGHT]:
            self.pos_x += self.speed
            print(f"boat is at: {self.pos_x} {self.pos_y}") 
        elif key.get_pressed()[pygame.K_LEFT]:
            self.pos_x -= self.speed
            print(f"boat is at: {self.pos_x} {self.pos_y}")
        elif key.get_pressed()[pygame.K_UP]:
            self.pos_y -= self.speed
            print(f"boat is at: {self.pos_x} {self.pos_y}") 
        elif key.get_pressed()[pygame.K_DOWN]:
            self.pos_y += self.speed        
            print(f"boat is at: {self.pos_x} {self.pos_y}")

    def update(self):
        self.hitbox.left = self.pos_x
        self.hitbox.top = self.pos_y
        self.move()