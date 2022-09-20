import pygame

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
pygame.display.set_caption("Werkplaats 1: PyGame")
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
halt_game = False
while not halt_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halt_game = True
    pygame.display.flip()
    clock.tick(60)
