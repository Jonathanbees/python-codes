from math import sqrt
def is_square(n):
    if n < 0:
        return False    
    if sqrt(n) % 1 == 0:
        return True
    else:
        return False
print(is_square(25))
print(is_square(26))
