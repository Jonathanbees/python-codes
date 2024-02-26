def friend(x):
    nueva_lista = [i for i in x if len(i) == 4]
    return nueva_lista
print(friend(["Ryan", "Kieran", "Mark", "Jimmy"])) # ["Ryan", "Mark"]
