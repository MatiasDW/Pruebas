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

