""" 1) """


from math import fmod


def imprimir_numeros():
    for x in range(1, 11, 1):
        print(x)


""" 2) """


def imprimir_numeros_pares():
    for x in range(1, 11, 1):
        if fmod(x, 2) == 0:
            print(x)


""" 3) """


def imprimir_eco():
    for x in range(1, 11, 1):
        print("eco")


""" 4) """


def cuenta_regresiva(numero: int):
    for x in range(numero, 0, -1):
        print(x)
    print("Despegue")


""" 5) """


def monitoreo_viaje_tiempo(año_partida: int, año_llegada: int):
    while año_partida > año_llegada:
        año_partida = año_partida - 1
        print("Viajó un año al pasado, estamos en el año: " + str(año_partida))


""" 6) """


def mas_cercano_aristoteles(año_partida: int):
    while año_partida > -384:
        año_partida = año_partida - 20
        print("Viajó veinte años al pasado, estamos en el año: " + str(año_partida))
