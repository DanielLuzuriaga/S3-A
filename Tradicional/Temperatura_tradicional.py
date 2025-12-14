print("UNIVERSIDAD ESTATAL AMAZONICA")
print("\nProgramación Tradicional Promedio de Temperaturas")
print("Autor: Daniel Luzuriaga")

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("\nIngrese las temperaturas diarias de la semana:")

    for dia in range(1, 8):
        temp = float(input(f"Día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función principal
def main():
    temperaturas_semana = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas_semana)

    print("\nTemperaturas ingresadas:", temperaturas_semana)
    print(f"Promedio semanal de temperatura: {promedio_semanal:.2f} °C")


# Ejecución del programa
main()
