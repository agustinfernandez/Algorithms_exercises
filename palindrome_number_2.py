def palindrome(X):

    if x < 0 or (x != 10 and x % 10 == 0):
        return False
    
    var = 0
    while var < x:

        var = (var * 10) + (x % 10)
        x = x // 10

        if (x == var) or (x == var//10 ):
            return True

