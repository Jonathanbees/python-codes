def draw_pyramid(n):
    height = 2*n
    width = (3*(n-1) + 1) + 3 + height - 1
    print(width)
    for i in range(height, 0, -1):
        if i == height-1:
            print('\\' + "/" + "__")
        else:
            print("*"*width)

    #Nota reconocimiento patrón 2: (tener en cuenta que estoy contando de abajo para arriba la altura) 
    #imprimir _, esta se imprime a partir de la línea h hasta h=2
    #otro patron: _ se garantiza que SIEMPRE estará antes de cerrar la pirámide \, y la cantidad de _ que se imprimen por linea (de abajo hacia arriba) es height sumando el _ adicional al lado de \

    #return '\n'.join([
    #    " ./\\ ",
    #   "\\/__\\"])
"""
print('''
    ./\   
 .´\/__\  
\´\/__:_\ 
 \/_|__|_\\
'''.replace(' ', '*'))
"""
    
draw_pyramid(1)

def generate_sequence_excluding_modulo(n, mod, exclude):
    sequence = []
    i = 0
    while len(sequence) < n:
        if i % mod != exclude:
            sequence.append(i)
        i += 1
    return sequence

n = 10  # Número de términos deseados
sequence = generate_sequence_excluding_modulo(n, 6, 1)
print(sequence)