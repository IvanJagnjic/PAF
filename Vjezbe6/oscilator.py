import harmonic_oscilator as ho
import numpy as np
import math as m
import matplotlib.pyplot as plt

#crtanje x/t,a/t,v/t grafa
cestica=ho.Oscilator(150,6,15,0.0002,15)
cestica.prikazi_graf()

#usporedivanje grafa
cestica.graf_po_dt(0.01,0.001,10)


#uspoređivanje perioda
lista_perioda_analiticki=[]
lista_perioda_numericki=[]
lista_t=np.linspace(0.01,0.001,100)
for t in lista_t:
    cestica=ho.Oscilator(100,3,10,t,10)
    an=cestica.period_titranja_analiticki()
    nm=cestica.period_titranja_numericki()
    lista_perioda_analiticki.append(an)
    lista_perioda_numericki.append(nm)


plt.plot(lista_t,lista_perioda_numericki)
plt.plot(lista_t,lista_perioda_analiticki)
plt.title("Analiticki period/numericki period")
plt.show()
#Mozemo primjetiti da iako dva grafa na prvo oko ne izgledaju slicno, ako promotrimo koje su im vrijednosti pridodane primjetit ćemo da se razlikuju u zanemarivoj kolicini 
