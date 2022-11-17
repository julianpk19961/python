# 3.6 Librerías de fecha y datetime para horas
# requieren ser importadas de la librería date o datetime.

# Si se necesita usar fechas en un programa, es necesario importar las librerías Python: datetime y date

from datetime import date
from datetime import datetime
import random


today = date.today()
# print('date.today() = ', today)

nowIs = datetime.now()
# print('datetime.now() = ',nowIs)

