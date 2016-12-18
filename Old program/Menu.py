#pygame.draw.line(gameDisplay, black, (50, 50), (50, height - 50), 10)
#pygame.draw.line(gameDisplay, black, (int(width/2) - 25,height - 50), (50, height - 50), 10)
#pygame.draw.line(gameDisplay, black, (int(width/2) + 25, height - 50), (width - 50, height - 50), 10)
#pygame.draw.line(gameDisplay, black, (50, 50), (width - 50, 50), 10)
#pygame.draw.line(gameDisplay, black, (width - 50, 50), (width - 50, height - 50), 10)
import pygame
pygame.init()

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
green = (0,255,0)
black = (0,0,0)
white = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60
def Menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        gameDisplay.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 67)
        text = font.render("Spooky Scary Slitherins", 1, black)
        gameDisplay.blit(text, (width / 2 - 400, height / 2 - 120))

        if width / 2 - 50 < mouse[0] < width / 2 + 50 and height / 2 + 60 < mouse[1] < height / 2 + 120:
            pygame.draw.rect(gameDisplay, (0, 200, 0), (width / 2 - 50, height / 2 + 60, 100, 60))
            if pygame.mouse.get_pressed()[0] == 1:
                menu = False
        else:
            pygame.draw.rect(gameDisplay, green, (width / 2 - 50, height / 2 + 60, 100, 60))
        pygame.display.update()
        clock.tick(FPS)