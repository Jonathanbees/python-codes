def to_jaden_case(string):
    lista = string.split()
    nuevalista = []
    for i in lista:
        i = i.capitalize()
        nuevalista.append(i)
    return ' '.join(nuevalista)

to_jaden_case("How can mirrors be real if our eyes aren't real") # How Can Mirrors Be Real If Our Eyes Aren't Real