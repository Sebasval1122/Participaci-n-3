import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

punto1 = Punto(15, 6)
punto2 = Punto(20, 4)

punto1.mover(6, 15)
punto2.mover(6, 15)

print("Coordenadas del punto 1:", punto1)
print("Coordenadas del punto 2:", punto2)
print("Distancia entre los dos puntos:", punto1.distancia(punto2))