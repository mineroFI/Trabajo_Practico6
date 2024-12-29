""" Trabajo Practico N°6
Nombre y Apellido: Navarro Ana Florencia
Comisión: Jueves - virtual
tips:
- para comentar codigo se usa # o comillas triples 
- si se usa vscode, se puede usar el comando ctrl+k, ctrl+c
"""

"""
Ejercicio 01: Escriba una función redondear() que permita redondear un número 
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el 
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente 
anterior (3).
"""
# import math

# def redondear(x):
#     if x > 3.50:
#         return math.ceil(x)
#     else:
#         return math.floor(x)
    

# numerox = float(input("Ingrese un numero decimal: "))

# resultado = redondear(numerox)

# print(f"El número redondeado es: {resultado}")


"""
Ejercicio 02: Coloque el módulo del ejercicio anterior dentro de un paquete. En un 
módulo que esté fuera de ese paquete, cree una función de suma de 
decimales que redondee el resultado haciendo uso de la función 
redondear() del paquete recién creado.
"""
# El ejercicio esta en la carpeta paquete_ejercicio2_redondeo junto con el archivo ejercicio2


"""
Ejercicio 03: Usando el módulo datetime, escribe un programa que muestre la fecha 
y hora actuales del sistema
"""
# import datetime

# fecha = datetime.datetime.now()

# print(f"Fecha y hora actual:" , fecha)


"""
Ejercicio 04: Escriba un programa que devuelva un número par al azar entre 2 y 10 
(pista: para comprobar si se pueden generar todos los números, pruebe 
ejecutar el programa dentro de un ciclo infinito).
"""

# import random

# while True:
#     numero_azar = random.randint(2, 10)
#     if numero_azar % 2 == 0: # verificar si numero es par
#         print(f"Número aleatorio par: {numero_azar}")
#         break

"""
Ejercicio 05: Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado 
para la adivinación o para buscar consejo. Su mecanismo es muy simple: 
ante una pregunta del usuario, la bola responde con una de 8 posibles 
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica
"""

# import random

# def bola_magica():
#     opciones = [
#         "Es seguro que sí",
#         "Las chances son buenas",
#         "Puedes contar con ello",
#         "Pregúntame de nuevo más tarde",
#         "Concéntrate y pregunta de nuevo",
#         "No veo con claridad, intenta de nuevo",
#         "Mi respuesta es no",
#         "Mis fuentes me dicen que no"
#     ]
#     return random.choice(opciones)

# Pregunta = input("Preguntale algo a la bola magica: ")

# respuesta = bola_magica()

# print(f"La bola magica responde: {respuesta}")

"""
Ejercicio 06: Encuentre el tiempo de ejecución de los programas de los ejercicios 
anteriores (pista: use el módulo time)
"""
# import time
# start_time = time.time()

"""ejercicio 1"""

# import math

# def redondear(x):
#     if x > 3.50:
#         return math.ceil(x)
#     else:
#         return math.floor(x)
    

# numerox = float(input("Ingrese un numero decimal: "))

# resultado = redondear(numerox)

# print(f"El número redondeado es: {resultado}")

# end_time = time.time()

# print(f"Tiempo de ejecución: {end_time - start_time} segundos")

"""ejercicio 2"""

# import time
# start_time = time.time()

# from paquete_ejercicio2_redondeo.redondear import redondear

# def suma_redondeo(num1, num2):
#     suma = num1 + num2
#     return redondear(suma)

# numero1 = float(input("Ingrese el primer numero decimal: "))

# numero2 = float(input("Ingrese el segundo numero decimal: "))

# resultado = suma_redondeo(numero1, numero2)

# print(f"La suma redondeada es: {resultado}")

# end_time = time.time()

# print(f"Tiempo de ejecución: {end_time - start_time} segundos")

"""ejercicio 3"""

# import time
# start_time = time.time()

# import datetime

# fecha = datetime.datetime.now()

# print(f"Fecha y hora actual:" , fecha)

# end_time = time.time()

# print(f"Tiempo de ejecución: {end_time - start_time} segundos")

"""ejercicio 4"""

# import time
# start_time = time.time()

# import random

# while True:
#     numero_azar = random.randint(2, 10)
#     if numero_azar % 2 == 0: # verificar si numero es par
#         print(f"Número aleatorio par: {numero_azar}")
#         break

# end_time = time.time()

# print(f"Tiempo de ejecución: {end_time - start_time} segundos")

"""ejercicio 5"""

# import time
# start_time = time.time()

# import random

# def bola_magica():
#     opciones = [
#         "Es seguro que sí",
#         "Las chances son buenas",
#         "Puedes contar con ello",
#         "Pregúntame de nuevo más tarde",
#         "Concéntrate y pregunta de nuevo",
#         "No veo con claridad, intenta de nuevo",
#         "Mi respuesta es no",
#         "Mis fuentes me dicen que no"
#     ]
#     return random.choice(opciones)

# Pregunta = input("Preguntale algo a la bola magica: ")

# respuesta = bola_magica()

# print(f"La bola magica responde: {respuesta}")

# end_time = time.time()

# print(f"Tiempo de ejecución: {end_time - start_time} segundos")
