
def likes(names: list):
    frase = ""
    resto = str(len(names)-2)
    if len(names) == 0:
        return "no one likes this"
    for i in range(len(names)):
        if len(names) == 1:
            frase = names[i] + " likes this"
            break
        if len(names) == 2:
            frase = names[i] + " and " + names[i+1] + " like this"
            break
        if len(names) == 3:
            frase = names[i] + ", " + names[i+1] + " and " + names[i+2] + " like this"
            break
        if len(names) > 3:
            if i > 1:
                frase += " and "+ resto + " others like this"
                break
            frase+= ", "+names[i]
    if frase[0] == "," or frase[0] == " ":
        frase = frase[2:]
    #print(frase)
    return frase
likes(['Alex', 'Jacob', 'Mark', 'James', 'esteban'])

'''
Optimized solution:
'''
def likes2(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
likes2(['Alex', 'Jacob', 'Mark', 'James', 'esteban'])