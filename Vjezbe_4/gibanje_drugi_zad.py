import particle as par
import matplotlib.pyplot as plt
import numpy as np
import math as m

lista_vremena=np.linspace(0.01, 0.0001, num=1000)
lista_x=[]
for dt in lista_vremena:
    p1=par.cestica(10,60,0,0,dt)
    x=np.abs(p1.racun()-p1.range())
    lista_x.append(x)
plt.plot(lista_vremena,lista_x)
plt.show()