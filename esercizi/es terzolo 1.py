a = 10
print(a , type(a))

a = 'ciao come stai'
print(a, type(a))

print('-------------------------------------------------------------------------------')

lista_nomi = ['mario', 'carlo', 'daniele', 'matteo']

numero_nomi = len(lista_nomi)

if numero_nomi < 4:
    print('lista corta')
else: 
    print('lista abbastanza lunga')

if 'daniele' in lista_nomi:
    print('esiste pure giuseppe')

for n in lista_nomi:
    print(n)





