import numpy as np
import matplotlib.pyplot as plt
import math
[v_pocetna,kut,x,y]=[200,30,0,0]
v_x=math.cos(math.radians(kut))*v_pocetna
v_y=math.sin(math.radians(kut))*v_pocetna
#vrijeme
t=10
#koliko koraka uzimamo
broj=200
#definiramo liste vremena. x-pozicije i brzina ovisno o vremenu
vremena=np.linspace(0,t,num=broj)
dt=vremena[1]-vremena[0]

lista_x=[]
lista_y=[]
for i in vremena:
    y=dt*v_y+y
    x=dt*v_x+x
    lista_x.append(x)
    lista_y.append(y)

fig,(ax1,ax2,ax3) = plt.subplots(3)
ax1.plot(lista_x,lista_y)
ax2.plot(vremena,lista_x)
ax3.plot(vremena,lista_y)
plt.show()