#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula divisiones y encuentra el número mayor por medio de ciclos while.


#Función que calcula las divisiones por medio de un ciclo while.
def dividir(dividendo, divisor):
    cociente = 0
    dividendoInicial = dividendo

    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    residuo = dividendo

    print("%d / %d = %d, sobra %d" % (dividendoInicial, divisor, cociente, residuo))


#Función que encuentra el número mayor.
def encontrarMayor():
    numeroMayor = 0
    print("Teclea una serie de números para encontrar el mayor.")
    numero = int(input("Teclea un número [-1 para salir]: "))

    if numero == -1:
        print("No hay valor mayor")

    else:
        while numero != -1:
            if numero >= numeroMayor:
                numeroMayor = numero
            numero = int(input("Teclea un número [-1 para salir]: "))

        print("El mayor es: %d" % numeroMayor)


#Función principal. Lee e imprime datos
def main():
    print("""Misión 7. Ciclos while
Autor: Michelle Sánchez Guerrero
Matrícula: A01376622
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
    seleccion = int(input("Teclea tu opción: "))

    while seleccion != 3:

        if seleccion == 1:
            print()
            print("Calculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            if divisor == 0:
                print("Error")
                print()
            elif divisor < 0 or dividendo < 0:
                print("Por favor teclee números positivos")
                print()
            else:
                dividir(dividendo, divisor)
                print()

        elif seleccion == 2:
            print()
            encontrarMayor()
            print()

        else:
            print("ERROR, teclea 1, 2 o 3")
            print()

        print("""
Misión 7. Ciclos while
Autor: Michelle Sánchez Guerrero
Matrícula: A01376622
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        seleccion = int(input("Teclea tu opción: "))

    print()
    print("Gracias por usar este programa, regresa pronto.")


#Llamar a la función principal.
main()
