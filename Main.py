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
FPS = 60

link = pygame.image.load("link.png")
linkwidth = 40
linkheight = 25

x = width/2
y = height/2
xmove = 0
ymove = 0
movespeed = 8



exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xmove = -movespeed
                ymove = 0
            if event.key == pygame.K_RIGHT:
                xmove = movespeed
                ymove = 0
            if event.key == pygame.K_UP:
                ymove = -movespeed
                xmove = 0
            if event.key == pygame.K_DOWN:
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
    gameDisplay.blit(link, (x, y))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()