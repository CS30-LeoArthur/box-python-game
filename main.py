import pygame
import math
import random

# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (800, 800)
    screen = pygame.display.set_mode(size)

    # Make random wall list
    wall_list = []
    for i in range(5):
        x = random.randrange(50, 500)
        y = random.randrange(50, 500)
        width = random.randrange(20, 100)
        height = random.randrange(100, 200)
        if width > height:
            height == 20
        elif height > width:
            width == 20
        wall_list.append([x, y, width, height])

    # Player
    class Player():
        def __init__(self):
            # Class attributes
            self.player_x = 200
            self.player_y = 380
            self.player_width = 20
            self.player_height = 20
            # player's speed and direction / vector
            self.change_x = 0
            self.change_y = 0


        def move(self):
            self.player_x += self.change_x
            self.player_y += self.change_y
                
        def draw_player(self, screen):
             pygame.draw.rect(screen, RED, [self.player_x, self.player_y, self.player_width, self.player_height])
    # Functions
    def make_border():
        # Borders
        pygame.draw.rect(screen, GREY, [50, 50, 700, 20])
        pygame.draw.rect(screen, GREY, [50, 50, 20, 700])
        pygame.draw.rect(screen, GREY, [50, 750, 700, 20])
        pygame.draw.rect(screen, GREY, [750, 50, 20, 720])

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create player
    the_player = Player()
    # loop until user clicks the close button
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # Drawing code
        screen.fill(WHITE)
        # Player
        the_player.draw_player(screen)

        # Draw rectangles in rectangle list
        for i in range(len(wall_list)):
            pygame.draw.rect(screen, GREY, wall_list[i])

        # Borders
        make_border()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

main()


