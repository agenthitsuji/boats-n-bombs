import pygame, sys, constants

from town import Town
from player import Player
from boat import Boat
from label import Label



def main():
    print("Hello from boats-n-bombs!!!")

    # Initialize PyGame
    pygame.init()

    # Clock
    clock = pygame.time.Clock()
    dt = 0

    # Fonts

    font_large = pygame.font.SysFont('veraserif', 24)
    font_small = pygame.font.SysFont('veraserif', 18)

    # Screen
    screen = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H), pygame.FULLSCREEN)
    pygame.display.set_caption('Boats and Bombs!')

    # Objects
    player_boat = Boat('Player Boat', "/home/yoichann/boats-and-bombs/boat.png", (0, 0))
    p1 = Player('Bingus', player_boat)
    town = Town('Walterville', 3, 350, 220)
    status = Label('Status', font_large, str(f"X: {p1.boat.pos_x}, Y: {p1.boat.pos_y}\nSupplies: {p1.boat.supply}"), 600, 600)

    # Drawing Table
    drawable = [player_boat, town]


    # Game Loop
    
    running = True

    while running:

        screen.fill(constants.SCREEN_COLOR)
        status.draw(screen)

        for item in drawable:
            item.draw(screen)



        # PyGame EXIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            sys.exit()



        # Collision Test
        if p1.boat.hitbox.colliderect(town.hitbox):
            print('boat has entered town!')
            p1.boat.supply += town.supply_bonus
            ui = pygame.draw.rect(screen, (35, 35, 35), [0, 0, screen.get_width(), 200], 0) 
        
        #status.text = f"X: {p1.boat.pos_x}, Y: {p1.boat.pos_y}\nSupplies: {p1.boat.supply}"
        status = Label('Status', font_large, str(f"X: {p1.boat.pos_x}, Y: {p1.boat.pos_y}\nSupplies: {p1.boat.supply}"), 600, 600)

        


        

        # Display Flip
        #print(f"boat is at: {x} {y}")
        pygame.display.update()
        


        # Clock 
        dt = clock.tick(constants.FRAMERATE) / 1000
        #print("Delta: " + dt)


if __name__ == "__main__":
    main()
