import InformacionDeLosSensores as isen
import BaseDeDatosProyecto as bdp
from time import sleep

while True:
  print(isen.obtenerDistancia())
  print("Flujo: %.2f L/min - Total: %.2f L" % (isen.flow_rate, isen.total_flow))
  bdp.GrabarFlujoYDistancia(isen.obtenerDistancia(), isen.flow_rate)
  sleep(1)