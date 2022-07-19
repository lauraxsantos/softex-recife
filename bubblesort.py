lista = [6, 8, 1, 9]
print(lista)

c = 0
vezes = 0

while True:

    if lista[c] > lista[c+1]:
        temp = lista[c]
        lista[c] = lista[c+1]
        lista[c+1] = temp
   
   c += 1
    
    if c == len(lista)-1:
        c = 0
        vezes += 1
        
    if vezes == len(lista):
        break

print(lista)
