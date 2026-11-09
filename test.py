class Kaart:
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
