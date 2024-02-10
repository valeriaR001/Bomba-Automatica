import InformacionDeLosSensores
import BaseDeDatosProyecto
from time import sleep

while True:
    InformacionDeLosSensores.leerFlujoYDistancia()
    print(f"Flujo: {InformacionDeLosSensores.flujo}")
    print(f"Distancia: {InformacionDeLosSensores.distancia}")
    BaseDeDatosProyecto.GrabarFlujoYDistancia(InformacionDeLosSensores.flujo, InformacionDeLosSensores.distancia)
    sleep(5)