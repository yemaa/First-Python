#STANZE
"""
stanza 1 terraria
stanza 2 gta
stanza 3 minecraft
stanza 4 Assassin's creed

"""

#STATISCICHE E OGGETTI NECESSARI PER FINIRE IL GIOCO
stats = [4, 4, 4] #strenght, intelligence, and stelth
chiavi = [] #lista delle chiavi da trovare e finire il gioco

#INTRODUZIONE 
print("\nCiao! Benvenuto! Oggi ti cimenterai in una piccola avventura creata da due ragazzi, sarà divertente e speriamo che ti prenda. Si chiama: 'New Game!' È un piccolo gioco a scelte, dove il tuo obiettivo sarà quello di completare tutte le missioni e vincere!")
nomeGiocatore = input("Prima di tutto dimmi il tuo nome: ")
nomeGiocatore = nomeGiocatore.capitalize()
print("\nCiao "+ nomeGiocatore)
print("Le possibili azioni che puoi eseguire sono: interagisco, cerco, si, no, torno, prendo, destra, sinistra. Nel caso non siano collegate con domanda, accanto a essa ci saranno i possibili comandi.")
print("Se vedrai dei nomi e delle virgolette vuol dire che stai leggendo un dialogo, mentre se non ci sono è un pensiero oppure una narrazione, dipende dai punti di vista ")
print("Capito tutto? Spero di si! Cominiciamo!")
print("")

#INIZIO GIOCO
print("Do- Dove sono? Ah che mal di testa... Perché è tutto a pixel? Ma, quella è una persona? Non avevo mai visto una persona fatta a pixel. Sopra di lui c'è una scritta: Co-Cody? sarà il suo nome? ")


while True: 

	primaScelta = input("Devo andare a chiedere a Cody che cosa sia questo mondo oppure cercare da solo la risposta, e magari anche un'uscita... Cosa faccio?: ")
	primaScelta = primaScelta.lower()
	if primaScelta == "interagisco":
		print("\nCody: 'Ti trovi nel mondo di Terraria, e sei nella stanza numero 1.' ")
		print(""+nomeGiocatore+": 'Stanza numero 1?' ")
		print("Cody: 'Esatto! Ne sono presenti 4 e devi andare fino all'ultima! Per passare nella stanza 2 devi usare lo specchio magico che trovi nel dungeon, a tuo rischio e pericolo... ' ")
		primaScelta = "cerco"
		

	if primaScelta == "cerco":
		print("\nMeglio non fidarsi di Cody... Diamo una chance a quel castello là. Tanto è lì davan-")
		print("Cody:'Attento! Non entrarci! È un dungeon! Non sei pronto!")
		print("Magari ha ragione...")
		break
	
	else:
		print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

while True:

	secondaScelta = input("Entro o no?:  ")
	secondaScelta = secondaScelta.lower()

	if secondaScelta == "si":
		print("\nNo! È meglio non fidarsi e ignorarlo un'altra volta. Entriamo nel dungeon. Però non posso andare avanti con tutti quei cosi strani lì dentro, tuttavia li davanti c'è lo specchio magico... Se lo prendo devo usarlo subito, sennò farò una brutta fine, questo è certo...")
		terzaScelta = input("Vado a prendere lo specchio oppure torno indietro?:  ")
		terzaScelta = terzaScelta.lower()
		break


	elif secondaScelta == "no":
		print("\n"+nomeGiocatore+": 'Forse avevi ragione. Sono appena entrato in questo mondo e già entro in un dungeon. Ma che videogiocatore sono? '")		
		print("Cody: 'Allora l'hai capito! Dai vieni, ho un compito per te. Devi cercare delle bacche speciali: sono rosse e di forma ottagonale, se lo farai ti darò una ricompensa.'")
		print(""+nomeGiocatore+": 'Ok facciamolo!' ")
		print(". . . . .")
		print("Ah! Eccole! È stato più facile del previsto. Saranno buone?")
		print("Ciomp Ciomp...")
		print("Co-Cosa mi sta succedendo? Sento come un formicolio passarmi per tutto il corpo..")
		print(""+nomeGiocatore+": 'Ehy, che diavolo mi è successo?' ")
		print("Cody: 'Lo scoprirai presto... Nel frattempo ti do la tua ricompensa' ")
		print(""+nomeGiocatore+": 'Ma questo... È lo specchio magico. Perché non mi hai detto che ce l'avevi?' ")
		print("Cody: 'Volevo provare la tua fiducia nei miei confronti. Ora usalo su!")
		terzaScelta = "prendo"
		stats[0] = stats[0] + 2
		break

	else:
		print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

