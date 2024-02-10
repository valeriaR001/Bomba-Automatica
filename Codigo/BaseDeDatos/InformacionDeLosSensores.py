flujo = 0
distancia = 0

def leerFlujoYDistancia():
    global flujo, distancia
    import random
    flujo = random.uniform(0.0, 30.0)
    distancia = int(random.randrange(0,100, 1))