import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("Xu ly anh")

clock = pygame.time.Clock()

running = True

BACKGROUND = (214, 214, 214)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

while running:
    clock.tick(60)

    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            running = False

    pygame.display.flip()

pygame.quit()