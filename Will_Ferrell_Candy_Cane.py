import os
import random
import pygame
pygame.init()
pygame.font.init()

play_song = False
notquit = True
running = True
pause = False
time_over = False


timer = 120
frame_count = 0
levels = []
level = []

count_p1 = 0
count_p2 = 0

myndGameOver = pygame.image.load('images/gameover.jpg')
myndWall = pygame.image.load('images/wall+santa.png')
myndCandy = pygame.image.load('images/candy.png')
myndFrame = pygame.image.load('images/frame.jpg')
myndSnow = pygame.image.load('images/snowflake.png')
myndStart = pygame.image.load('images/start_screen.jpg')
elfMynd = pygame.image.load('images/elf.png')
managerMynd = pygame.image.load('images/manager.png')
pauseMynd = pygame.image.load('images/pause/pause_screen.jpg')


red = (255, 0, 0)
score_font = pygame.font.Font( None, 32)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Will Ferrell gets the candy cane!!")
screen = pygame.display.set_mode((1280, 960),pygame.FULLSCREEN)
clock = pygame.time.Clock()
walls = []
snows = []
p1name = "Will"
p2name = "Ferrell"

class Player(object):
    name = ""
    def __init__(self):
        self.rect = pygame.Rect(random.randint(1, 39)*32, random.randint(1,49)*32,32,32)
        self.spawn()

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
    def spawn(self):
        self.rect.x = random.randint(2, 38)*32
        self.rect.y = random.randint(2, 28)*32

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

class Candy(object):
    def __init__(self):
        self.rect = pygame.Rect(320, 320, 32, 32)
        self.move()
        
    def move(self):
        self.rect.x = random.randint(2, 38)*32
        self.rect.y = random.randint(2, 28)*32
        
class Snow(object):
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, 1280), random.randint(0,960),0,0)
        self.move()
        
    def move(self):
        self.rect.y += random.randint(0, 4)
        if self.rect.y > 960:
            self.rect.y = 0

class Wall(object):
    def __init__(self, pos):
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

