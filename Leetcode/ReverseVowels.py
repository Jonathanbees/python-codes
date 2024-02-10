import threading
import queue

q = queue.Queue()
class Solution:
    def reverseVowels(self, s: str) -> str:
        lowercase = s.lower()
        vowels = "aeiou"
        vowelscapital = "AEIOU"
        lista = list(s)

        posicionesj = []

        """Pruebas"""

        print(lista)
        for j in range(len(lista)-1, -1, -1):
            if lista[j] in vowels or lista[j] in vowelscapital:
                print("Elemento j",lista[j],"indice j",j)
                posicionesj.append(lista[j])
                q.put(j)
        print("Posicionesj",posicionesj)
        print("Queue",q.queue)
        for i in range(len(lista)):
            if lista[i] in vowels or lista[i] in vowelscapital:
                print("Elemento i",lista[i])
                lista[i] = posicionesj.pop(0)
                print("La lista hasta el momento es:", lista[:i])
        print("Lista",lista)
        return ''.join(lista)



"""2
        for i in range(len(lista)-1):
            if lista[i] in vowels:
                print("Elemento i",lista[i])
                posicionesi.append(i)
        print(posicionesi)

        for i in range(len(lista)-1):
            lista[i]
            #lista[i], lista[posicionesj[i]] = lista[posicionesj[i]], lista[i]
        return ''.join(lista)
"""
"""

        for i in range(len(lista)-1):
            if lista[i] in vowels:
                print("Elemento i",lista[i])
                for j in range(len(lista)-1, -1, -1): #No me recorre el segundo ciclo por el break, pero tampoco me cambia las vocales correctamente
                    if lista[j] or lista[j-1] in vowels:
                        print("Elemento j",lista[j])
                        lista[i], lista[j] = lista[j], lista[i]
                    break
        
        return ''.join(lista)
"""     

# Test cases

print(Solution().reverseVowels("aA"))  # leotcede
