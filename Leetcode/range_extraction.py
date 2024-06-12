def solution(lista):
    if len(lista) < 1:
        return ""
    string = ""
    temporal = []
    temporal.append(lista[0])
    string+=str(temporal[0])
    #string+=str(lista[i])
    lista.pop(0)
    for i in lista:
        print(abs(temporal[0]) - abs(lista[i]))
        if (abs(abs(temporal[0]) - abs(lista[i]))) > 1 and (abs(abs(temporal[0]) - abs(lista[i]))) < 3:
            string = string + "-" + str(lista[i])
            print(string)
            temporal.append(lista[i])
            temporal.pop(0)
            print(temporal)
            lista.pop(0)
        
        elif (abs(abs(temporal[0]) - abs(lista[i]))) > 1 and (abs(abs(temporal[0]) - abs(lista[i]))) > 3:
            string = string + "-" + str(lista[i]) + "si"
            print(string)
            temporal.append(lista[i])
            temporal.pop(0)
            print(temporal)
    print(string)

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])