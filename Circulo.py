import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def area(self):
        area = self.radio ** 2 * math.pi
        print("El área es de:", area)
    
    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print("El perímetro es de:", perimetro)
    
    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_centro_punto <= self.radio


radio = float(input("Ingrese el radio: "))
centro_x = float(input("Ingrese la coordenada x del centro: "))
centro_y = float(input("Ingrese la coordenada y del centro: "))

circulo = Circulo((centro_x, centro_y), radio)


punto_x = float(input("Ingrese la coordenada x del punto a verificar: "))
punto_y = float(input("Ingrese la coordenada y del punto a verificar: "))


circulo.area()
circulo.perimetro()


if circulo.punto_pertenece((punto_x, punto_y)):
    print(f"El punto ({punto_x}, {punto_y}) está dentro del círculo.")
else:
    print(f"El punto ({punto_x}, {punto_y}) está fuera del círculo.")
