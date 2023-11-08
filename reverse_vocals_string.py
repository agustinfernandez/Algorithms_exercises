def reverse_vocal(s):
    
    s = [x for x in s]

    vocals_dict = {"a":1, "e":2, "i":3, "o":4,"u":5, "A":6, "E":7, "I":8,"O":9,"U":10}
    
    first_index = 0
    second_index= len(s)-1

    while first_index < second_index:
        
        if s[first_index] in vocals_dict and s[second_index] in vocals_dict:

            s[first_index], s[second_index] = s[second_index], s[first_index]

            first_index += 1
            second_index += -1

        
        elif s[first_index] in vocals_dict and s[second_index] not in vocals_dict:

            second_index += -1

        else:

            first_index += 1
    
    return "".join(s)

if __name__ == "__main__":
    print(reverse_vocal("leetcode"))