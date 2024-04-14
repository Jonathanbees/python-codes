"""
def generate_hashtag(s: str):
    print(len(s))
    if len(s) > 141:
        return False
    if len(s) == 1 or len(s) == 0:
        return False
    s = s.strip()
    """
'''
    if s[0] != s[0].upper():
        s = s[0].upper() + s[1:]
    '''
"""
    #print(s)
    #print(len(s))
    length = len(s) - 1
    #print(length)
    s = s.lower()
    lista = s.split(' ')
    print(lista)
    print(len(lista))
    for i in range(len(lista)):
        if lista[i] == '':
            del lista[i]
    print(lista)
    
    for i in range(len(lista)):
        lista[i] = lista[i][0].upper() + lista[i][1:]
    #print(lista)
    s = "#" + "".join(lista)
    if len(s) > 142:
        return False
    print(s)
    return s
    

generate_hashtag("LoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongCat")
    
print(len("#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))
"""
def generate_hashtag(s: str):
    s = s.strip()
    if len(s) == 0:
        return False
    words = s.split(' ')
    words = [word.capitalize() for word in words if word]  # Capitalize each word and ignore empty strings
    hashtag = "#" + "".join(words)
    if len(hashtag) > 140:
        return False
    return hashtag

"""
s = s.split()
    if len(s) > 140 or not (s):
        return False
    ans = '#'
    for word in s:
        ans += word.title()
    if len(ans) > 140 or not (s):
        return False
    return ans
    
"""