while True:

	if terzaScelta == "torno":
		print("\n"+nomeGiocatore+": 'Forse avevi ragione. Sono appena entrato in questo mondo e già entro in un dungeon. Ma che videogiocatore sono? '")
		print("Cody: 'Allora l'hai capito! Dai vieni, ho un compito per te. Devi cercare delle bacche speciali: sono rosse e di forma ottagonale, se lo farai ti darò una ricompensa.'")
		print(""+nomeGiocatore+": 'Ok facciamolo!' ")
		print(". . . . .")
		print("Ah! Eccole! È stato più facile del previsto. Saranno buone?")
		print("Ciomp Ciomp...")
		print("Co-Cosa mi sta succedendo? Sento come un formicolio passarmi per tutto il corpo..")
		print(""+nomeGiocatore+": 'Ehy, che diavolo mi è successo?' ")
		print("Cody: 'Lo scoprirai presto... Nel frattempo ti do la tua ricompensa' ")
		print(""+nomeGiocatore+": 'Ma questo... È lo specchio magico. Perché non mi hai detto che ce l'avevi?' ")
		print("Cody: 'Volevo provare la tua fiducia nei miei confronti. Ora usalo su!")
		stats[0] = stats[0] + 2
		print(". . . . .")
		print("Ma che... Nemmeno il tempo di dire 'a' che appena ho toccato lo specchio non ho visto più niente per pochi secondi...")
		print("\nDov- Dove sono? È un letto quello dove mi ritrovo? Perché sento di averlo già visto questo abbiente? ")
		print("TOC TOC")
		print("Ma chi è ora... Big Smoke? Quello di San Andreas? Cosa diavolo sta succedendo? ")
		print("GNIIIK")
		print("\nBig Smoke: 'Hey com'è fratello? ")
		print("Ma, non mi ha mai conosciuto di persona, come fa ad essere così amichevole?")
		print("Big Smoke: 'Senti fratello so che tu per me faresti qualsiasi cosa, mi devi aiutare con un colpo: sarà sia nei tuoi e miei interessi, se andrà a buon fine potrai vedere le tue statistiche e andare avanti, sei con me?")
		print("Statistiche? Andare avanti? Intende con le stanze?")
		print(""+nomeGiocatore+": 'Ci sto!")
		print("Grande Fumo: 'Dovremo saccheggiare una banca, quella che mi ha fatto andare in rosso per colpa delle tasse. Gli ruberemo tutti i soldi. Dovremo essere veloci: entrare, spaccare, uscire, ciao")
		print("Big Smoke: 'Ci siamo, potremo finalmente vendicarci di quegli avvoltoi. Sei pronto? ")
		print(""+nomeGiocatore+": 'Lo sai che sono nato pronto! Facciamolo!") 
		break


	if terzaScelta == "prendo":
		print("\nMa che... Nemmeno il tempo di dire 'a' che appena ho toccato lo specchio non ho visto più niente per pochi secondi...")
		print("Dov- Dove sono? È un letto quello dove mi ritrovo? Perché sento di averlo già visto questo posto? ")
		print("TOC TOC")
		print("Ma chi è ora... Big Smoke? Quello di San Andreas? Cosa diavolo sta succedendo? ")
		print("GNIIIK")
		print("\nBig Smoke: 'Hey com'è fratello? ")
		print("Ma, non mi ha mai conosciuto di persona, come fa ad essere così amichevole?")
		print("Big Smoke: 'Senti fratello so che tu per me faresti qualsiasi cosa, mi devi aiutare con un colpo: sarà sia nei tuoi e miei interessi, se andrà a buon fine potrai vedere le tue statistiche e andare avanti, sei con me?")
		print("Statistiche? Andare avanti? Intende con le stanze?")
		print(""+nomeGiocatore+": 'Ci sto!")
		print("Grande Fumo: 'Dovremo saccheggiare una banca, quella che mi ha fatto andare in rosso per colpa delle tasse. Gli ruberemo tutti i soldi. Dovremo essere veloci: entrare, spaccare, uscire, ciao")
		print("Big Smoke: 'Ci siamo, potremo finalmente vendicarci di quegli avvoltoi. Sei pronto? ")
		print(""+nomeGiocatore+": 'Lo sai che sono nato pronto! Facciamolo!") 
		break

	else:
		print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

