import pygame

pygame.init()

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

levels = []
levels.append([((50, 50), (50, height - 50), 10),
               ((int(width/2) - 25,height - 50), (50, height - 50), 10),
               ((int(width/2) + 25, height - 50), (width - 50, height - 50), 10),
                ((50, 50), (width - 50, 50), 10),
                ((width - 50, 50), (width - 50, height - 50), 10)])

link = pygame.image.load("link.png")
head = pygame.image.load("head.png")
linkwidth = 40
linkheight = 25
x = width/2
y = height/2
xmove = 0
ymove = 0
movespeed = 8
snake = 20
headsBeen = []
time = 0
snakeElasticity = 4
for i in range(snakeElasticity):
    headsBeen.append((x,y))

def Menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        gameDisplay.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 67)
        text = font.render("Spooky Scary Slitherins", 1, black)
        gameDisplay.blit(text, (width/2 - 400, height/2 - 120))
        pygame.draw.rect(gameDisplay, green, (width/2 - 50, height/2 +60, 100, 60))
        pygame.display.update()
        clock.tick(FPS)

def drawSnake(x, y):
    gameDisplay.blit(head, (x, y))
    #pygame.draw.circle(gameDisplay, green, (int(x), int(y)), 10)
    for part in range(snake):
        #pygame.draw.circle(gameDisplay, black, headsBeen[int(max(time-part*4, 0))], 10)
        gameDisplay.blit(link, headsBeen[max(time-part*snakeElasticity, 0)])

left = [pygame.K_LEFT, pygame.K_a]
right = [pygame.K_RIGHT, pygame.K_d]
up = [pygame.K_UP, pygame.K_w]
down = [pygame.K_DOWN, pygame.K_s]

Menu()
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
    headsBeen.append((x, y))
    drawSnake(x, y)
    pygame.display.update()
    time += 1
    clock.tick(5)
pygame.quit()
quit()

