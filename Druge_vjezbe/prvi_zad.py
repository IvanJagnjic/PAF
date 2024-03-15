import numpy as np
 
import matplotlib.pyplot as plt
#unesite iznos
[F,m,x,y]=[10,100,1,1]
a=F/float(m)
#kolko koraka gledamo"
broj=200
#lista akceleracija po vremenu(acc je konst)
lista_a=[a]*broj
#vremenski interval od 10 sekundi
t=10
#definiramo liste vremena. x-pozicije i brzina ovisno o vremenu
vremena=np.linspace(0,t,num=broj)
dt=vremena[1]-vremena[0]
lista_x=[]
lista_v=[]
v=0
#Lista brzina
for i in vremena:
    v=a*dt+v
    x=dt*v+x
    lista_v.append(v)
    lista_x.append(x)

#print(vremena)
#print(lista_x)
#print(lista_v)
fig,(ax1,ax2,ax3) = plt.subplots(3)
ax1.plot(vremena,lista_x)
ax2.plot(vremena,lista_v)
ax3.plot(vremena,lista_a)
plt.show()