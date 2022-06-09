class Vehiculo:
    _color = None
    _ruedas = None
    _puertas = None

class Coche(Vehiculo):
    _velocidad = 220
    _cilindrada = 6

miCoche = Coche()

miCoche._color = "Negro"
miCoche._ruedas = 4
miCoche._puertas = 4

print("Color de auto: ", miCoche._color)
print("Cantidad de ruedas: ", miCoche._ruedas)
print("Cantidad de puertas: ", miCoche._puertas)
print("Velocidad: ", miCoche._velocidad)
print("Cilindradas: ", miCoche._cilindrada)