b=int(input('Base: '))
h=int(input('Altezza: '))

for i in range(h):
    for j in range(b):
        if i==0 or i==h-1 or j==0 or j==b-1:
            print('* ', end=' ')
        else:
            print('  ', end=' ') #due spazi vuoti all’interno degli apici
    print()