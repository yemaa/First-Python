#Import librerie
import random
from termcolor import colored, cprint
import time

#Dichiarazione variabili del gioco: colori, errori, vittoria
colori=["Bianco", "Rosso", "Giallo", "Blu", "Verde", "Magenta"]
erroriPermessi = 6
rispEsatte = ["...", "...", "...", "..."]
Vittoria = False
puntinoNero = colored("•", "grey", "on_white")
puntinoBianco = colored("•", "white", "on_grey")

#Introduzione e spiegazione gioco
time.sleep(2)
print("Ciao! Benvenuto nel gioco meno adatto per le persone daltoniche: Master Mind! ")
time.sleep(4)
print("In pratica il computer sceglierà quattro colori, e tu dovrai indovinare la combinazione. Avrai a disposizione 6 tentativi. ")
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
print("Ovviamente non vagherai nel vuoto, ti dirò se hai messo un colore nel posto giusto, in questo modo: ")

time.sleep(3)
print("Stamperò un pallino nero a sfondo bianco quando il colore è quello giusto nella posizione giusta, così: ", puntinoNero )

time.sleep(3)
print("Stamperò invece un pallino bianco a sfondo nero quando il colore è presente nella sequenza, ma non pè nel posto giusto, così:", puntinoBianco)

#Annunciazione inizio
time.sleep(3)
print("Sei pronto!?!?")
print("Cominciamo! ")

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

    #Input colori
    time.sleep(2)
    primoRis = str(input("Digita il primo colore: ")).capitalize()
    secondoRis = str(input("Digita il secondo colore: ")).capitalize()
    terzoRis = str(input("Digita il terzo colore: ")).capitalize()
    quartoRis = str(input("Digita il quarto colore: ")).capitalize()
    
    #Calcolo errori permessi
    erroriPermessi -= 1
    
    #Controllo colori
    time.sleep(3)
    if erroriPermessi == 0:
        cprint("Mi dispiace, ma hai esaurito i tentativi...", "red")
        break

    else:
        
        if primoRis == primo:
            cprint("•", "grey","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(0)
            rispEsatte.insert(0, primoRis)
            
        if primoRis in listaAppoggio and primoRis != primo:
            cprint("•", "white", "on_grey", end=colored("|", "cyan"))

        if secondoRis == secondo:
            cprint("•", "grey","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(1)
            rispEsatte.insert(1, secondoRis)

        elif secondoRis in listaAppoggio and secondoRis != secondo:
            cprint("•", "white", "on_grey", end=colored("|", "cyan"))

        else:
            pass

        if terzoRis == terzo:
            cprint("•", "grey","on_white", end=colored("|", "cyan") )
            rispEsatte.pop(2)
            rispEsatte.insert(2, terzoRis)

        elif terzoRis in listaAppoggio and terzoRis != terzo:
            cprint("•", "white", "on_grey", end=colored("|", "cyan"))

        else:
            pass

        if quartoRis == quarto:
            cprint("•", "grey","on_white") 
            rispEsatte.pop(3)
            rispEsatte.insert(3, quartoRis)
        
        elif quartoRis in listaAppoggio and quartoRis != quarto:
            cprint("•", "white", "on_grey")
        
        else:
            pass

        if rispEsatte == listaAppoggio:
            Vittoria = True
            break

#Stampa finale del gioco
if Vittoria == True:
    cprint("Complimenti, sei riuscito a battere un pezzo di ferraglia a un gioco per bambini!! Torna a giocare quando vuoi! ", "cyan")

else:
    cprint("GAME OVER... La sequenza era:", "red", end=" ")
    print(", ".join(listaAppoggio))