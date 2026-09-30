import random
import os
import time
# Stock kaarten 
# 0 tot 8 = 4x in het spel
# 9 = 9x in het spel
# ruilkaart = 9x in het spel
# kijkkaart = 7x in het spel

kaart = [
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
 10, 10, 10, 10, 10, 10, 10, #ruilen
 11, 11, 11, 11, 11 #spieken
 ]

def pakken():
    gepakteKaart = kaart[random.randint(0, (len(kaart)) - 1) ]
    kaart.remove(gepakteKaart)
    return gepakteKaart

stapel = pakken()

speler1 = [0, 0, 0, 0]
speler2 = [0, 0, 0, 0]

gameActive = False


def spelregelUitleg():
    print("uitleg")


def vervangen(kaartInSpel):
    a = input("Wil je de kaart ruilen? \n[1], [2], [3], [4] of [n]iet")
    if a == "n":
        return kaartInSpel
    else:
        a = int(a) - 1
        oudeKaart = speler1[a] 
        speler1[a] = kaartInSpel
        return oudeKaart
           
def spieken():
    a = int(input("Welke kaart wil je spieken? \n [1], [2], [3], [4]"))
    if a == 1:
        spiek = f"{speler1[0]} | * | * | * "
    elif a == 2:
        spiek = f"* | {speler1[1]} | * | * "
    elif a == 3:
        spiek = f"* | * | {speler1[2]} | * "
    elif a == 4:
        spiek = f"* | * | * | {speler1[3]} "
    return spiek


def ruilen():
    speler = int(input("Welke speler wil je ruilen? \n Speler [1]?"))
    kaartSpeler = int(input(f"Welke kaart wil je ruilen van speler {speler}? \n [1], [2], [3], [4]")) + 1
    eigenKaart = int(input(f"Welke eigen kaart wil je ruilen voor kaart {kaartSpeler} van speler {speler}?")) + 1

    if speler == 1:
        a = speler2[kaartSpeler]
        speler2[kaartSpeler] = speler1[eigenKaart]
        speler1[eigenKaart] = a

def uitdelen():
    for x in range(len(speler1)):
        speler1[x] = pakken()
    for x in range(len(speler2)):
        speler2[x] = pakken()

uitdelen()

gameActive = True
print(f"Onthoud deze kaarten goed! {speler1[0]} | * | * | {speler1[3]}")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

while gameActive is True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"De bovenste kaart op de pot is {stapel}")
    mode = input("Wat wil je doen? Wil je [S]toppen, [N]ieuwe kaart trekken of een kaart van de [P]ot pakken?")
    if mode == "N":
        a = pakken()
        if a == 10:
            print(f"Jouw kaart is ruilen")
            if (input("Wil je ruilen?")) == "J":
                ruilen()
            else:
                continue
        elif a == 11:
            print(f"Jouw kaart is spieken")
            print(spieken())
            time.sleep(2)
            continue
        else: 
            print(f"Jouw kaart is {a}")
            stapel = vervangen(int(a))
            continue
    elif mode == "S":
        for x in range(len(speler1)):
            while speler1[x] > 9:
                print("Geen actiekaart in kaarten toegstaan. Pak een nieuwe...")
                speler1[x] = pakken()
        for x in range(len(speler2)):
            while speler2[x] > 9:
                print("Geen actiekaart in kaarten toegstaan. Pak een nieuwe...")
                speler2[x] = pakken()

        somSpeler = speler1[0] + speler1[1] + speler1[2] + speler1[3]
        somComputer = speler2[0] + speler2[1] + speler2 [2] + speler2[3]
        print(f"Jouw kaarten: {speler1}, kaarten van de computer: {speler2}")
        print(f"Jouw score is: {somSpeler}, de score van de computer is {somComputer}")
        if somSpeler == somComputer:
            print("Jullie hebben gelijk gespeeld")
        elif somSpeler > somComputer:
            print("De computer heeft gewonnen")
        else:
            print("Gefeliciteerd! jij hebt gewonnen!")
        gameActive = False
    elif mode == "P":
        stapel = vervangen(stapel)

