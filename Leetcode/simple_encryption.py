def decrypt(encrypted_text, n):
    if encrypted_text == "" or n <= 0:
        return encrypted_text
    
    while n > 0:
        i = 0
        texto = encrypted_text
        encrypted_text = list(encrypted_text)
        total = []
        listaimpares = []

        largo = len(texto)
    
        for i in range(len(encrypted_text)//2):
            listaimpares.append(texto[i])
            encrypted_text.pop(0)
        #print(len(encrypted_text))
        
        i = 0
        while i < len(encrypted_text)-1:
            total+=(encrypted_text[i])
            total+=(listaimpares[i])
        #print(total)
            #print(i)
            i+=1
        #print(listaimpares)
        #print(encrypted_text)
        #encrypted_text = texto
        #encrypted_text = list(encrypted_text)
        n-=1
        #print(i)
        #print(encrypted_text[i])
        if largo % 2 != 0:
            total+= texto[-1]
        else:
            total+= encrypted_text[-1]
            total+= listaimpares[-1]
        encrypted_text = "".join(total)
        
    #print(i)
    #print(total)
    return "".join(total)


def encrypt(text, n):
    if text == "" or n == 0:
        return text
    total = []
    listaimpares = []
    listapares = []
    while n > 0:
        textootro = ""
        for i in range(len(text)):
            if i % 2 != 0:
                textootro += text[int(i)]
                listaimpares.append(text[int(i)])
        for i in range(len(text)):
            if i % 2 == 0:
                textootro += text[int(i)]
                listapares.append(text[int(i)])
        n-=1
        text = textootro
    total = total+ listaimpares + listapares
    #print(text)
    return text


message = encrypt("This kata is very interesting!", 1)
decrypt(message, 1)
'''
def encrypt(text, n):
    total = []
    listaimpares = []
    listapares = []
    while n > 0:
        textootro = ""
        for i in range(len(text)):
            if i % 2 != 0:
                textootro += text[int(i)]
                listaimpares.append(text[int(i)])
                dictionary.append(text[int(i)])
                dictionary.append(int(i))
        for i in range(len(text)):
            if i % 2 == 0:
                textootro += text[int(i)]
                listapares.append(text[int(i)])
                dictionary.append(text[int(i)])
                dictionary.append(int(i))
        #print(textootro)
        n-=1
        text = textootro
    total = total+ listaimpares + listapares
    print(total)
    #print(total)
    #print(dictionary)
    #print(type(dictionary))
    print(text)

    otralista = []
    i = 0
    while len(otralista) < len(text):
        if i in dictionary:
            print("sisas pa")
            indice = dictionary.index(i)
            print(indice)
            otralista.append(dictionary[indice-1])
        i+=1
    print(otralista)

    return text
'''