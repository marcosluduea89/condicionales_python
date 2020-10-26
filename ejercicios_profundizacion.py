#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print("------------------------")
    print("-----Ejercicios N°1-----")
    print('Ejercicios de práctica con números\n')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_uno = int (input("Ingrese el primer numero: "))
    numero_dos = int (input("Ingrese el segundo numero: "))
    
    resta = numero_uno - numero_dos

    if resta == 0:
        print("El resultado es 0")
    elif resta > 0:
        print("El resultado es positivo")
    else:
        print("El resultado es negativo")



def ej2():
    print("------------------------")
    print("-----Ejercicios N°2-----")
    print('Ejercicios de práctica con números\n')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_uno = int (input("Ingrese el primer numero: "))
    numero_dos = int (input("Ingrese el segundo numero: "))
    numero_tres = int (input("Ingrese el tercer numero: "))

    if (numero_uno %2) == 1:
        print("{} Es Impar".format(numero_uno))
    else:
        print("{} Es par".format(numero_uno))
    if (numero_dos %2) == 1:
        print("{} Es Impar".format(numero_dos))
    else:
        print("{} Es par".format(numero_dos))
    if (numero_tres %2) == 1:
        print("{} Es Impar".format(numero_tres))
    else:
        print("{} Es par".format(numero_tres))
    

def ej3():
    print("------------------------")
    print("-----Ejercicios N°3-----")
    print('Ejercicios de práctica con números\n')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_uno = int (input("Ingrese el primer numero: "))
    numero_dos = int (input("Ingrese el segundo numero: "))
    print("---------------")
    print("Perfecto, a continuación ingrese la operacion deseada:")
    print("+")
    print("-")
    print("*")
    print("/")
    print("**")

    suma = numero_uno + numero_dos  
    resta = numero_uno - numero_dos
    multiplicacion = numero_uno * numero_dos
    division = numero_uno / numero_dos
    exponente = numero_uno ** numero_dos 

    opcion = str(input())

    if opcion == "+":
        print("El resultado de la suma entre {} y {} es : {} ".format(numero_uno,numero_dos,suma))
    elif opcion == "-":
        print("El resultado de la resta entre {} y {} es : {} ".format(numero_uno,numero_dos,resta)) 
    elif opcion == "*":
        print("El resultado de la multiplicacion entre {} y {} es : {} ".format(numero_uno,numero_dos,multiplicacion)) 
    elif opcion == "/":
        print("El resultado de la division es entre {} y {} : {} ".format(numero_uno,numero_dos,division))
    elif opcion == "**":
        print("El resultado del exponente entre {} y {} es : {} ".format(numero_uno,numero_dos,exponente))
    else:
        print("Esa operacion no esta habilitada, intente nuevamente.")    

def ej4():
    print("------------------------")
    print("-----Ejercicios N°4-----")
    print('Ejercicios de práctica con cadenas\n')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    
    palabra_uno = str (input("Ingrese la primera palabra:"))
    palabra_dos = str (input("Ingrese la segunda palabra:"))
    palabra_tres = str (input("Ingrese la tercer palabra:"))
    

    print("Perfecto, ¿como quiere ordenar las palabras?.\n")
    print("1 = Ordenar por orden alfabetico")
    print("2 = Ordenar por cantidad de letras")
    
    opcion = int (input("Ingrese la opcion deseada:"))

    #Opcion 1 = Guardamos las palabras en una variable "biblioteca" y usamos la funcion sorted
    biblioteca = [palabra_uno,palabra_dos,palabra_tres]
    orden_alfabetico = sorted(biblioteca)

    #Opcion 2 = Calculamos el tamaño de cada palabra y usamos la misma funcion sorted
    orden_len_1 = len (palabra_uno)
    orden_len_2 = len (palabra_dos)
    orden_len_3 = len (palabra_tres)
    numeros = [orden_len_1,orden_len_2,orden_len_3]
    orden_len= sorted(numeros)

    if opcion == 1:
        print (orden_alfabetico[0])
        print (orden_alfabetico[1])
        print (orden_alfabetico[2])
    elif opcion ==2:
        print (orden_len[0])
        print (orden_len[1])
        print (orden_len[2])
    else: 
        print("La opcion ingresada no es válida.")


def ej5():
    print("------------------------")
    print("-----Ejercicios N°5-----")
    print('Ejercicios de práctica con números \n')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    print("Ingrese tres valores de temperatura en °C")

    temperatura_uno = int (input("Ingrese el primer numero: "))
    temperatura_dos = int (input("Ingrese el segundo numero: "))
    temperatura_tres = int (input("Ingrese el tercer numero: "))

    temperaturas = [temperatura_uno,temperatura_dos,temperatura_tres]

    maxima = max(temperaturas)
    minima = min(temperaturas)
    promedio =(temperatura_uno + temperatura_dos + temperatura_tres)/3
    print("------------------------")
    print ("Resultados: ")

    print("La temperatura maxima es {}°C ".format(maxima))
    print("La temperatura minima es {}°C ".format(minima))
    print("El promedio de temperatura es {}°C".format(promedio))

    print("----Fin Programa-------")



if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
