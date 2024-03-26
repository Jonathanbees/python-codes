def is_isogram(string):
    lowered = string.lower()
    print(lowered)
    letters = [
        "abcdefghijklmnopqrstuvwxyz"
    ]
    viewed_letters = []
    
    for i in lowered:
        #iterates over any letter in the string and checks if it is in the alphabet
        if i.lower() in letters[0]:
            if i.lower() in viewed_letters:
                return False
            #if the letter is not in the viewed_letters list, it is added to the list
            viewed_letters.append(i.lower())
        else:
            continue
    return True
# Test cases
print(is_isogram("isIsogram")) 
