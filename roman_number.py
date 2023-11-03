


def roman_number(number):

    number = number.upper()

    dictionary_values ={"I":1,
                        "V":5,
                        "X":10,
                        "L":50,
                        "C":100,
                        "D":500,
                        "M":1000}
    
    dictionary_constrains = {"IV":4,
                             "IX":9,
                             "XL":40,
                             "XC":90,
                             "CD":400,
                             "CM":900}

    sum = 0

    if len(number) == 1:
        sum += dictionary_values[number[0]]


    for i in range(len(number)-1):
        
        if i <= len(number)-2:
            print(sum)
            
            window = number[i:i+2]
            window_next = number[i+1:i+3]
            window_pre = number[i-1:i+1]
            print(window)
            if window in dictionary_constrains:
                sum +=  dictionary_constrains[window]
            
            elif window_next in dictionary_constrains and window_pre not in dictionary_constrains and i == 0:
                sum += dictionary_values[window[0]]
            elif window_next in dictionary_constrains and window_pre not in dictionary_constrains:
                sum += 0
            
            elif window_pre in dictionary_constrains and window_next in dictionary_constrains:
                
                sum += 0
            
            elif i > 0:
                sum += dictionary_values[window[1]]

            else:
                sum += dictionary_values[window[0]] + dictionary_values[window[1]]

        else:

            window = number[i:i+2]
            
            if window in dictionary_constrains:
                sum +=  dictionary_constrains[window]
                    
            elif i > 0:
                sum += dictionary_values[window[1]]

            else:
                sum += dictionary_values[window[0]] + dictionary_values[window[1]]

    return sum

if __name__ == "__main__":
    test = roman_number("D")
    print(test)