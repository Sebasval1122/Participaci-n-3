class Carta:
    
    CORAZON = 'Corazón'
    DIAMANTE = 'Diamante'
    TREBOL = 'Trébol'
    ESPADA = 'Espada'

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


mi_carta = Carta(8, Carta.CORAZON)
print("Valor de la carta:", mi_carta.valor)
print("Pinta de la carta:", mi_carta.pinta)
