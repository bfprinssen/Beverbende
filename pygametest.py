import pygame
import random

pygame.init()

screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Beverbende")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (50, 150, 80)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# --- Spelgegevens ---
deck = []
speler1 = []   # begint leeg: pas na een klik op "Uitdelen" krijg je kaarten
speler2 = []


def maak_deck():
    nieuw = []
    for waarde in range(0, 9):      # 0 t/m 8: elk 4 keer
        nieuw += [waarde] * 4
    nieuw += [9] * 9
    nieuw += [10] * 7               # ruilen
    nieuw += [11] * 5               # spieken
    random.shuffle(nieuw)
    return nieuw


def uitdelen():
    # [:] past de bestaande lijst aan, zodat je geen 'global' nodig hebt
    deck[:] = maak_deck()
    speler1[:] = [deck.pop() for _ in range(4)]
    speler2[:] = [deck.pop() for _ in range(4)]


def kaartMaken(pos, waarde, user):
    x = 200 + pos * 120             # pos is 0, 1, 2, 3
    y = 400 if user else 50

    pygame.draw.rect(screen, WHITE, (x, y, 100, 150))
    text = font.render(str(waarde), True, BLACK)
    text_rect = text.get_rect(center=(x + 100 / 2, y + 150 / 2))
    screen.blit(text, text_rect)


class Knop:
    def __init__(self, naam, function, x, y, breedte=150, hoogte=60):
        self.naam = naam
        self.function = function
        self.rect = pygame.Rect(x, y, breedte, hoogte)

    def tekenen(self):
        kleur = GRAY if self.rect.collidepoint(
            pygame.mouse.get_pos()) else WHITE
        pygame.draw.rect(screen, kleur, self.rect)
        text = font.render(self.naam, True, BLACK)
        screen.blit(text, text.get_rect(center=self.rect.center))

    def verwerk_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.function()


# Let op: uitdelen ZONDER haakjes
uitdeel_knop = Knop("Uitdelen", uitdelen, 375, 270)

running = True
while running:

    # 1. EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        uitdeel_knop.verwerk_event(event)

    # 2. TEKENEN
    screen.fill(GREEN)

    for pos, waarde in enumerate(speler1):
        kaartMaken(pos, waarde, True)
    for pos, waarde in enumerate(speler2):
        kaartMaken(pos, waarde, False)

    uitdeel_knop.tekenen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
