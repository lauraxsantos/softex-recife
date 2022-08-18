lista = []
from random import randint
    
while len(lista) < 30:
    
    item = randint(0,30)
    if item % 2 != 0:
        lista.append(item)
    
print(lista)

for i in range(1, len(lista)):
    key = lista[i]
    j = i - 1
        
    while j>= 0 and key < lista[j]:
        lista[j+1] = lista[j]
        j = j - 1
            
    lista[j+1] = key
        

print(lista)

