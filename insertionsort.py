def insertionSort(lista):
    
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        
        while j>= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j = j - 1
            
        lista[j+1] = key
        

array = [5, 6, 1, 9, 7]
insertionSort(array)
print(array)
