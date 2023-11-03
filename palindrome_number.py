def palindrome(number):
    number_str= str(number)
    
    if number_str[0] =="-":
        return False

    if number_str[0] =="0":
        number_str = number_str[1:]
    
    if len(number_str) % 2 != 0:
        
        last_character =number_str[-1]
        index_last_character = number_str.rfind(last_character)
        medium = index_last_character // 2
        
        left_list= number_str[:medium]
        right_list= number_str[medium+1:]
        print(left_list)
        print(right_list)

        for i in range(len(left_list)):

            if left_list[i] == right_list[-1-i]:
                pass
            else:
                return False
        
        return True            

    else:
        medium = len(number_str) // 2
        left_list= number_str[:medium]
        right_list= number_str[medium:]
        

        for i in range(len(left_list)):
            
            if left_list[i] == right_list[-1-i]:
                
                pass
            else:
                return False
        
        return True


palindro= palindrome(1233321)
print(palindro) 


#-------------------------------------#

def more_simple_solution(numb):

    x = str(x)
    return x == x[::-1]