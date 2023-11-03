def mov_zeros(lista):

    first_index = 0 
    second_index= 1
    
    for i in range(1,len(lista)):
        
        if len(lista) == 1:
            return lista

        elif lista[first_index] == 0 and  lista[second_index] != 0 and second_index == len(lista)-1:

            lista[first_index], lista[second_index]= lista[second_index], lista[first_index]

            return lista

        elif lista[first_index] == 0 and  lista[second_index] != 0:

            lista[first_index], lista[second_index]= lista[second_index], lista[first_index]

            first_index += 1
            second_index += 1
        
        elif lista[first_index] == 0 and  lista[second_index] == 0:

            second_index += 1

        elif  lista[first_index] != 0:

            first_index += 1
            second_index += 1
    return lista

move = mov_zeros([0])
print(move)


