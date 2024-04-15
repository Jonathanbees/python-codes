def order(sentence):
    if sentence == "":
        return ""
    counter = 1
    nuevalista = []
    array = sentence.split()
    i = 0
    while len(nuevalista) < len(array):
        if str(counter) in array[i]: #need to compare the counter bc this filters me how many strings do i have previously
            nuevalista.append(array[i]) # if the number is in the position of the array, put that in the new array solution
            counter +=1
            i=0 #and reinitializes the process
        else:
            i+=1
    return " ".join(nuevalista)
order("is2 Thi1s T4est 3a")