alien_alphabet = "zyxwvutsrqponmlkjihgfedcba"

alien_index = [x for x in range(len(alien_alphabet))]

alien_dictionary = {k:v for (k,v) in zip(alien_alphabet, alien_index)}


human_alphabet = "abcdefghijklmnopqrstuvwxyz"

human_index = [x for x in range(len(human_alphabet))]

human_dictionary = {k:v for (k,v) in zip(human_alphabet, human_index)}


def test_order(alphabet, word_list):

    word_list = [element.lower() for element in word_list]
    
    for i in range(len(word_list)-1):
        
        main_word = word_list[i]
        secondary_word = word_list[i+1]
        

        for z in range(len(main_word)):
            
            if (z == len(secondary_word)-1) and (len(secondary_word) < len(main_word)):
                
                return False
                 
            elif alphabet[main_word[z]] == alphabet[secondary_word[z]]:
                pass
            
            elif alphabet[main_word[z]] < alphabet[secondary_word[z]]:
                break

            else:
                return False

    return True

palabras = [ "arbitro","conocer" ,"cono"]

test = test_order(human_dictionary,palabras)
print(test)