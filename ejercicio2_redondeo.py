from Ejercicio_redondeo.funcion_redondeo import redondear

def suma_redondeo(num1, num2):
    suma = num1 + num2
    return redondear(suma)

numero1 = float(input("Ingrese el primer numero decimal: "))

numero2 = float(input("Ingrese el segundo numero decimal: "))

resultado = suma_redondeo(numero1, numero2)

print(f"La suma redondeada es: {resultado}")