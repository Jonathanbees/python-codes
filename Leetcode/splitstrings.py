def solution(s):
    print(len(s))
    storednumbers = []
    if len(s) % 2 != 0:
        s+= '_'
        for i in range(len(s)):
            if i % 2 == 0:
                storednumbers.append(s[i] + s[i+1])
    elif (len(s)) == 0:
        return storednumbers
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                storednumbers.append(s[i] + s[i+1])
    
    #print(storednumbers)
    return storednumbers
solution('abcdef') # Should return ['ab', 'cd', 'e_']

"""
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
"""

