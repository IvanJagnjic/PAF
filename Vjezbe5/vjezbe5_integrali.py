import numpy as np
import math as m
import matplotlib.pyplot as plt
import calculus as cal

def funkcija1(x):
    #Integral=x*x*x/3
    return x*x

#[gornji,donji]=cal.kvadratna_integracija(funkcija1,1,5,4000)
#print("Gornji:",gornji,"Donji:",donji)
#print(cal.trapezna_integracija2(funkcija1,1,5,4000))

[n_max,n_min]=[1000,1]
(a,b)=(1,5)

lista_n=np.linspace(n_min,n_max,n_max-n_min+1)
lista_gornja=[]
lista_donja=[]
lista_trapezna=[]
for n in lista_n:
    print(n)
    [gornji,donji]=cal.kvadratna_integracija(funkcija1,a,b,n)
    trapezni=cal.trapezna_integracija2(funkcija1,a,b,n)
    lista_gornja.append(gornji)
    lista_donja.append(donji)
    lista_trapezna.append(trapezni)
print(lista_gornja)
plt.plot(lista_n,lista_gornja)
plt.plot(lista_n,lista_donja)
plt.plot(lista_n,lista_trapezna)
plt.show()











#print(cal.trapezna_integracija(funkcija1,1,5,0.0001))