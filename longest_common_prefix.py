def common_prefix(lista):
    common_letters = ""

    for i in range(len(lista)):
        
        if lista[i] == "":
            return ""
        
        elif len(lista) == 1:
            return lista[0]

        
        if i == 0:
            
            
            if len(lista[i]) > len(lista[i+1]):

                for x in range(len(lista[i+1])):

                    if lista[i][x] != lista[i+1][x] and x == 0:
                        return ""
                    
                    elif lista[i][x] != lista[i+1][x] and x > 0:
                        common_letters = common_letters
                        break

                    elif lista[i][x] == lista[i+1][x]:    
                        common_letters += lista[i][x] 
            
            else:

                for x in range(len(lista[i])):
                    
                    if lista[i][x] != lista[i+1][x] and x == 0:
                        return ""
                    
                    elif lista[i][x] != lista[i+1][x] and x > 0:
                        common_letters = common_letters
                        break

                    elif lista[i][x] == lista[i+1][x]:    
                        common_letters += lista[i][x]
        
        elif i == 1:
            pass
        
        
        else:
            if len(common_letters) < len(lista[i]):
                for z in range(len(common_letters)):

                    if common_letters[z] == lista[i][z]:
                        common_letters = common_letters
                    elif  common_letters[z] != lista[i][z] and z > 0:
                        common_letters= common_letters[:z]
                        break
                    else:
                        return ""
            else:
                for z in range(len(lista[i])):
                    print(i,z,common_letters)
                    if common_letters[z] == lista[i][z] and len(lista[i]) >1:
                        common_letters = common_letters

                    elif common_letters[z] == lista[i][z] and len(lista[i]) == 1:
                        common_letters = common_letters[0]


                    elif  common_letters[z] != lista[i][z] and z > 0:
                        common_letters= common_letters[:z]
                        break
                    else:
                        return ""


    return common_letters


list = ["acabado","aca","ac","a"]
common = common_prefix(list)
print(common)




