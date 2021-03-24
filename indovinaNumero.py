import random
limite = int(input("Scegli un limite che sia maggiore di 0: "))
if limite == 0:
    print("Sei una puttana")

else: 
    print("Scegli un numero che vada da 0 al limite che mi hai detto, ma non dirmelo... ")
    print("Rispondi A se il numero che ho detto è troppo basso.")
    print("B, se è troppo alto. ")
    print("C, se è corretto. ")
    print("Cominciamo: ")
    x = False
    while x == False:
        guessComp = random.randint(0, limite)
        print(guessComp)
        guessPlayer = str(input("A, B, o C?"))
        guessPlayer = guessPlayer.upper()
        if guessPlayer == "A":
            guessComp2 = random.randint(guessComp, limite)
            print(guessComp2) 
        
        elif guessPlayer == "B":
            guessComp2 = random.randint(limite, guessComp)
            print(guessComp2)

        elif guessPlayer == "C":
            print(guessComp2)

        

    