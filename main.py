import pygame
import random

# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


wall_list = []
for i in range(5):
    x = random.randrange(50, 500)
    y = random.randrange(50, 500)
    width = random.randrange(20, 150)
    height = random.randrange(20, 150)
    if width > height:
        height == 20
        width == 150
    elif height > width:
        width == 20
        height == 150
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
        
    
    def go_left(self):
        self.change_x = -3
    
    def go_right(self):
        self.change_x = 3
    
    def go_up(self):
        self.change_y = -3
    
    def go_down(self):
        self.change_y = 3

    def update(self):
        self.player_x += self.change_x

        self.player_y += self.change_y

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def stop_at_border(self):
        if self.player_x >= 730:
            self.player_x = 730
        elif self.player_x <= 70:
            self.player_x = 70
        elif self.player_y >= 730:
            self.player_y = 730
        elif self.player_y <= 70:
            self.player_y = 70

    def stop_at_walls(self):
        for i in range(len(wall_list)):
            if wall_list.x[i] == self.player_x + self.player_width or wall_list.x[i] + wall_list.width[i] == self.player_x:
                self.player_x = 200
            


    def draw_player(self, screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [self.player_x, self.player_y, self.player_width, self.player_height])

def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (800, 800)
    screen = pygame.display.set_mode(size)

    # Create player
    player = Player()

    # Make borders
    def make_border():
        # Borders
        # Top side horizontal
        pygame.draw.rect(screen, GREY, [50, 50, 700, 20])
        # Right side vertical
        pygame.draw.rect(screen, GREY, [50, 50, 20, 700])
        # Bottom side horizontal
        pygame.draw.rect(screen, GREY, [50, 750, 700, 20])
        # Right side vertical
        pygame.draw.rect(screen, GREY, [750, 50, 20, 720])

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # loop until user clicks the close button
    done = False
    while not done:
        # EVENT STUFF
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_UP:
                    player.go_up()
                elif event.key == pygame.K_DOWN:
                    player.go_down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.stop()

        # LOGIC STUFF 
        player.update()
        player.stop_at_border()

        # DRAW STUFF

        # Player
        player.draw_player(screen)
        # Draw rectangles in rectangle list
        for i in range(len(wall_list)):
            pygame.draw.rect(screen, GREY, wall_list[i])
        # Borders
        make_border()

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


