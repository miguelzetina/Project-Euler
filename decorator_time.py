from time import time  # importamos la función time para capturar tiempos


def decorator_time(funcion):

    def decorator(*args, **kwargs):
        tiempo_inicial = time()

        f = funcion(*args, **kwargs)

        tiempo_final = time()
        tiempo_de_ejecucion = tiempo_final - tiempo_inicial
        print("El programa ha tardado {:10f} segundos en ejecutarse.".format(tiempo_de_ejecucion))
        return f

    return decorator
