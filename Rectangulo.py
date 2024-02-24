class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def perimetro(self):
        base = self.esquina2[0] - self.esquina1[0]
        altura = self.esquina2[1] - self.esquina1[1]
        p = 2 * (base + altura)
        return p

    def area(self):
        base = self.esquina2[0] - self.esquina1[0]
        altura = self.esquina2[1] - self.esquina1[1]
        area = base * altura
        return area

    def es_cuadrado(self):
        base = self.esquina2[0] - self.esquina1[0]
        altura = self.esquina2[1] - self.esquina1[1]
        return base == altura

# Crear instancias de Rectangulo
esquina1 = (15, 6)
esquina2 = (15, 6)
mi_rectangulo = Rectangulo(esquina1, esquina2)

# Mostrar información sobre el rectángulo
print("Esquina uno:", esquina1)
print("Esquina dos:", esquina2)
print("Perímetro:", mi_rectangulo.perimetro())
print("Área:", mi_rectangulo.area())
if mi_rectangulo.es_cuadrado():
    print("El rectángulo es también un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
