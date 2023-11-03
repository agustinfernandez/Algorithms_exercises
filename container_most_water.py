def container(lista):

    area = 0
    index_first = 0 
    index_second= -1
    
    for i in range(len(lista)):
        

        if index_first == len(lista)+index_second:
            return area
        
        else:

            first_element = lista[index_first]
            last_element=lista[index_second]
            base = (len(lista)-1) - i 
            

            if first_element < last_element:
                
                height =  first_element
                index_first = index_first+1    

            elif first_element == last_element:

                height = first_element
                index_first = index_first+1

            else:
                height =  last_element 
                index_second = index_second-1
           
            
            if base * height > area:
                area = base * height

            else:
                area = area
    return area

cont = container([1,8,6,2,5,4,8,3,7])
print(cont)



        