def solution(number):
    if number < 0:
        return 0
    suma = 0
    for i in range(number):
        if i == 0 or i==1:
            pass
        else:
            if (i % 3 == 0 or i % 5 == 0):
                suma += i
    #print(suma)
    return suma

