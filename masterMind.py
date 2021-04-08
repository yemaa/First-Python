#Import librerie
import random
from termcolor import colored, cprint
import time

#Dichiarazione variabili del gioco: colori, errori, vittoria
colori=["Bianco", "Rosso", "Giallo", "Blu", "Verde", "Magenta"]
erroriPermessi = 6
rispEsatte = ["...", "...", "...", "..."]
Vittoria = False
"""
#Introduzione e spiegazione gioco
time.sleep(2)
print("Ciao! Benvenuto nel gioco meno adatto per le persone daltoniche: Master Mind! ")

time.sleep(4)
print("In pratica il computer sceglierà quattro colori da una lista, e tu dovrai indovinare la combinazione. Avrai a disposizione 6 tentativi")

time.sleep(6)
print("Per azzeccare la sequenza dovrai inserire i nomi di quattro dei sei possibili colori, questi qua: ")

#Stampa lista
time.sleep(5)
cprint("Bianco", "white")
cprint("Giallo", "yellow")
cprint("Rosso", "red")
cprint("Magenta", "magenta")
cprint("Verde", "green")
cprint("Blu", "blue")

time.sleep(5)
print("Ovviamente non vagherai nel vuoto, ti dirò se hai messo un colore nel posto giusto")

#Annunciazione inizio
time.sleep(3)
print("Are you ready!?!?")
print("Let's start! ")
"""
#Scelta sequenza
primo = random.choice(colori)
secondo = random.choice(colori)
terzo = random.choice(colori)
quarto = random.choice(colori)
listaAppoggio = [primo, secondo, terzo, quarto]

#While del gioco
time.sleep(5)
while True:
    #Stampa errori rimasti e colori nella lista
    print("Errori rimasti: ", erroriPermessi)
    print(listaAppoggio)

    #Input colori
    time.sleep(2)
    primoRis = str(input("Dimmi un colore: ")).capitalize()
    secondoRis = str(input("Dimmi un colore: ")).capitalize()
    terzoRis = str(input("Dimmi un colore: ")).capitalize()
    quartoRis = str(input("Dimmi un colore: ")).capitalize()
    
    #Calcolo errori permessi
    erroriPermessi -= 1
    
    #Controllo colori
    time.sleep(3)
    if erroriPermessi == 0:
        cprint("Mi dispiace, ma hai esaurito i tentativi.", "red")
        break

    else:
        
        if primoRis == primo:
            cprint(" ", "white","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(0)
            rispEsatte.insert(0, primoRis)
            
        if primoRis == listaAppoggio:
            cprint(" ", "grey", "on_grey", end=colored("|", "cyan"))
            print("bro")

        if secondoRis == secondo:
            cprint(" ", "white","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(1)
            rispEsatte.insert(1, secondoRis)

        elif secondoRis == listaAppoggio and secondoRis != secondo:
            cprint(" ", "grey", "on_grey", end=colored("|", "cyan"))

        else:
            pass

        if terzoRis == terzo:
            cprint(" ", "white","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(2)
            rispEsatte.insert(2, terzoRis)

        elif terzoRis == listaAppoggio and terzoRis != terzo:
            cprint(" ", "grey", "on_grey", end=colored("|", "cyan"))

        else:
            pass

        if quartoRis == quarto:
            cprint(" ", "white","on_white") 
            rispEsatte.pop(3)
            rispEsatte.insert(3, quartoRis)
        
        elif quartoRis == listaAppoggio and quartoRis != quarto:
            cprint(" ", "grey", "on_grey")
        
        else:
            pass

        if rispEsatte == listaAppoggio:
            Vittoria = True
            break

#Stampa finale del gioco
if Vittoria == True:
    print("Complimenti, sei riuscito a battere un pezzo di ferraglia a un gioco per bambini!! Torna a giocare quando vuoi! ")

else:
    print(f"GAME OVER... La sequenza era:, {primo}, {secondo}, {terzo}, {quarto}")