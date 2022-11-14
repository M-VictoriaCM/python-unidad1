##1. Escribe un programa muestre por pantalla “Hello World”.##
def saludo():
    print("Hola mundo")


# saludo()

# 2. Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5
def sumar(a, b):
    resultado = a + b
    print("El resultado es", resultado)


# sumar(3, 5)


# 3. Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
def saludo_a(saludo, nombre):
    print(saludo, nombre)


# msj= "Ingrese su nombre"
# saludo ="hola"
# saludo_a(saludo, input(msj))


# 4. Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
def sumar_dos_valores(nro1, nro2):
    resultado = nro1 + nro2
    print("La suma es: ", resultado)


# msj = "Ingrese un numero: "
# nro1= int(input(msj))
# nro2= int(input(msj))
# sumar_dos_valores(nro1, nro2)


# 5. Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
def es_mayor(nro1, nro2):
    if nro1 > nro2:
        print("El mayor es: ", nro1)
    else:
        print("El mayor es: ", nro2)


# msj = "Ingrese un numero: "
# nro1= int(input(msj))
# nro2= int(input(msj))
# es_mayor(nro1, nro2)


# 6. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
def es_mayor_tres(nro1, nro2, nro3):
    if (nro1 > nro2) and (nro1 > nro3):
        print("El mayor es: ", nro1)
    elif (nro1 < nro2) and (nro2 > nro3):
        print("El mayor es: ", nro2)
    else:
        print("El mayor es: ", nro3)


# msj = "Ingrese un numero: "
# nro1 = int(input(msj))
# nro2 = int(input(msj))
# nro3 = int(input(msj))

# es_mayor_tres(nro1, nro2, nro3)

# 7.Escribe un programa que pida un número y diga si es divisible por 2
def divisible_dos(nro):
    if nro % 2 == 0:
        print(nro, "es divisble por 2")
    else:
        print("no es divisible")


# msj = "Ingrese un numero: "
# nro = int(input(msj))
# divisible_dos(nro)


# 8. Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
def buscar_divisores(divisor1, divisor2, divisor3, divisor4, nro):
    if nro % divisor1 == 0:
        print(nro, "es divisble por", divisor1)
    elif nro % divisor2 == 0:
        print(nro, "es divisble por", divisor2)
    elif nro % divisor3 == 0:
        print(nro, "es divisble por", divisor3)
    elif nro % divisor4 == 0:
        print(nro, "es divisble por", divisor4)
    else:
        print(nro, "no es divisible por ningun numero")


# msj = "Ingrese un numero: "
# nro = int(input(msj))
#  buscar_divisores(2, 3, 5, 7, nro)

# 9. Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
def todos_divisibles(divisor1, divisor2, divisor3, divisor4, nro):
    if (
        (nro % divisor1 == 0)
        or (nro % divisor2 == 0)
        or (nro % divisor3 == 0)
        or (nro % divisor4 == 0)
    ):
        if nro % divisor1 == 0:
            print(nro, "es divisble por", divisor1)
        if nro % divisor2 == 0:
            print(nro, "es divisble por", divisor2)
            if nro % divisor3 == 0:
                print(nro, "es divisble por", divisor3)
                if nro % divisor4 == 0:
                    print(nro, "es divisble por", divisor4)
    else:
        print(nro, "no es divisible por ningun numero")


# msj = "Ingrese un numero: "
# nro = int(input(msj))
# todos_divisibles(2, 3, 5, 7, nro)

# Escribir un programa que escriba en pantalla los divisores de un número dado
def es_divisor(nro):
    print("Los divisores de ", nro, "son:")
    for i in range(99, 0, -1):
        if nro % i == 0:
            print(i)


# nro= msj="Ingrese un numero: "
# es_divisor(nro)


# 11. Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)


def es_primo(nro):
    for n in range(2, nro):
        if nro % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True


# msj="Ingrese un numero: "
# es_primo(int(input(msj)))

"""12. Pide una nota (número). Muestra la calificación según la nota:
    - 0-3: Muy deficiente
    - 3-5: Insuficiente
    - 5-6: Suficiente
    - 6-7: Bien
    - 7-9: Notable
    - 9-10: Sobresaliente
"""


def calificacion(nota):
    if (nota >= 0) and (nota <= 3):
        print("muy deficiente")
    elif (nota >= 3) and (nota <= 5):
        print("Insuficiente")
    elif (nota >= 5) and (nota <= 6):
        print("Suficiente")
    elif (nota >= 6) and (nota <= 7):
        print("Bien")
    elif (nota >= 7) and (nota <= 9):
        print("Notable")
    elif (nota >= 9) and (nota <= 10):
        print("Sobresaliente")
    else:
        print("La nota es incorrecta")


# msj = "Ingrese una nota: "
# nota = float(input(msj))
# calificacion(nota)

"""
13. Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
    1
    22
    333
    4444
    55555
    666666
    ……….
"""


def piramide():
    for i in range(1, 30):
        print(str(i) * i)


# piramide()

"""14. Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555 
"""

def piramide(nro):
    for i in range(nro, -1, -1):
        print(str(i) * i)


# msj = "Ingrese un numero: "
# nro = int(input(msj))
# piramide(nro)
