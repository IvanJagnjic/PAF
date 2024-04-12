import numpy as np
import math as m
import matplotlib.pyplot as plt
import calculus as cal

def kub(x):
    y=x*x*x-x+1
    #Der=3x2-1
    return y
def analiticki_kub(x):
    return (3*x*x-1)

#raspon pomaka e
[min,max]=[1,20]
lista_x=np.linspace(min,max,100)

lista_der_num=[]
lista_der_an= []
e=0.01
for x in lista_x:
    #mijenjanjem trece varijable biramo izmedu two point i three point metode
    lista_der_num.append(cal.derivacija(kub,x,e,2))
    lista_der_an.append(analiticki_kub(x))

print(lista_der_an)
print(lista_der_num)
plt.plot(lista_x,lista_der_num)
plt.plot(lista_x,lista_der_an)
plt.show()