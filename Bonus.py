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
