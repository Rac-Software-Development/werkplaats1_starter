import pygame

pygame.init()
GAME_SPEED = 60
LOGO_SPEED = 3
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# Kleuren worden aangeven met een tuple van 3 getallen - rood, groen, blauw - tussen 0 en 255.
# 0, 0, 0 betekend geen kleurm, dus zwart.
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Werkplaats 1: PyGame")


clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def handle_events():
    halting = False
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop. Hier komen ook de toetsaanslagen
    # in te staan. Let op! De .get() methode haalt de lijst leeg.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                halting = True
                break
    return halting


def get_new_speed_directions(
    current_speed, position_rect, screen_boundary_x, screen_boundary_y
):
    speed_x, speed_y = current_speed
    # Linkerkant van het scherm geraakt?
    if position_rect.left <= 0:
        speed_x = LOGO_SPEED
    # Rechterkant van het scherm geraakt?
    elif position_rect.right >= screen_boundary_x:
        speed_x = -LOGO_SPEED

    # Bovenkant van het scherm geraakt?
    if position_rect.top <= 0:
        speed_y = LOGO_SPEED
    # Onderkant van het scherm geraakt?
    elif position_rect.bottom >= screen_boundary_y:
        speed_y = -LOGO_SPEED
    return [speed_x, speed_y]


logo = pygame.image.load("images/ra_logo.png").convert_alpha()
logo_rect = logo.get_rect()
logo_speed = [LOGO_SPEED, LOGO_SPEED]

# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    canvas.fill(BACKGROUND_COLOR)
    logo_speed = get_new_speed_directions(
        current_speed=logo_speed,
        position_rect=logo_rect,
        screen_boundary_x=SCREEN_WIDTH,
        screen_boundary_y=SCREEN_HEIGHT,
    )
    # Met de nieuwe snelheid verplaatsen we de locatie van het logo
    # https://www.pygame.org/docs/ref/rect.html
    logo_rect.move_ip(logo_speed)
    canvas.blit(logo, logo_rect)
    pygame.display.flip()
    clock.tick(GAME_SPEED)

print("Game over!")
