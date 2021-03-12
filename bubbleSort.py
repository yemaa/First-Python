#Input variabili
x = float(input("Dimmi un numero: "))
y = float(input("Dimmene un altro: "))
z = float(input("Dimmene un altro ancora: "))

#Controllo ordine numeri
if y > z:
    a = y
    y = z 
    z = a

if x > y:
    b = x
    x = y
    y = b

if z < y:
    c = y
    y = z
    z = c

#Stampa a schermo dei numeri
print("Ecco i tuoi numeri ordinati in ordine crescente:",x,y,z)