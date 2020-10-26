#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Marcos Ludueña"
__email__ = "marcosluduea89@gmail.com"
__version__ = "1.0"


def ej1():
    print("------------------------")
    print("-----Ejercicios N°1-----")
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    print("------------------------")

    print("¿Cual es el mayor de los numeros? \n ")
   
    if numero_1 == numero_2:
        print ("Son iguales los numeros, ingrese valores diferentes.")
        
    elif numero_1 > numero_2:
        print ("El Numero {} es mayor que el numero {} ".format(numero_1,
                                                                numero_2))
    else: print("El Numero {} es mayor que el numero {} ".format(numero_2,
                                                                numero_1))
    print("------------------------")
    print("Verificación de Positivo , negativo o cero del primer numero ingresado ")
    
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print("El numero {} es Positivo. ".format(numero_1))
    elif numero_1 < 0:
        print("El numero {} es Negativo. ".format(numero_1))
    else:
        print("El numero es igual a cero. ")

    print("------------------------")
    # Verifique si el numero_1 es mayor a 0 y menor a 100

    print("¿El numero {} es mayor a 0 y menor a 100?".format(numero_1))
    
    if numero_1 > 0 and (numero_1 < 100) :
        print("El numero {} cumple la condición. ".format(numero_1))
    else: 
        print("El numero {} no cumple la condición. ".format(numero_1))

    print("------------------------")

    # Imprima en pantalla si se cumple o no la condición
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    print("¿El numero {} es menor a diez o el numero {} menor a -2?".format(numero_1,numero_2))
    
    if (numero_1 < 10) or (numero_2 < -2):
        print("La condición se cumple.")
    else:
        print("La condicion no se cumple.")
    
    # Imprima en pantalla si se cumple o no la condición


def ej2():
    print("------------------------")
    print("-----Ejercicios N°2-----")
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas

    texto_1 = str(input("Ingrese la primera palabra:"))

    texto_2 = str(input("Ingrese la segunda palabra:"))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    print("------------------------")
    
    
    if texto_1 > texto_2:
        print("El texto {} es el mayor alfabeticamente".format(texto_1))
    else:
        print("El texto {} es el mayor alfabeticamente".format(texto_2))

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    leng_texto_1 = len (texto_1) 
    leng_texto_2 = len (texto_2)

    if leng_texto_1 > leng_texto_2:
        print("La palabra {} tiene la mayor cantidad de palabras ".format(texto_1))
    else:
        print("La palabra {} tiene la mayor cantidad de palabras ".format(texto_2))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    if texto_1[0] > texto_2 [0]:
        print("La palabra {} contine la primer letra mayor a la segunda".format(texto_1))
    else:
        print("La palabra {} contine la primer letra mayor a la segunda".format(texto_1))
    print("------------------------")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    if texto_1 == copia_texto_1:
        print("Son iguales")
    else:
        print("No son iguales")

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_1:
        print("Son distintos")
    else:
        print("Son iguales")
    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda


def ej3():
    # Ejercicios de práctica numérica
    print("------------------------")
    print("-----Ejercicios N°3-----")
    print( "Condicionales anidados" ) 
    numero_1 = 7
    numero_2 = -2

    if numero_1 > 5: 
        if numero_2 > 0:
            print ("Resp=1")
        else:
            print ("Resp=2")
    else : 
        if numero_2 > 5:
            print ("Resp=3")
        else:
            print ("Resp=4")
        
    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    print("------------------------")
    print("Verificar la calificación de un estudiante \n")
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = int(input("Ingrese el puntaje:"))

    if puntaje >=90:
        print("A")
    elif puntaje >=80:
        print("B")
    elif puntaje >= 70:
        print("C")
    elif puntaje >= 60:
        print("D")
    elif puntaje < 60:
        print("F")

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados
def ej4():
    # Ejemplos variables de texto
    print("------------------------")
    print("-----Ejercicios N°4-----")
    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("La variable {} es mayor que {} ".format(texto_1,texto_2))
    else:
        print("La variable {} es mayor que {} ".format(texto_2,texto_1))
    
    num_texto_1 = int(texto_1)
    num_texto_2 = int(texto_2)

    if num_texto_1 > num_texto_2:
        print("El numero {} es mayor que {}".format(num_texto_1,num_texto_2))
    else:
        print("El numero {} es mayor que {}".format(num_texto_2,num_texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    
    

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)



if __name__ == '__main__':
    print ("Bienvenidos a otra clase de Inove con Python  ")
    ej1()
    ej2()
    ej3()
    ej4()
    
