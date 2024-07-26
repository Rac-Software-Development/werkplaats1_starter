import pygame

pygame.init()
GAME_SPEED = 60
LOGO_START_SPEED = 3
LOGO_MAX_SPEED = 9
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BUTTON_PUSH_WAIT = 100
# Kleuren worden aangeven met een tuple van 3 getallen - rood, groen, blauw - tussen 0 en 255.
# 0, 0, 0 betekend geen kleurm, dus zwart.
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Werkplaats 1: PyGame")

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

logo_speed = LOGO_START_SPEED
x_direction = 1
y_direction = 1
button_push_timer = 0


def is_halt_requested():
    """
    Deze functie controleert of de gebruiker het programma wilt stoppen.
    """
    should_halt = False

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        should_halt = True
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop. Bijvoorbeeld, of er op het exit kruis is gedrukt.
    # Let op! De .get() methode haalt de lijst leeg.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_halt = True
            break
    return should_halt


def get_new_speed():
    """
    Deze functie controleert of de gebruiker de snelheid van het logo wilt aanpassen door op
    de pijltjestoetsen te drukken. De snelheid kan niet onder 1 of boven LOGO_MAX
    """

    new_logo_speed = logo_speed
    # Wil je in een functie een globale variable aanpassen dan moeten we dat expliciet aangeven.
    global button_push_timer
    if button_push_timer <= pygame.time.get_ticks():
        if pygame.key.get_pressed()[pygame.K_LEFT] and logo_speed > 1:
            new_logo_speed = logo_speed - 1
        if pygame.key.get_pressed()[pygame.K_RIGHT] and logo_speed < LOGO_MAX_SPEED:
            new_logo_speed = logo_speed + 1
        button_push_timer = pygame.time.get_ticks() + BUTTON_PUSH_WAIT
    return new_logo_speed


def get_direction_change(
    current_x_direction,
    current_y_direction,
    position_rect,
    screen_boundary_x,
    screen_boundary_y,
):
    """
    Deze functie controleert of het logo de rand van het scherm raakt en verandert de richting
    """
    new_x_direction = current_x_direction
    new_y_direction = current_y_direction
    # Linkerkant van het scherm geraakt?
    if position_rect.left <= 0:
        new_x_direction = 1
    # Rechterkant van het scherm geraakt?
    elif position_rect.right >= screen_boundary_x:
        new_x_direction = -1
    # Bovenkant van het scherm geraakt?
    if position_rect.top <= 0:
        new_y_direction = 1
    # Onderkant van het scherm geraakt?
    elif position_rect.bottom >= screen_boundary_y:
        new_y_direction = -1
    return new_x_direction, new_y_direction


logo = pygame.image.load("images/ra_logo.png").convert_alpha()
# Geeft een rect object terug met de grootte van het logo, en de locatie (0, 0)
logo_rect = logo.get_rect()

# Dit is de "game loop"
while True:
    halt_requested = is_halt_requested()
    if halt_requested:
        break

    logo_speed = get_new_speed()
    x_direction, y_direction = get_direction_change(
        current_x_direction=x_direction,
        current_y_direction=y_direction,
        position_rect=logo_rect,
        screen_boundary_x=SCREEN_WIDTH,
        screen_boundary_y=SCREEN_HEIGHT,
    )
    logo_coordinate_change = [x_direction * logo_speed, y_direction * logo_speed]
    # Met de nieuwe snelheid verplaatsen we de locatie van het logo
    # https://www.pygame.org/docs/ref/rect.html
    logo_rect.move_ip(logo_coordinate_change)
    canvas.fill(BACKGROUND_COLOR)
    canvas.blit(logo, logo_rect)
    pygame.display.flip()
    clock.tick(GAME_SPEED)

print("Game over!")
