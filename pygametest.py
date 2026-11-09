import pygame
import random
import os
import time

pygame.init()

screen = pygame.display.set_mode((900, 600))
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Beverbende")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (50, 150, 80)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

deck = [
    0, 0, 0, 0,
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9, 9, 9, 9, 9, 9,
    10, 10, 10, 10, 10, 10, 10,  # ruilen
    11, 11, 11, 11, 11  # spieken
]

beurtPlayer = True
gameActive = False

speler1 = [0, 0, 0, 0]
speler2 = [0, 0, 0, 0]


def pakken():
    gepakteKaart = deck[random.randint(0, (len(deck)) - 1)]
    deck.remove(gepakteKaart)
    return gepakteKaart


def uitdelen():
    for x in range(len(speler1)):
        speler1[x] = pakken()
    for x in range(len(speler2)):
        speler2[x] = pakken()


kaartKnoppen = []   # de kaarten die op het scherm moeten staan

timerUitdelen = None


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


class Pot:
    def __init__(self, x=405, y=255, breedte=90, hoogte=126):
        self.rect = pygame.Rect(x, y, breedte, hoogte)

    def tekenen(self):
        kleur = GRAY if self.rect.collidepoint(
            pygame.mouse.get_pos()) else WHITE
        pygame.draw.rect(screen, kleur, self.rect)
        text = font.render(str(potWaarde), True, BLACK)
        screen.blit(text, text.get_rect(center=self.rect.center))

    def verwerk_event(self, event):
        global potWaarde
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                potWaarde = pakken()


class kaartSpeler:
    def __init__(self, speler, positie, hidden):
        self.speler = speler
        self.positie = positie
        self.hidden = hidden
        if speler == 1:
            self.waarde = speler1[positie]
        elif speler == 2:
            self.waarde = speler2[positie]
        breedte = 90
        hoogte = 126
        if speler == 1:
            y = 440
        elif speler == 2:
            y = 20

        if positie == 0:
            x = 220
        elif positie == 1:
            x = 340
        elif positie == 2:
            x = 460
        elif positie == 3:
            x = 580
        self.rect = pygame.Rect(x, y, breedte, hoogte)

    def tekenen(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            kleur = GRAY
        else:
            kleur = WHITE
        pygame.draw.rect(screen, kleur, self.rect)
        if not self.hidden:
            text = font.render(str(self.waarde), True, BLACK)
            screen.blit(text, text.get_rect(center=self.rect.center))


potWaarde = None
potRect = pygame.Rect(405, 300, 90, 126)


def tekenPot():
    rect = pygame.Rect(405, 300, 90, 126)   # 405 = gecentreerd
    kleur = GRAY if rect.collidepoint(pygame.mouse.get_pos()) else WHITE
    pygame.draw.rect(screen, kleur, rect)
    text = font.render(str(potWaarde), True, BLACK)
    screen.blit(text, text.get_rect(center=rect.center))


start = False


def startGame():
    global start
    start = True


uitdeel_knop = Knop("Start", startGame, 375, 270)
knoppen = [uitdeel_knop]
pot = Pot()
uitdelen()
running = True
while running:

    # 1. EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for knop in knoppen:
            knop.verwerk_event(event)
        pot.verwerk_event(event)

    # 2. TEKENEN
    screen.fill(GREEN)
    if potWaarde is not None:
        pot.tekenen()
    for knop in knoppen:
        knop.tekenen()
    for knop in kaartKnoppen:
        knop.tekenen()
    if start:
        knoppen.remove(uitdeel_knop)
        for positie in range(len(speler1)):
            if positie == 1 or positie == 2:
                # Kaarten van de speler op positie 2 en 3. Verbergen.
                kaart = kaartSpeler(1, positie, True)
                kaartKnoppen.append(kaart)
            else:
                # Kaarten van de speler op posititie 1 en 4. Laten zien
                kaart = kaartSpeler(1, positie, False)
                kaartKnoppen.append(kaart)
        for positie in range(len(speler2)):
            # Kaarten van de computer op alle posities. verbergen
            kaart = kaartSpeler(2, positie, True)
            kaartKnoppen.append(kaart)
            timerUitdelen = pygame.time.get_ticks()
        start = False
        potWaarde = pakken()
    if timerUitdelen is not None and pygame.time.get_ticks() - timerUitdelen >= 2000:
        for positie in range(len(speler1)):
            # Kaarten van de speler verbergen.
            kaart = kaartSpeler(1, positie, True)
            kaartKnoppen.append(kaart)
        timerUitdelen = None

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

pygame.display.flip()
clock.tick(60)

pygame.quit()
