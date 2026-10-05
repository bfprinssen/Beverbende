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

beurtPlayer = True

def pakken():
    gepakteKaart = kaart[random.randint(0, (len(kaart)) - 1)]
    kaart.remove(gepakteKaart)
    return gepakteKaart


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ____  ________      ________ _____  ____  ______ _   _ _____  ______\n|  _ \\|  ____\\ \\    / /  ____|  __ \\|  _ \\|  ____| \\ | |  __ \\|  ____|\n| |_) | |__   \\ \\  / /| |__  | |__) | |_) | |__  |  \\| | |  | | |__\n|  _ <|  __|   \\ \\/ / |  __| |  _  /|  _ <|  __| | . ` | |  | |  __|\n| |_) | |____   \\  /  | |____| | \\ \\| |_) | |____| |\\  | |__| | |____\n|____/|______|   \\/   |______|_|  \\_\\____/|______|_| \\_|_____/|______|")

gameActive = False

def welkom():
    clearScreen()
    print("Welkom bij beverbende! Tactisch geheugenspel voor het hele gezin.")
    print("Probeer zo min mogelijk strafpunten te verzamelen, maar omdat je maar twee van je vier kaarten kent, is dat niet zo eenvoudig.")
    print("Met de kaarten die je trekt kun je ruilen en acties uitvoeren. Zo weet je steeds meer van je eigen kaarten en die van je tegenstanders.")
    print("Maar dat geldt natuurlijk ook voor de andere spelers!")

def spelregelUitleg():
    uitleg = True
    print("Elke speler heeft 4 gedekte kaarten varierend van 0 t/m 9. Aan het begin van het spel mag je alleen de buitenste 2 kaarten spieken")
    print("Het doel van het spel is zo min mogelijk strafpunten te hebben.")
    while uitleg is True:
        print("Aan het begin van elke beurt heb je 3 opties; Welke regel snap je nog niet?")
        print("[1]Een nieuwe kaart \n[2]Stoppen \n[3]De pot \n[4]Ruilen \n[5]Spieken \n[6]Ik snap het, ik wil beginnen.")
        optie = input("")
        if optie == "1":
            print("Een nieuwe kaart:")
            print("Een nieuwe kaart pakken is een kaart van de stapel pakken. Daarna heb je 1 keuze. \nGa ik deze kaart ruilen voor een van mijn kaarten of niet?")
            print("Wil je nog meer uitleg? \n[1]Ja \n[2]Nee")
            nieuweKaartUitleg = input()
            if nieuweKaartUitleg == "1":
                print("Als je een nieuwe kaart pakt heb je de keuze of je hem wilt ruilen. Het doel van het spel is om zo min mogelijk strafpunten te hebben aan het eind van het spel.")
                print("Bijvoorbeeld: Ik heb op plek 1 een 7 liggen. Ik trek uit de pot een 5. Omdat 5 lager is dan 7, en ik zo weinig mogelijk strafpunten wil hebben ruil ik de 5 met de 7.")
            elif nieuweKaartUitleg == "2":
                uitleg = False
                continue
        elif optie == "2":
            print("Stoppen:")
            print("Als je denkt dat je de laagste strafpunten hebt dan iedereen moet je stoppen.")
            print("Vul 1 in in het menu. Alle spelers na jou mogen nog 1 beurt afmaken. Daarna worden alle kaarten opgeteld. \nDe gene met de laagste strafpunten wint.")
            print("Wil je nog meer uitleg? \n[1]Ja \n[2]Nee \n[3]Ander onderwerp.")
            nieuweKaartUitleg = input()
            if nieuweKaartUitleg == "1":
                print("Een voorbeeld: Ik spieke aan het begin van het spel dat ik op positie 1 en 4 een 0 heb liggen. Na mijn eerste beurt trok ik een 1 uit de stapel. \n Een kaart is voor mij nog onbekend. Maar omdat het zo vroeg in het spel is is het verstandig om gelijk te stoppen.")
                print("De kaarten worden nu geteld. Op de onbekende plek had jij een 6, jouw uiteindelijke score is een 7. Je tegenstander had een 4, 5, 6 en een 9. Zijn score is 24. jij hebt dus gewonnen.")
            elif nieuweKaartUitleg == "2":
                uitleg = False
                continue
        elif optie == "3":
            print("Een kaart van de pot pakken:")
            print("In plaats van een nieuwe kaart pakken kan je ook een kaart van de pot pakken die door een andere speler werd verworpen.")     
        elif optie == "4":
            print("Ruilen: \nJe kan je kaart ruilen met een kaart van een andere speler.\nDit kan je bijvoorbeeld doen als je ziet dat een speler een 0 van de pot pakt.")
        elif optie == "5": 
            print("Spieken: \nJe kan een van je eigen kaart spieken! Handig als je er een bent vergeten.")
        elif optie == "6":
            uitleg = False


def vervangen(kaartInSpel):
    a = input(f"Op welke plek wil je {kaartInSpel} zetten? \n[1], [2], [3], [4] of [0]Niet")
    if a == "0":
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

def stoppen():
    for x in range(len(speler1)):
        while speler1[x] > 9:
            print("Geen actiekaart in kaarten toegestaan. Pak een nieuwe...")
            speler1[x] = pakken()
    for x in range(len(speler2)):
        while speler2[x] > 9:
            print("Geen actiekaart in kaarten toegestaan. Pak een nieuwe...")
            speler2[x] = pakken()

    somSpeler = speler1[0] + speler1[1] + speler1[2] + speler1[3]
    somComputer = speler2[0] + speler2[1] + speler2[2] + speler2[3]
    print(f"Jouw kaarten: {speler1}, kaarten van de computer: {speler2}")
    print(f"Jouw score is: {somSpeler}, de score van de computer is: {somComputer}")
    if somSpeler == somComputer:
        print("Jullie hebben gelijk gespeeld")
    elif somSpeler > somComputer:
        print("De computer heeft gewonnen...")
    else:
        print("Gefeliciteerd! jij hebt gewonnen!")
    return False




def bot():
    global stapel
    score = speler2[0] + speler2[1] + speler2[2] + speler2[3]
    b_bot = pakken()
    if b_bot == 10:
        stapel = b_bot
    elif b_bot == 11:
        randomKaart = random.randint(0, 3)
        speler2_see[randomKaart] = speler2[randomKaart]
    elif b_bot < 6:
        veranderKaart = max(speler2_see)
        kaartIndex = speler2_see.index(veranderKaart)
        stapel = speler2[kaartIndex]
        speler2[kaartIndex] = b_bot
        speler2_see[kaartIndex] = b_bot
    elif stapel < 6:
        veranderKaart = max(speler2_see)
        kaartIndex = speler2_see.index(veranderKaart)
        speler2[kaartIndex], stapel = stapel, speler2[kaartIndex]
        speler2_see[kaartIndex] = stapel
    else:
        stapel = b_bot
    if score < 10:
        stoppen()
    print("De computer heeft een kaart gepakt")

def ruilen():
    speler = int(input("Welke speler wil je ruilen? \n[1]Speler 1?"))
    kaartSpeler = int(input(f"Welke kaart wil je ruilen van speler {speler}? \n[1], [2], [3] of [4]")) + 1
    print(f"Welke eigen kaart wil je ruilen voor kaart {kaartSpeler} van speler {speler}?")
    eigenKaart = int(input("[1], [2], [3] of [4]")) + 1

    if speler == 1:
        a = speler2[kaartSpeler]
        speler2[kaartSpeler] = speler1[eigenKaart]
        speler1[eigenKaart] = a

def uitdelen():
    for x in range(len(speler1)):
        speler1[x] = pakken()
    for x in range(len(speler2)):
        speler2[x] = pakken()

welkom()
uitleg = input("Ken je de spelregels al, of wil je uitleg? \n[1]Ik ken de regels al \n[2]Ik wil graag uitleg")
if uitleg == "2":
    spelregelUitleg()


gameActive = True
stapel = pakken()
ronde = 1
speler1 = [0, 0, 0, 0]
speler2 = [0, 0, 0, 0]
uitdelen()
speler2_see = [speler2[0], 6, 6, speler2[3]]
clearScreen()
print(f"Onthoud deze kaarten goed! {speler1[0]} | * | * | {speler1[3]}")
time.sleep(5)

while gameActive is True:
    if beurtPlayer is True:
        beurtPlayer = False
        clearScreen()
        print(f"Ronde: {ronde} \nHuididge speler: Jij \nJouw kaarten: * | * | * | * ")
        ronde = ronde + 1
        print(f"De bovenste kaart op de pot is {stapel}")
        mode = input("Wat wil je doen? \n[1]Stoppen \n[2]Nieuwe kaart trekken \n[3]Pak de kaart van de stapel")
        if mode == "2":
            a = pakken()
            if a == 10:
                print(f"Jouw kaart is ruilen")
                if (input("Wil je ruilen? \n [1]Ja \n [2]Nee")) == "1":
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
        elif mode == "1":
            gameActive = stoppen()
            break
        elif mode == "3":
            stapel = vervangen(stapel)
    elif beurtPlayer is False:
        beurtPlayer = True
        bot()
        time.sleep(2)
 