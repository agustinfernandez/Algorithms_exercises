def reverse_string(s):

    i = 0 
    
    while i < len(s)-i:
        
        s[i], s[-1-i] = s[-1-i], s[i]
        i += 1
    
    return s

if __name__ == "__main__":
    test = reverse_string(["H","a","n","n","a","h"])
    print(test)