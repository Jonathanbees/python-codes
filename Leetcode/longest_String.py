def longest(a1, a2):
    sorted = a1 + a2
    sorted = list(set(sorted)) # El metodo set() elimina los elementos duplicados de la lista
    sorted.sort() #Ordena los elementos
    sorted = ''.join(sorted) # los concatena en un string
    return sorted

print(longest("aretheyhere", "yestheyarehere")) # "aehrsty"