def load_levels():
    global levels, level
    levels = []
    levels.append([
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W",
    "W W                                W W W",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",#5
    "W W                              W W W W",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W                          W W   W W W W",
    "WWWWW WWWWWWWWWWWWWWWWWWWW W W W W W W W",
    "W     W                  W W W W W W W W",#10
    "W WWWWWWWWWWWWWWWWWWWWWW W     W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",#15
    "W                            W W W W   W",
    "W                            W W W WWW W",
    "W                            W   W     W",
    "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W",
    "W                                      W",#20
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  W W W",
    "W W                                W W W",
    "W W WWWWWWWWWWWWWWWWW WWWWWWWWWWWW W W W",
    "W W                              W W W W",
    "W W WWWWWWWWWW WWWWWWWWWWWWWWWWWWW W W W",#25
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    ])
    levels.append([
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",
    "W                                      W",
    "W       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                WWWWWWW",#5
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWWW",
    "W                                WWWWWWW",
    "W                                WWWWWWW",
    "WW WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",#10
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",#15
    "W                            W W W W   W",
    "W                            W W W WWW W",
    "W                            W   W     W",
    "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                 WWWWWW",#20
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWW",
    "W W                               WWWWWW",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W W                              WWWWWWW",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",#25
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    ])
    levels.append([
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",
    "W                                      W",
    "W       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                WWWWWWW",#5
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWWW",
    "W                                WWWWWWW",
    "W                                WWWWWWW",
    "W                                     WW",
    "W                                      W",#10
    "W  WWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",
    "W                            W W W W W W",#15
    "W                            W W W W W W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",
    "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                 WWWWWW",#20
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W W                               WWWWWW",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W W                              WWWWWWW",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",#25
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "W                              WWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    ])
    level = []
    level = levels[random.randint(0, len(levels)-1)]

def music():
    pygame.mixer.music.load('songs/jol.ogg')
    pygame.mixer.music.play(-1)

def changeName(i):
    changing = True
    global p1name, p2name
    if i == 1:
        name = p1name
    else:
        name = p2name
    while changing:
        screen.fill((0, 0, 0))
        screen.blit(myndFrame, (0, 0))
        screen.blit(score_font.render(name, 1, red), (80, 60))
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                changing = False
                if i == 1:
                    p1name = name
                else:
                    p2name = name
            elif e.type == pygame.KEYDOWN:
                if e.key == 303 or e.key == 304:
                    continue
                elif (pygame.key.get_pressed()[303] != 0) or (pygame.key.get_pressed()[304] != 0):
                    name = name + str.upper(pygame.key.name(e.key))
                elif (pygame.key.get_pressed()[32] != 0):
                    name = name + " "
                else:
                    name = name + pygame.key.name(e.key)

def start_screen():
    global running, notquit, screen
    running = False
    while not running:
        screen.fill((0, 0, 0))
        screen.blit(myndStart,(0,0))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
                notquit = False
                return 0
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                running = True
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_1 or e.key == pygame.K_2):
                if e.key == pygame.K_1:
                    changeName(1)
                else:
                    changeName(2)

                
def lose_screen(count_p1, count_p2):
    global running, notquit, screen
    screen.fill((0, 0, 0))
    screen.blit(myndGameOver,(0,0))
    screen.blit(score_font.render(p1name + ": " + str(count_p1) , 1, red),(640,500))
    screen.blit(score_font.render(p2name + ": " +  str(count_p2) , 1, red),(640,600))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
            notquit = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            running = False

def pause_screen():
    global running, notquit, screen
    running = False
    while not running:
        screen.fill((0, 0, 0))
        screen.blit(pauseMynd,(0,0))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
                notquit = False
                return 0
            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                running = True


def main():
    
    global screen,walls,notquit,lose,running, count_p1, count_p2, play_song, timer, frame_count, snows, pause, levels
    
    if not play_song:
        music()
        play_song = True
        
    start_screen()
    
    player = Player()
    player2 = Player()

    load_levels()

    x = y = 0
    count_p1 = 0
    count_p2 = 0
    snows = []
    walls = []
    for i in range(0,1500):
        snows.append(Snow())
    for row in level:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))
            x += 32
        y += 32
        x = 0
    candy_rect = Candy()
    

    while running:
        
        frame_count += 1
        if frame_count % 15 == 0:
            timer -= 1
        
        clock.tick(15)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                notquit = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
                not_quit = False
                
        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        speed = 32

        if key[pygame.K_LEFT]:
            player.move(-speed, 0)
        if key[pygame.K_RIGHT]:
            player.move(speed, 0)
        if key[pygame.K_UP]:
            player.move(0, -speed)
        if key[pygame.K_DOWN]:
            player.move(0, speed)
            
        if key[pygame.K_a]:
            player2.move(-speed, 0)
        if key[pygame.K_d]:
            player2.move(speed, 0)
        if key[pygame.K_w]:
            player2.move(0, -speed)
        if key[pygame.K_s]:
            player2.move(0, speed)

        if key[pygame.K_p] and not pause :
            pause_screen()
            pause = True
        elif pause:
            pause = False
            

        if player.rect.colliderect(candy_rect):
            count_p1 += 1
            candy_rect.move()
        if player2.rect.colliderect(candy_rect):
            count_p2 += 1
            candy_rect.move()
            
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            screen.blit(myndWall,wall.rect)
            if wall.rect.colliderect(candy_rect):
                candy_rect.move()
            if wall.rect.colliderect(player):
                player.spawn()
            if wall.rect.colliderect(player2):
                player2.spawn()
        for snow in snows:
            screen.blit(myndSnow,snow.rect)
            snow.move()
        screen.blit(elfMynd, player.rect)
        screen.blit(managerMynd, player2.rect)
        screen.blit(myndCandy, candy_rect)
        screen.blit(myndFrame, (995,803))
        screen.blit(score_font.render(p1name + ": " +  str(count_p1) , 1, red),(1100,830))
        screen.blit(score_font.render(p2name + ": " + str(count_p2) , 1, red),(1100,870))
        screen.blit(score_font.render("T: %s" % timer , 1, red),(1100,910))
        pygame.display.flip()
        if timer == 0:
            running = False
            not_quit = False


    running = True
    play_song=True

    while running and notquit:
        timer = 120
        lose_screen(count_p1,count_p2)
        
while notquit:
    main()

pygame.quit()