while True:
	print("\n. . . . .")
	sequenza = input("SBAM! Entrando facciamo sedere tutti a terra con le mani sulla nuca. Ora tocca agli agenti... Uno si alza e ci minaccia, sta per sparare a Big Smoke, presto digita questa sequenza per sparare all'agente: '53550' ")
	if sequenza == "53550":
		print("\nOh ok menomale, hai digitato la sequenza giusta e sei riuscito a salvare Big Smoke sparando al braccio dell'agente")
		print("Dopo averlo legato cerchiamo i soldi della banca, che ovviamente sono nel cavou. 984 milioni di dollari. Questo è l'ammontare di denaro che dobbiamo rubare... ")
		print("Dopo aver preso tutti questi soldi, carichiamo le borse sul camion e ci prepariamo a partire per la fuga.")
		print("OOUUWIIIOOOUUUWWIIIII")
		print("Nemmeno il tempo di rubare dei soldi che la polizia già ci sta alle calcagna, dobbiamo scappare all'istante.")
		print("WROOM")
		print("Vivendo la nostra vita a un quarto di miglio alla volta riusciamo a partire in tempo prima che la polizia ci catturi. Ma il bello viene adesso: è notte fonda e non si vede niente, i fari del camion sono rotti, dobbiamo affidarci al destino. Scrivi sinistra o destra per guidare il camion e riuscire a scappare...")
		break
	else:
		print("\nMa sai maneggiare un'arma? Cavolo credo proprio di no. Ti sei appena sparato sul piede! Ci vuole dell'impegno")
		print("Comunque Big Smoke non c'è più per colpa tua, e tu sei un esperto nel spararsi addosso.")
		print("GAME OVER. . . ")
		exit()

while True:
	primaCurva = input("\nSiamo alla prima curva, decidi: sinistra o destra. (Hint: izquierda...):  ")
	primaCurva = primaCurva.lower()
	if primaCurva == "sinistra":
		print("Ok perfetto, la prima curva è andata... Decidi per la prossima... ")
	else:
		print("Ti avranno bocciato alla patente, perché come vedi ci siamo appena schiantati e la polizia ci ha presi")
		print("GAME OVER. . .")
		exit()
	###########################
	secondaCurva = input("\nChe dio sia con noi! Avanti con la prossima curva. (Hint: con che mano scriveva Napoleone se scriveva con la destra?:  ")
	secondaCurva = secondaCurva.lower()
	if secondaCurva == "destra":
		print("God bless us! Seconda curva fatta...")
	else:
		print("Ti avranno bocciato alla patente, perché come vedi ci siamo appena schiantati e la polizia ci ha presi")
		print("GAME OVER. . .")
		exit()
	###########################
	terzaCurva = input("\nAvanti un altro! (Hint: il bagno è sempre in fondo a...): ")
	terzaCurva = terzaCurva.lower()
	if terzaCurva == "destra":
		print("Cavolo si! Ne manca solo una forza!")
	else:
		print("Ti avranno bocciato alla patente, perché come vedi ci siamo appena schiantati e la polizia ci ha presi")
		print("GAME OVER. . .")
		exit()
	###########################
	quartaCurva = input("\nGiorno fortunato eh? Dai andiamo! (Hint: orientamento di Renzi): ")
	quartaCurva = quartaCurva.lower()
	if quartaCurva == "sinistra":
		print("Lucckkkyyy. Ciao Ciao polizia, e bienvenidos dinero")
		break
	else:
		print("Ti avranno bocciato alla patente, perché come vedi ci siamo appena schiantati e la polizia ci ha presi")
		print("GAME OVER. . .")
		exit()

