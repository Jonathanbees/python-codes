def draw_pyramid(n):
    height = 2*n
    width = (3*(n-1) + 1) + 3 + height - 1
    print(width)

    #Nota reconocimiento patrón 2: (tener en cuenta que estoy contando de abajo para arriba la altura) 
    #imprimir _, esta se imprime a partir de la línea h hasta h=2

    return '\n'.join([
        " ./\\ ",
       "\\/__\\"])
"""
print('''
    ./\   
 .´\/__\  
\´\/__:_\ 
 \/_|__|_\\
'''.replace(' ', '*'))
"""
draw_pyramid(4)