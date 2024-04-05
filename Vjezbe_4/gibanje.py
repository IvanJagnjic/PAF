import particle as par
import matplotlib.pyplot as plt

#Definiramo cesticu (brzinu,kut,X0,Y0)
p1=par.cestica(20,45,0,10,0.00001)
print(p1.racun())
#Funkcija koja kreira graf trajektorija cestice, bez da mijenja poziciju cestice(vrijednost x0,y0 i brzinu)
p1.plot_trajectory()
plt.show()
#Pozicija prije pada
p1.poz()

#Funckija koja ispisuje domet
print("Domet je:",p1.range(),"m")
#Pozicija nakon pada
p1.poz()

#rijesi analiticki pa usporedi