#FINE CICLO WHILE
print("\nBig Smoke: 'Ah ah fratello sei una bomba! Ma ti rendi conto di cosa abbiamo appena fatto?! 984 milioni di dollari!")
print(""+nomeGiocatore+": 'Si diavolo! Ohi bro, una promessa è una promessa. Mi darai cosa mi hai detto vero? ")
print("Big Smoke: 'Certo fratello' ")
print("Big Smoke: 'Ora che siamo ricchi e al sicuro ti posso dire cosa so: le statistische, o stats, sono dei dati che rappresentano la tua forma fisica. Di stats ne sono presenti 3: forza, intelligenza e denaro")
print(str(stats[0]) + " - strengh, " + str(stats[1]) + " - intelligence, " + str(stats[2]) + " - stealth")
if stats[0] >= 6:
	print("Big Smoke: 'Oh vedo che hai già allenato la forza! Sei stato bravo!")
print("Big Smoke: 'Fico vero? ")
print("Big Smoke: 'Andiamo a dormire ora, domani è un'altro giorno...' ")
print(". . . . .")
print("\nBuongiorno a m- Cosa, è successo?! Questo non è il mio letto, e nemmeno la mia stanza. E perché è di nuovo tutto a pixel? Sono di nuovo nella stanza di Terraria? No, è diversa...")
print("HHHHAAAHHHH")
print(""+nomeGiocatore+": 'E tu chi diavolo saresti?' ")
print("???: 'Io sono il capo villager di questo villaggio. HHHAAAHHH. Sei arrivato fin qua, notevole. Visto che sei così determinato, ti darò una missione. HHHAAAAHHH. Se la porterai a termine ti darò il lascia passare per la quarta stanza")
print("Villager? Vuol dire che siamo in minecraft? Cosa gli dovrei portare? Degli smeraldi?")
print("Capo Villager: 'HHHAAAHHH. La tua missione sarà quella quella di andare in miniera e trovare una riserva di smeraldi che è stata persa anni orsono dai nostri concittadini. Si trova sotto al livello 12, quindi sarai molto vicino alla lavAAHHHAAAA. '")
while True: 
	quartaScelta = input("\nSei dei nostri?: ")
	quartaScelta = quartaScelta.lower()
	if quartaScelta == "no":
		print("Capo Villager: 'Bene... Ma non pensare che ti garantiremo vitto e alloggio. Via dal nostro villaggio. HHHAAAHHH' ")
		print(". . . . .")
		print("E ora? Non ho nè cibo nè una casa. Sono le 8 di sera e la notte sta arrivando. I mob mi mangeranno e non scoprirò il segreto di questo gioco, forse è meglio accettare quell'incarico...")
		quartaScelta = "si"

	if quartaScelta == "si":
		print("Capo Villager: 'Una recluta in più non fa mai male, soprattutto se è promettente come te.HHHAAAHHH. Vieni su ti spiego il piano...")
		quintaScelta = input("\nCapo Villager: 'HHHAAAH. Hai tre scelte per eseguire questa missione: 1. seguire le caverne inesplorate di questo villaggio; 2. seguire le miniere scavate dai nostri coetanei; 3. scavare tutto sotto di te. Dimmi solo il numero del tipo che vuoi seguire. HHHAAAHHH. A te la scelta... ")
		if quintaScelta == "1":
			print("\nCapo Villager: 'Quindi sei un esploratore eh? Non te l'avrei consigliato, ma deciti tu. L'equipaggiamento è di là. Tutto tuo. HHHAAAHHH' ")
			print(". . . . .")
			print(""+nomeGiocatore+": 'Ok tutto pront! Ci vediamo quando torno!")
			print("Capo Villager: 'Ti HHAAAHHspetteremo!")
			print(". . . . .")
			print(""+nomeGiocatore+": 'Certo che sono buie queste caverne... Forse era meglio scegliere un'altra strada... Chissà se rimbomba: EEHHHHYYYY'")
			print("'EHHYY...EEHHHYY.EEHY.EHy.HH'")
			print("Wow!")
			print("'BRAAAA.BRAAAA.BRAAA.BRAA'")
			print("QUello non era un buon segno. Cos'era un pipistrello? Non penso che i pipistrelli facciano questi suoni. Ma allora, chi, è?  ")
			print("UUFF")
			print(""+nomeGiocatore+": 'Ehy ehy NO! Lasciami in pace! NOOoo..")
			print(""+nomeGiocatore+" was slain by zombie")
			exit()
		
		if quintaScelta == "2":
			print("\nCapo Villager: 'Scelta più saggia. L'equipaggiamento è di là. Tutto tuo. HHHAAAHHH ")
			print(". . . . .")
			print("Sono scavate proprio bene queste caverne. Tutto così ben fatto. Come avranno fatto a perdersi? ")
			print("Ehy ma quella è luce? Sebbene sia debole... Speriamo sia la strada giusta...")
			print("OH. MIO. DIO. Ce l'ho fatta. Davanti a me ho la riserva di smeraldi del villaggio. Ma quel-")
			print("???: 'Ti prego aiutami... Sono da qui da settimane e ho finito il cibo...")
			print(""+nomeGiocatore+": 'Tranquillo. Ci sono qui io. Sei del villaggio giusto? ")
			print("???: 'Si. Stavamo cercando di riportare questa riserva quando ci è caduta addosso della ghiaia e non abbiamo più visto niente")
			print(""+nomeGiocatore+": 'Ecco perché non siete più tornati... '")
			print(""+nomeGiocatore+": 'Dai forza vieni... OOIISSA... Certo che sei davvero pesante per non aver mangiato per settimane...' ")
			print(". . . . . ")
			print("Capo Villager: 'Ehy eccolo!! Ha anche Cory con sè! Forza aiutiamoli")
			print(". . . . .")
			print("Capo Villager: 'Sei di sicuro il nostro salvatore! HIPPIP HURRA per "+nomeGiocatore+"!!!!' ")
			print("Villaggio: HIPPIP HURRA!!! HIPPIP HURRA!!! HIPPIP HUR-'")
			break

		if quintaScelta == "3":
			print("\nCapo Villager: 'Sei una talpa? Contento te. Stai attento però, è possibile che tu cada nella lava. L'equipaggiamento è di là. Tutto tuo. HHHAAAHHH' ")
			print(". . . . .")
			print("STUM STUM STUM")
			print("Ma quanto ancora devo scavare per trovare quella riserva? ")
			print("STLANK")
			print("Ma che?! Ma... Nemmeno un nabbo avrebbe preso il piccone d'oro, Lo sanno tutti che su minecraft il piccone d'oro è quello più fragile. Adesso mi tocca scavare a mani nude.")
			print("AAHHH. Ma quanto fa male?! Ci vuole un sacco per rompere un blocco e in più mi sto distruggendo le mani. Perché poi fa così caldo? Siamo sottot-")
			print("OOOAAAHHHH")
			print("AAAAAAAHHHHHHH")
			print(". . . . .")
			print(""+nomeGiocatore+" swam in lava")
			exit()
		
		else:
			print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

