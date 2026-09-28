import random
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
 10, 10, 10, 10, 10, 10, 10,
 11, 11, 11, 11, 11
 ]

stapel = 0

speler1 = [0, 0, 0, 0]
speler2 = [0, 0, 0, 0]




def spelregelUitleg():
    print("uitleg")


def pakken():
    gepakteKaart = kaart[random.randint(0, (len(kaart)) - 1) ]
    kaart.remove(gepakteKaart)
    return gepakteKaart


def vervangen(kaartInSpel):
    a = input("Wil je de kaart ruilen? \n[1], [2], [3], [4] of [n]iet")
    if a == "n":
        return kaartInSpel
    else:
        oudeKaart = speler1[a] 
        speler1[a] = kaartInSpel()
        return oudeKaart
           
def spieken():
    a = input("Welke kaart wil je spieken? \n [1], [2], [3], [4]")
    if a == 1:
        spiek = f"{speler1[0]} | * | * | * "
    elif a == 2:
        spiek = f"* | {speler1[1]} | * | * "
    elif a == 3:
        spiek = f"* | * | {speler1[2]} | * "
    elif a == 4:
        spiek = f"* | * | * | {speler1[3]} "
    return spiek

#Kaart ruilen

    # Vraag aan de speler welke hij van zijn eigen kaarten wilt ruilen
    # Vraag aan de speler van welke speler hij de kaart wilt ruilen
    # Vraag welke positie hij wilt ruilen.
def ruilen():
    speler = input("Welke speler wil je ruilen? \n Speler [1]?")
    kaartSpeler = input(f"Welke kaart wil je ruilen van speler {a}? \n [1], [2], [3], [4]")
    eigenKaart = input(f"Welke eigen kaart wil je ruilen voor kaart {b} van speler {a}?")

    if speler == 1:
        a = speler2[kaartSpeler]
        speler2[kaartSpeler] = speler1[eigenKaart]
        speler1[eigenKaart] = a
        return True
    

def laatsteBeurt():
    ai()
    somSpeler = speler1[0] + speler1[1] + speler1[2] + speler1[3]
    somComputer = speler2[0] + speler2[1] + speler2 [2] + speler2[3]
    print(f"Jouw kaarten: {speler1}, kaarten van de computer: {speler2}")
    print(f"Jouw score is: {somSpeler}, de score van de computer is {somComputer}")
    if somSpeler == somComputer:
        print("Jullie hebben gelijk gespeeld")
    elif somSpeler < somComputer:
        print("De computer heeft gewonnen")
    else:
        print("Gefeliciteerd! jij hebt gewonnen!")



