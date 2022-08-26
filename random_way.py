import random
from position import Position
""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)
    def __repr__(self):
        return 'Person({!r}, {!r})'.format(self.name, self.age)
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age
    def __le__(self, other):
        return self.age <= other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __ne__(self, other):
        return self.age != other.age
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.age - other.age
    def __mul__(self, other):
        return self.age * other.age
    def __truediv__(self, other):
        return self.age / other.age
    def __floordiv__(self, other):
        return self.age // other.age
    def __mod__(self, other):
        return self.age % other.age
    def __divmod__(self, other):
        return divmod(self.age, other.age)
    def __pow__(self, other):
        return self.age ** other.age
    def __lshift__(self, other):
        return self.age << other.age
    def __rshift__(self, other):
        return self.age >> other.age
    def __and__(self, other):
        return self.age & other.age
    def __xor__(self, other):
        return self.age ^ other.age
    def __or__(self, other):
        return self.age """

class B:
    def __init__(self, name, position):
        self.name = name
        self.position = Position(0,0)

class B2(B):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

def main():
    pass

if __name__ == '__main__':
    main()


""" 
from borracho import BorrachoTradicional
from campo import Campo 
from coordenada import Coordenada 

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional) """