print("\nHEYHEYHEY perché?! Perché se mi acclamano deve finire tutto? E ora? Dove diavolo sono? ")
print("???: 'Non importa dove sei ora, ma quanta strada hai fatto fino ad ora. È tempo di spiegarti bene tutto ciò che hai passato in questa avventura:")
print(""+nomeGiocatore+": 'Si ma tu chi sei? '")
print("???: 'Io sono Ezio Auditore. Uno dei più grandi assassini mai esistiti. '")
print(""+nomeGiocatore+": 'Oh quindi adesso siamo in Assassin's Creed? Fantast-'")
print("Ezio Auditore: 'Zitto. Niente scherzi. Sono io a parlare qui... Stavo dicendo:")
print("Ezio Auditore: 'Cody di sicuro ti avrà detto poco e niente. Nelle 4 stanze che hai appena visitato sono presenti tre occhi di ender, che saranno le chiavi per aprire il portale e uscire da qui. In più per trovarle avrai bisogno di migliorare i tuoi stats, dovrai avere un minimo di 6 per poter trovare gli occhi.'")
print("Ezio Auditore: 'Al momento i tuoi stats sono questi: "+str(stats)+"")
if stats[0] >= 6:
	print("Ezio Auditore: 'Oh, vedo che hai già allenato la forza trovando le bacche ottagonali! Ben fatto!'")
