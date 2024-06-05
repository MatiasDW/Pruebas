print("¡Hola Te damos la más cordial bienvenida a Ruuf, tu aliado en la optimización de energía solar.")
print("Estamos emocionados de ayudarte a transformar tu espacio con la magia de los paneles solares.")      
print("Para comenzar, necesitamos conocer las dimensiones en metros de tu techo y qué tamaño de paneles solares tienes en mente.")      
print("Con esta información, podremos decirte cuántos paneles podrías instalar y así, juntos, daremos un paso más hacia un futuro más verde y sostenible.")


def best_fit_con_rotacion():
    X = int(input("Por favor, ingresa el ancho del techo: "))  # Width of the roof
    Y = int(input("Por favor, ingresa el alto del techo: "))  # Height of the roof
    a = int(input("Por favor, ingresa el ancho del panel solar: "))  # Width of the solar panel
    b = int(input("Por favor, ingresa el alto del panel solar: "))  # Height of the solar panel

    max_rects = 0
    # Check if the panel dimensions are greater than the roof dimensions
    if a > X or b > Y or a > Y or b > X:
        print("La cantidad máxima de paneles solares que caben en el techo es: ", max_rects)
        return

    # Try fitting without rotation
    max_rects_sin_rotar = (X // a) * (Y // b)
    # Try fitting with rotation
    max_rects_con_rotar = (X // b) * (Y // a)

    # Choose the maximum between both options
    max_rects = max(max_rects_sin_rotar, max_rects_con_rotar)

    # Check if rotating some rectangles can fit more
    espacio_restante_sin_rotar = X * Y - (max_rects_sin_rotar * a * b)
    espacio_restante_con_rotar = X * Y - (max_rects_con_rotar * b * a)

    if espacio_restante_sin_rotar >= b * a:
        max_rects += espacio_restante_sin_rotar // (b * a)
    elif espacio_restante_con_rotar >= a * b:
        max_rects += espacio_restante_con_rotar // (a * b)

    # Check if there is leftover space
    espacio_sobrante = (X * Y) % (a * b)
    if espacio_sobrante > 0:
        print("Hemos acomodado los paneles solares. Aún queda un espacio de", espacio_sobrante, " unidades cuadradas después de acomodar los paneles solares.")

    print("La cantidad máxima de paneles solares que caben en el techo es: ", max_rects)

# Example usage:
best_fit_con_rotacion()

#Techo triangular isosceles
def max_paneles_en_triangulo(base, altura, a, b):
    def paneles_en_fila(fila_ancho, panel_ancho):
        return fila_ancho // panel_ancho
    
    max_paneles = 0
    
    for fila in range(1, altura + 1):
        fila_ancho = (base * fila) // altura
        paneles_en_fila_sin_rotar = paneles_en_fila(fila_ancho, a)
        paneles_en_fila_con_rotar = paneles_en_fila(fila_ancho, b)
        
        max_paneles += max(paneles_en_fila_sin_rotar, paneles_en_fila_con_rotar)
    
    return max_paneles

# Ejemplo de uso
base_triangulo = 10
altura_triangulo = 5
ancho_panel = 2
alto_panel = 1

print(max_paneles_en_triangulo(base_triangulo, altura_triangulo, ancho_panel, alto_panel))

#Rectangulos superpuestos 
def max_paneles_superpuestos(x, y, a, b, d):
    def paneles_en_techo(techo_ancho, techo_alto, panel_ancho, panel_alto):
        return (techo_ancho // panel_ancho) * (techo_alto // panel_alto)
    
    # Paneles en el primer rectángulo
    max_paneles_1_sin_rotar = paneles_en_techo(x, y, a, b)
    max_paneles_1_con_rotar = paneles_en_techo(x, y, b, a)
    max_paneles_1 = max(max_paneles_1_sin_rotar, max_paneles_1_con_rotar)
    
    # Paneles en el segundo rectángulo superpuesto
    y_superpuesto = y - d
    max_paneles_2_sin_rotar = paneles_en_techo(x, y_superpuesto, a, b)
    max_paneles_2_con_rotar = paneles_en_techo(x, y_superpuesto, b, a)
    max_paneles_2 = max(max_paneles_2_sin_rotar, max_paneles_2_con_rotar)
    
    return max_paneles_1 + max_paneles_2

# Ejemplo de uso
x_techo = 10
y_techo = 5
ancho_panel = 2
alto_panel = 1
superposicion = 2

print(max_paneles_superpuestos(x_techo, y_techo, ancho_panel, alto_panel, superposicion))
