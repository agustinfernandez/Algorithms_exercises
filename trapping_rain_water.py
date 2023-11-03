def rain_water(lista):

    total = 0
    index_first = 0 
    index_second= 1
    first_limit = lista[index_first] 
    last_limit = lista[index_second]
    previous_total = 0
    middle_total = 0

    for i in range(1,len(lista)):
        

        if i == len(lista)-1 and first_limit > last_limit:
            total += middle_total
            return total
        
        elif first_limit <= last_limit and i == len(lista)-1:
            total += previous_total
            return total


        elif first_limit <= last_limit :
            
            total += previous_total
            previous_total = 0
            middle_total = 0
            first_limit = last_limit
            index_second = index_second+1
            last_limit = lista[index_second]

        else:
            
            previous_total +=  first_limit - last_limit

            if lista[index_second-1] > last_limit and lista[index_second+1] > last_limit:
                
                middle_total += min(lista[index_second-1],lista[index_second+1]) - last_limit
            
            index_second = index_second  + 1
            last_limit = lista[index_second]
    
    return total

if __name__ == "__main__":
    
    trapping = rain_water([0,1,0,2,1,0,1,3,2,1,2,1,3])
    print(trapping)