print("Ezio Auditore: 'Adesso sei libero di allenare le tue stats nelle stanze...")
print("Ezio Auditore: 'Ora vai nella terza stanza tramite quella porta laggiù, così potrai cominciare a muoverti e iniziare a guadagnare stats e occhi di ender.")

#IL MONDO APERTO
while True:
    if 1 in chiavi and 2 in chiavi and 3 in chiavi:
        print("\nCapo Villager: 'Vedo che sei riuscito a trovare tutti gli occhi di ender, davanti a te il portale e la scelta: vuoi entrare? ")
        sceltaFinale = input("si o no?: ")
        if sceltaFinale == "si":
            print(""+nomeGiocatore+"SI! Voglio scoprire cosa c'è dopo, ti saluto Capo... ")
            break
        elif sceltaFinale == "no":
            print(""+nomeGiocatore+": 'Nah. Voglio passare ancora un pò di tempo qua...")

    fatto = False
    print("\n"+nomeGiocatore+": 'Bene, ora che sono nella stanza 3 devo decidere cosa fare, ma come lo decido? Ah ok perfetto c'è il capo dei Villager: ")
    print(""+nomeGiocatore+": 'Hey, mi sapresti dire come faccio a muovermi di stanza?") 
    print("Capo Villager: '"+nomeGiocatore+", dopo che ci hai aiutati non posso non darti una risposta:")
    stanza = input("PER LA STANZA NUMERO 1 DEVI PREMERE 1, PER LA STANZA NUMERO 2 DEVI PREMERE 2, PER LA STANZA NUMERO 4 DEVI PREMERE 4, PER ALLENARE L'INTELLIGENZA DEVI PREMERE 'i': ")

    if stanza == "1":
        print("\nOh wow! Bene! Sono di nuovo nella stanza di Terraria immagino")
        print("Cody: 'PER L'OCCHIO DI ENDER NECESSITI DI 6 DI INTELLIGENZA...")
        print("Mi serve almeno 6 di intelligenza per ottenere l'occhio... ")
        while fatto != True:
            laMiaScelta1 = input("\nHmmmm, devo decidere che fare... Usare l'intelligenza, allenare la forza, oppure tornare nella stanza 3? (i, f, 3): ")
            if laMiaScelta1 == "i":
                if stats[1] >= 6:
                    print("\nMi hanno sempre detto che sono intelligente ma che non mi applico. Attivati cervello!")
                    print("*LAMPADINA CHE SI ACCENDE*")
                    print("Proviamo a cercare sotto al letto di Cody... ")
                    print(". . . . .")
                    print("*Hai trovato il terzo occhio!*")
                    print("EVVAI!!")
                    if 3 in chiavi:
                        print("\nHai già trovato il terzo occhio, non c'è più!")
                        print(chiavi)
                        fatto = True
                    else:                       
                        chiavi.append(3)
                        print("\nOra posso tornare nella stanza 3...")
                        print(chiavi)
                        print(". . . . .")
                        fatto = True
                else:
                    print("Uh, non so proprio che fare. Non ho ideeee...")

            elif laMiaScelta1 == "f":
                print("\nOk proviamo ad allenare la forza. Ma come? Chiediamolo a Cody ")
                print(""+nomeGiocatore+": 'Hey Cody, sai mica come possa fare ad allenare la forza?")
                print("Cody: 'Certo! Devi mangiare le bacche ottagonali, ma una sola manciata non ti darà forza sufficiente...")
                print("CIOMP CIOMP")
                print(""+nomeGiocatore+": 'Ok credo che abbiano fatto effetto... Grazie Cody!")
                stats[0] = stats[0] + 1
                fatto = True
            elif laMiaScelta1 == "3":
                print("\nBene, non ho niente da fare qua, torno nella stanza 3")     
                print(". . . . .")          
                fatto = True
            else:
                print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

    elif stanza == "2":
        print("\nHuh, di nuovo da grande fumo... Ehy fratello come faccio a trovare l'occhio di questa stanza?") 
        print("Grande Fumo: 'Ehy fratello... Senti per prendere l'occhio dovrai fare un altro colpo, ma stavolta da solo: l'occhio si trova nella camera del presidente della banca che abbiamo saccheggiato. Dovrai allenare la stealth se vorrai rubarlo.")
        print("Quindi mi serve almeno 6 di stealth per prendere l'occhio. In più qua posso guardare le stats")
        while fatto != True:
            laMiaScelta2 = input("\nInsomma che faccio? Guardo le mie stats, provo a usare la stealth, oppure torno nella stanza 3? (ss, sh, 3): ")
            if laMiaScelta2 == "ss":
                print("\nProviamo a vedere le mie stats: voglio vedere le mie statistiche! ")
                print("Ah, sh*t, here we go again! ")
                print(stats)
                if stats[0] < 6:
                    print("\nSono troppo debole, non posso andare avanti cosi!")
                else:
                    print("\nBene! Ora i miei bicipiti sono sazi!")
                
                if stats[1] < 6:
                    print("\nSono troppo stupido, non posso andare avanti cosi!")
                else:
                    print("\nBene! Ho studiato anche fin troppo!")
                
                if stats[2] < 6:
                    print("\nSono troppo rumoroso, non posso andare avanti cosi!")
                else:
                    print("\nBene! Sono abbastanza stealth da non dovermi più allenare!")
                    fatto = True

            elif laMiaScelta2 == "sh":
                print("\nDevo provare a rubare l'occhio...")
                print(". . . . .")
                if stats[2] >= 6:
                    if 1 in chiavi:
                        print("\nNon mi serve rubarne un'altro, ne ho già uno!")
                        print(chiavi)
                        fatto = True
                    else:
                        print("\nMeno male che mi sono allenato a rubare nella stanza di Assassin's Creed.")
                        print("Occhio, sto arrivando!")
                        print("\n Ok, devo fare piano, sennò i miei giochi finiscono qui.  É proprio lì davanti.. Non posso sbagliare... ")
                        print("....")
                        print("PRESA! OK facciamo veloce... ")
                        print(". . . . .")
                        print("*Hai trovato il secondo occhio!*")
                        chiavi.append(1)
                        print(chiavi)
                        fatto = True
                else:
                    print("\nNon posso rubare l'occhio, non mi sento pronto. Se lui mi vedesse provare a toccare il suo occhio dopo quello che gli ho fatto, mi ucciderebe al'istante... ")
                    fatto = True
            elif laMiaScelta2 == "3":
                print("\nSi, penso che non abbia da fare qua, torno nella stanza 3")
                fatto = True
            else:
                print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

    elif stanza == "4":
        print("\nOk, sono nella stanza di Assassin's Creed... Devo solo scoprire come prendere l'occhio e cosa posso allenare qui.") 
        print(""+nomeGiocatore+": 'Ehm, Ezio Auditore? Mi potresti dire dove posso trovare l'occhio e cosa posso allenare qui?' ")
        print("Ezio Auditore: 'Si, certo. In questa stanza puoi allenare la stealth, e per trovare l'occhio ti servirà 6 di strenght, per rompere il baule di ferro che vedi dietro di me")
        print(""+nomeGiocatore+": 'Non c'è una serratura da aprire, ooo un lucchetto da scassinare? Robe così...")
        print("Ezio Auditore: 'Se ci fosse pensi che sarebbe facile aprirlo? Penso proprio di si, per questo solo gli avventurieri più preparati possono riuscire a collezionare ciò che c'è al suo interno. ")
        print(""+nomeGiocatore+": 'Effettivamente... Va bene grazie Ezio...")
        while fatto != True:                   
            laMiaScelta3 = input("Ora che so cosa devo fare, devo decidere che fare: provo a scassinare il baule, alleno la stealth, oppure torno nella stanza 3? (b, s, 3): ")
            if laMiaScelta3 == "b":
                print("Perché non tentare? Tanto per stare qui a non fare niente...")
                if stats[0] >= 6:
                    if 2 in chiavi:
                        print("Ormai il baule è vuoto, ho già la chiave!")
                        print(chiavi)
                        fatto = True
                    else:
                        print("\nOK! A noi due baule di ferro!")
                        print("CLINK CLANK CLUNK")
                        print("RUMORE DI ANGELI CHE CANTANO PER FARE EFFETTO SCENICO")
                        print("É stato più facile del previsto! Meno male che mi sono allenato prima!")
                        print("*Hai trovato il secondo occhio!*")
                        chiavi.append(2)
                        print(chiavi)
                        fatto = True
                else:
                    print("\nNon ha senso provare a scassinare il baule! Non ho abbastanza forza, devo allenarla prima di tentare di scassinarlo...")
                    fatto = True
            elif laMiaScelta3 == "s":
                print("\nEzio Auditore: 'Hai deciso di allenarti con la stealth eh? Perfetto, ma non pensare mica che ti dica come farlo...")
                print("E adesso? Non so come allenare la stealth... Cosa posso fare? Ehy, aspeta. Devo anche allenare l'intelligenza, quindi devo per forze trovare una risposta!")
                print("pensa pensa pensa pensa...")
                print("*LAMPADINA CHE SI ACCENDE*")
                print("Ma certo! Devo rubare un i soldi dalle vecchiette, allenando cosi la mia stealth. Mi chiamavano piccolo genio...")
                print("Andiamo a rubbare...")
                print("\nTre o quattro furti dopo...")
                stats[2] = stats[2] + 1  
                print("ok, penso di essere migliorato!")
                print("Ora posso tornare nella stanza 3")
                fatto = True
            elif laMiaScelta3 == "3":
                print("\nNon ho tanto da fare qua, torno nella stanza 3")
                fatto = True
            else:
                print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente..." )

    elif stanza == "i":
        print("\nNon ho bisogno di muovermi, HO BISOGNO DI RISPOSTE!")
        print("Ma come posso fare...")
        print("Capo Villager: 'Se ti servono consigli per diventare più intelligente prova ad andare in biblioteca... ")
        print(""+nomeGiocatore+": 'Ah, ehm, si. Stavo solo ragionando. Ci avevo già pensato, giuro... ")
        stats[1] = stats[1] + 1
        print(". . . . .")
        print("Non sono male questi libri, sono semplicissimi e in appena un'ora ho già fatto molto. Però ora sono stanco, ci tornerò dopo...")
        print("Vediamo che posso fare ora...")

    else:
        print("Penso che tu abbia scritto male il comando oppure che tu l'abbia sbagliato totalmente...")

