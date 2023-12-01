# Spelplanen är uppsatt med 10 positioner
spelplan1 = [' ' for x in range(10)]

# Funktion för att placera en spelares eller datorns symbol på en plats
def sättInSymbol(symbol, position):
    spelplan1[position] = symbol

# Funktionen gör så att den kontrollerar om spelplanen är ledig
def platsÄrLedig(position):
    return spelplan1[position] == ' '

# Funktion för att spelplanen ska skrivas ut i terminalen
def skrivUtSpelplan(spelplan):
    print('   |   |   ')
    print(' ' + spelplan[1] + ' | ' + spelplan[2] + ' | ' + spelplan[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + spelplan[4] + ' | ' + spelplan[5] + ' | ' + spelplan[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + spelplan[7] + ' | ' + spelplan[8] + ' | ' + spelplan[9])
    print('   |   |   ')

# Funktion för att kontrollera om planen är full
def ärSpelplanFull(spelplan):
    if spelplan.count(' ') > 1:
        return False
    else:
        return True

# Funktion för att kontrollera om en spelare har vunnit
def ärVinnare(spelplan, symbol):
    # Vinnande kombinationer för tre i rad
    vinnande_kombinationer = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]
   
# Funktion för spelarens drag
def spelarDrag():
    kör = True
    while kör:
        drag = input("Vänligen ange en position att placera X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if 0 < drag < 10:
                if platsÄrLedig(drag):
                    kör = False
                    sättInSymbol('X', drag)
                else:
                    print('Tyvärr, den här platsen är inte ledig')
            else:
                print('Välj ett nummer mellan 1 och 9')

        except ValueError:
            print('Vänligen välj ett nummer')

# Funktion för datorns drag
def datornsDrag():
    möjligaDrag = [x for x, symbol in enumerate(spelplan1) if symbol == ' ' and x != 0]
    drag = 0

    for symbol in ['O', 'X']:
        for i in möjligaDrag:
            kopiaAvSpelplan = spelplan1[:]
            kopiaAvSpelplan[i] = symbol
            if ärVinnare(kopiaAvSpelplan, symbol):
                drag = i
                return drag

    hörnLediga = []
    for i in möjligaDrag:
        if i in [1, 3, 7, 9]:
            hörnLediga.append(i)

    if len(hörnLediga) > 0:
        drag = slumpmässigtVal(hörnLediga)
        return drag

    if 5 in möjligaDrag:
        drag = 5
        return drag

    kanterLediga = []
    for i in möjligaDrag:
        if i in [2, 4, 6, 8]:
            kanterLediga.append(i)

    if len(kanterLediga) > 0:
        drag = slumpmässigtVal(kanterLediga)
        return drag

# Funktion för slumpmässigt val
def slumpmässigtVal(lista):
    import random
    ln = len(lista)
    r = random.randrange(0, ln)
    return lista[r]

# Huvudfunktionen för att köra spelet
def huvud():
    print("Välkommen till spelet!")
    skrivUtSpelplan(spelplan1)

    while not ärSpelplanFull(spelplan1):
        if not ärVinnare(spelplan1, 'O'):
            spelarDrag()
            skrivUtSpelplan(spelplan1)
        else:
            print("Bra försök, spela igen!")
            break

        if not ärVinnare(spelplan1, 'X'):
            drag = datornsDrag()
            if drag == 0:
                print(" ")
            else:
                sättInSymbol('O', drag)
                print('Datorn placerade en O på position', drag, ':')
                skrivUtSpelplan(spelplan1)
        else:
            print("Bra Jobbat! Du vann!")
            break

    if ärSpelplanFull(spelplan1):
        print("Oavgjort!")

# Huvudloop för att spela igen
while True:
    x = input("Vill du spela? Tryck 'y' för ja eller 'n' för nej (y/n)\n")
    if x.lower() == 'y':
        spelplan1 = [' ' for x in range(10)]
        print('--------------------')
        huvud()
    else:
        break