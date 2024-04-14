def solution(s):
    dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(len(s)):
        if s[i] in dictionary:
            result += " "  # Agrega un espacio antes de las letras mayúsculas
        result += s[i]  # Agrega el carácter actual a la cadena resultante
    print(result)
    return result

solution("camelCasing")  # Debería devolver "camel Casing"