import pygame
import Menu
import random

pygame.init()

# búa til leik
width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pygame.display.set_caption("Spooky Scary Slytherins")
clock = pygame.time.Clock()
FPS = 30

# afmarkað svæði
levels = []
levels.append([((50, 50), (50, height - 50), 10),
               ((50, height - 50),(int(width/2) - 25,height - 50), 10),
               ((int(width/2) + 25, height - 50), (width - 50, height - 50), 10),
               ((50, 50), (width - 50, 50), 10),
               ((width - 50, 50), (width - 50, height - 50), 10)])

# búa til snák
link = pygame.image.load("link.png")
head = pygame.image.load("head.png")
apple = pygame.image.load("apple.png")
apple_size = 30
apple = pygame.transform.scale(apple, (apple_size,apple_size))
                          
linkwidth = 40
linkheight = 25
x = width/2
y = height/2
xmove = 0
ymove = 0
movespeed = 10
snakeLength = 8
snakeElasticity = 3
headsBeen = []
time = 0
points = 0

rand1 = round(random.randrange(0,width-apple_size))
rand2 = round(random.randint(0,height-apple_size))

for i in range(snakeElasticity):
    headsBeen.append((x,y))

def wallDetector(level, coords):
    for wall in level:
        #rint(coords[1])
        if (wall[0][0] - 5 <= coords[0] <= wall[1][0] + 5) and (wall[0][1] - 5 <= coords[1] <= wall[1][1] + 5):
            print("CRASH!")
            return True
    return False

def changeApple():
    rand1 = round(random.randrange(0,width-apple_size))
    rand2 = round(random.randint(0,height-apple_size))
    return (rand1, rand2)

def drawApple(random1, random2):
    gameDisplay.blit(apple, (400.0,300.0))

def drawSnake(x, y):
    gameDisplay.blit(head, (x, y))
    for part in range(snakeLength):
        gameDisplay.blit(link, headsBeen[max(time-part*snakeElasticity, 0)])

def checkEat(level, snake, apple):
    if snake == apple:
        points += 105
        rect = rect.move((rand1, rand2))
        drawSnake(rand1, rand2)
        print(points)
        return True
    return False


#Control scheme set to arrow keys and WASD
left = [pygame.K_LEFT, pygame.K_a]
right = [pygame.K_RIGHT, pygame.K_d]
up = [pygame.K_UP, pygame.K_w]
down = [pygame.K_DOWN, pygame.K_s]

#Menu.Menu()
level = levels[0]
exit = False
    
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key in left:
                xmove = -movespeed
                ymove = 0
            if event.key in right:
                xmove = movespeed
                ymove = 0
            if event.key in up:
                ymove = -movespeed
                xmove = 0
            if event.key in down:
                ymove = movespeed
                xmove = 0
                
    x = x + xmove
    y = y + ymove
    if x < 0:
        x = 0
        xmove = 0
    if  x > width - linkwidth:
        x = width - linkwidth
        xmove = 0
    if y < 0:
        y = 0
        ymove = 0
    if y > height - linkheight:
        y = height - linkheight
        ymove = 0
        
    gameDisplay.fill(white)
    
    for wall in level:
        pygame.draw.line(gameDisplay, black, wall[0], wall[1], wall[2])
        
    if wallDetector(level, (x,y)):
        xmove = 0
        ymove = 0

    if checkEat(level, (x,y), (rand1, rand2)):
        print('apple was eaten')
        
    headsBeen.append((x, y))
    drawApple(rand1, rand2)
    
    drawSnake(x, y)
    pygame.display.update()
    time += 1
    clock.tick(FPS)


    
pygame.quit()
quit()