print("\nWAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP")
print("SBAM")
print(""+nomeGiocatore+": 'Quando è che toglierò questa sveglia? ")
print("Mamma: "+nomeGiocatore+"!! Svegliati su forza! Oppure non ne sei in grado dopo che hai passato tutta la notte a giocare?")
print("Tutta la notte a giocare? Ah si è vero, ho fatto la maratona stanotte...  ")
print("Ehy aspetta, era un sogno quello che ho fatto? Sono stato tutta la notte a giocare, no, non penso sia possibile... ")
print("Dalla lontanza: Ehy "+nomeGiocatore+"... ricordati che noi ci sAAHHHremo sempre per te...")
print("E-Era il capo dei villager quello? Amico, se eri tu, grazie...")
print(""+nomeGiocatore+": 'Arrivo mamma...")

print("\nThanks for playing! ")
print("Developers")
print("Bog e Ema")
print("Thanks to a lot of videogames and memes that helped us to create this game")
print("Expecially to Cory in the house and wake up guy ")
print("P.S: il verso del Capo dei Villager è il suo verso proprio, non è niente di sconcio o robe simili...")
######################################################################
if stats[0] > 15 and stats[1] > 15 and stats[2] > 15:
    print("oh well, now you are a boss of the gym")
    print("https://youtu.be/jhzzQd5hdCM%22")