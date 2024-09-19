def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] == s[-1]:
        print(s[1:-1])
        return palindrome(s[1:-1])
    else:
        return False

def FizzBuzz(n):
    for i in range(1,n+1):
        #print (i)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return ""

def Anagramas(s):
    print(s)
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict:
        print(i, dict[i])
    if len(dict) % 2 == 0:
        for i in dict:
            if dict[i] % 2 != 0:
                return False
        return True

def main():
    #n = int(input())
    #print(fibonnacci(n))
    #s = input("decime un string mi rey")
    #print(palindrome(s))
    #m = int(input("Decime un numero para fizzbuzz"))
    #print(FizzBuzz(m))
    s = input("dime el anagrama pa, sin puntos ni comas para este caso de mayor facilidad")
    print(Anagramas(s))

main()
