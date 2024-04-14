def count_bits(n):
    number = str(bin(n))
    #print(type(number))
    counter = 0
    for i in (number):
        if i == "1":
            counter+=1
    #print(counter)
    return counter
count_bits(4)
