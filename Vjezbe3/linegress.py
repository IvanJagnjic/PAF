import matplotlib.pyplot as plt
import arithm as ar
import math as m
import numpy as np
#lista_d= lista_a lista_x=lista_fi lista_y=lista_m
lista_m = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] 
lista_fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] 
lista_fi_kvadriran=[]
lista_m_kvadriran=[]
lista_d=[]
lista_xy=[]
for i in range(0,len(lista_m)):
    lista_d.append(lista_m[i]/lista_fi[i])
    
    lista_fi_kvadriran.append(lista_fi[i]*lista_fi[i])

    lista_m_kvadriran.append(lista_m[i]*lista_m[i])

    lista_xy.append(lista_m[i]*lista_fi[i])



srednji_x=ar.aritm(lista_fi)
srednji_y=ar.aritm(lista_m)
srednji_x_kvadrat=ar.aritm(lista_fi_kvadriran)
srednji_y_kvadrat=ar.aritm(lista_m_kvadriran)
srednji_xy=ar.aritm(lista_xy)
a=srednji_xy/srednji_x_kvadrat
print(a)

regresija=m.sqrt((srednji_y_kvadrat/srednji_x_kvadrat-a*a)/len(lista_m))
plt.scatter(lista_fi,lista_m)
fi = np.array(lista_fi)
plt.plot(lista_fi,a*fi)
plt.show()