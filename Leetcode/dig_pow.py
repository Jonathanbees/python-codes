def dig_pow(n,p):
    nums = []
    number = int(n)
    while n > 0:
        nums.append(n % 10) # Stores the last digit of the number
        n = n // 10 # Removes the last digit of the number
    nums.reverse() # Reverses the list
    suma = 0
    for i in range(len(nums)):
        suma += nums[i] ** (p+i) #apply the ecuation to elevate each number
    #print(suma)
    #print(number)
    resultado = suma//number #This would be k
    #print(resultado)
    if resultado*number == suma: #This have to be the same number, like the example
        return resultado
    else:
        return -1

dig_pow(46288, 3)