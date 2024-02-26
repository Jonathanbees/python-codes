def square_digits(num):
    s = ''
    for i in str(num):
        s = s+str(int(i)**2)
    return int(s)
print(square_digits(9119))