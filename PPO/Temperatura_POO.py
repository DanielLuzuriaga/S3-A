print("UNIVERSIDAD ESTATAL AMAZONICA")
print("\nProgramación Tradicional Promedio de Temperaturas")
print("Autor: Daniel Luzuriaga")

# Clase padre para representar el clima diario
class ClimaDiario:
    def __init__(self, temperatura):
        # Propiedad de encapsulamiento: atributo protegido
        self._temperatura = temperatura

    def obtener_temperatura(self):
        return self._temperatura


# Clase hijo que se hereda de ClimaDiario
class ClimaSemana(ClimaDiario):
    def __init__(self):
        self._temperaturas = []

    # Metodo para ingreso de temperaturas diarias
    def ingresar_datos(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for dia in range(1, 8):
            temp = float(input(f"Día {dia}: "))
            self._temperaturas.append(ClimaDiario(temp))

    # Propiedad de polimorfismo: metodo con comportamiento propio
    def calcular_promedio(self):
        suma = 0
        for dia in self._temperaturas:
            suma += dia.obtener_temperatura()
        return suma / len(self._temperaturas)


# Clase principal
def main():
    clima = ClimaSemana()
    clima.ingresar_datos()
    promedio = clima.calcular_promedio()

    print(f"\nPromedio semanal de temperatura: {promedio:.2f} °C")


# Ejecución del programa
main()
