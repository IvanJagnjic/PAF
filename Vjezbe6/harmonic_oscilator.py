# Fel=-k*x
# Fg=-9.81
#x poc=0

### Problem: za dt=0.001 program funkcionira, ali za manje nailazimo na probleme

import numpy as np
import math as m
import matplotlib.pyplot as plt
class Oscilator:
    def __init__(self,k,x0,brzina,dt,m):
        self.brzina=brzina
        self.x0=x0
        self.brzina=brzina
        self.k=k
        self.dt=dt
        self.m=m

    def move(self,dt):
        self.x0=self.x0+dt*self.brzina
        pass

    def poz(self):
        print("X:", self.x0)
        pass

    def period_titranja_analiticki(self):
        poc_brzina=self.brzina
        poc_x0=self.x0

        period=0
        x_pocetna=self.x0
        predznak_poc=np.sign(x_pocetna)
        predznak2=predznak_poc
        while (predznak_poc==predznak2):
            Fel=-1*self.k*self.x0
            a=Fel/self.m
            #print(a,self.brzina)
            self.move(self.dt)
            #print("Brzina 1:",self.brzina)
            self.brzina=self.brzina+a*self.dt
            #print("Brzina 2:",self.brzina)
            #period=period+self.dt
            #self.poz()
            predznak2=np.sign(self.x0)
        while (predznak_poc!=predznak2):
            Fel=-1*self.k*self.x0
            a=Fel/self.m
            #print(a,self.brzina)
            self.move(self.dt)
            #print("Brzina 1:",self.brzina)
            self.brzina=self.brzina+a*self.dt
            #print("Brzina 2:",self.brzina)
            period=period+self.dt
            #self.poz()
            predznak2=np.sign(self.x0)
        return period*2

    

    def graf(self):

            poc_brzina=self.brzina
            poc_x0=self.x0

            period=0
            x_pocetna=self.x0
            lista_x=[]
            lista_t=[]
            lista_a=[]
            lista_v=[]

            while period<10:
                Fel=-1*self.k*self.x0
                a=Fel/self.m
                self.move(self.dt)
                self.brzina=self.brzina+a*self.dt
                period=period+self.dt
                #self.poz()
                lista_x.append(self.x0)
                lista_t.append(period)
                lista_a.append(a)
                lista_v.append(self.brzina)
            self.brzina=poc_brzina
            self.x0=poc_x0
            self.x0=x_pocetna
            period=0
           
            return [lista_x,lista_v,lista_a,lista_t]
    
    def graf_po_dt(self,t1,t2,n):
        lista_t=np.linspace(t1,t2,n)
        lista_lista_x=[]
        lista_lista_t=[]
        for i in lista_t:
            self.dt=i
            [lista_x,b,c,lista_t]=self.graf()
            lista_lista_x.append(lista_x)
            lista_lista_t.append(lista_t)
        br=0
        for i in lista_lista_x:
            plt.plot(lista_lista_t[br],i)
            br=br+1

        
        plt.title("x/t graf u ovisnosti o koraku dt")
        plt.show()
        pass
            
    
    def period_titranja_numericki(self):
         return(2*m.pi*m.sqrt(float(self.m)/self.k))
    
    def prikazi_graf(self):
        [y1,y2,y3,x]=self.graf()

        plt.subplot(1, 3, 1)
        plt.plot(x,y1)
        plt.title("Ovisnost x o vremenu:")

        plt.subplot(1, 3, 2)
        plt.plot(x,y2)
        plt.title("Ovisnost v o vremenu:")
         
        plt.subplot(1, 3, 3)
        plt.plot(x,y3)
        plt.title("Ovisnost a o vremenu:")
        plt.show()
        





cestica=Oscilator(150,6,15,0.0002,15)

#print(cestica.period_titranja_analiticki())
#print(cestica.period_titranja_numericki())

