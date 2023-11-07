import pygame

# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Wall Class
class Wall():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_wall(self, screen):
        pygame.draw.rect(screen, GREY, [self.x, self.y, self.width, self.height])
        
# Player Class
class Player():
    def __init__(self, x, y, width, height, change_x, change_y):
        # Class attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # player's speed and direction / vector
        self.change_x = change_x
        self.change_y = change_y
        
    
    def go_left(self):
        self.change_x = -3
    
    def go_right(self):
        self.change_x = 3
    
    def go_up(self):
        self.change_y = -3
    
    def go_down(self):
        self.change_y = 3

    def update(self):
        self.x += self.change_x

        self.y += self.change_y

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def return_to_start(self):
        self.x = 200
        self.y = 380
        self.change_x = 0
        self.change_y = 0

    def draw_player(self, screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height])

def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    # Create player
    player = Player(200, 380, 20, 20, 0, 0)

    # Make wall list
    wall_list = []


    # append walls into list
    # Border walls
    wall_list.append(Wall(50, 50, 700, 20))
    wall_list.append(Wall(50, 50, 20, 700))
    wall_list.append(Wall(50, 750, 700, 20))
    wall_list.append(Wall(750, 50, 20, 720))
    wall_list.append(Wall(140, 200, 150, 20))
    wall_list.append(Wall(140, 600, 150, 20))
    wall_list.append(Wall(350, 250, 20, 300))
    wall_list.append(Wall(400, 70, 20, 200))
    wall_list.append(Wall(600, 300, 120, 20))
    wall_list.append(Wall(500, 600, 250, 20))

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
        for i in range(len(wall_list)):
            if player.x < wall_list[i].x + wall_list[i].width and player.y < wall_list[i].y + wall_list[i].height and player.x + player.width > wall_list[i].x and player.y + player.height > wall_list[i].y:
                player.return_to_start()
                

        # Draw Stuff

        # Player
        player.draw_player(screen)
        # Walls
        for i in range(len(wall_list)):
            wall_list[i].draw_wall(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


