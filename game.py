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


def quit_game_requested():
    halting = False
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting


def bounce_if_required(speed_tuple, position_rect):
    # Linkerkant van het scherm geraakt?
    if position_rect.left <= 0:
        speed_tuple[0] = LOGO_SPEED
    # Rechterkant van het scherm geraakt?
    elif position_rect.right >= SCREEN_WIDTH:
        speed_tuple[0] = -LOGO_SPEED

    # Bovenkant van het scherm geraakt?
    if position_rect.top <= 0:
        speed_tuple[1] = LOGO_SPEED
    # Onderkant van het scherm geraakt?
    elif position_rect.bottom >= SCREEN_HEIGHT:
        speed_tuple[1] = -LOGO_SPEED


# Hier wordt het logo ingeladen. In principe gebeurt er nu nog niets mee en
# staat het logo niet op het scherm
logo = pygame.image.load("images/ra_logo.png").convert_alpha()
logo_rect = logo.get_rect()


# De "snelheid" is het aantal pixels dat het logo per frame verplaatst,
# per loop. De eerste waarde geeft de horizontale snelheid aan, de
# tweede de verticale.
# Dus:
# [1, 1] betekend 1 pixel naar rechts en 1 pixel naar beneden.
# [-1, 1] betekend 1 pixel naar links en 1 pixel naar beneden.
# [-1, -1] betekend 1 pixel naar links en 1 pixel naar boven.
# [1, -1] betekend 1 pixel naar rechts en 1 pixel naar boven.
logo_speed = [LOGO_SPEED, LOGO_SPEED]

# Dit is de "game loop"
while not quit_game_requested():
    # Eerst wissen we alles als voorbereiding van deze "tick"
    canvas.fill(BACKGROUND_COLOR)

    # We passen de snelheid van het logo aan zodat die niet buiten het scherm gaat.
    # Let op! We passen hier de inhoud van de logo_speed lijst aan!
    bounce_if_required(logo_speed, logo_rect)

    # Met de nieuwe snelheid verplaatsen we de locatie van het logo
    # https://www.pygame.org/docs/ref/rect.html
    logo_rect = logo_rect.move(logo_speed)

    # Nu alles verplaatst is blitten we het logo op de achtergrond met de nieuwe locatie
    canvas.blit(logo, logo_rect)

    # ...en tonen we het scherm
    pygame.display.flip()

    # Daarna wachten we tot de volgende "tick" van de klok
    clock.tick(GAME_SPEED)

print("Game over!")
