#4.1
##def soma (lista):
##    if lista == []:
##        return 0
##    return lista[0] + soma(lista[1:])
##print (soma([2,4,6]))

#4.2
##def conta(lista):
##    if lista == []:
##        return 0
##    return 1 + conta(lista[1:])
##print (conta([2,4,6]))

#4.3
#def maior(lista):
 #   if len(lista) == 2:
 #       return lista[0] if lista[0] > lista[1] else lista[1]
 #   sub_max = maior(lista[1:])
 #   return lista[0] if lista [0] > sub_max else sub_max
#print (maior([2,25,6]))

#def quicksort (array):
#    if len(array) < 2:
 #       return array
#    if array[0] > array[1]:
#        return array[0]
#    return array[1]
#print (quicksort([120,87]))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
