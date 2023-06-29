def find_prime(value):
    if value % 2 == 0 or value % 3 == 0 or value % 4 == 0 or value % 5 == 0:
        return("Not a prime")
    else:
        return("Prime")
 