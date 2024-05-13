import math as m
import matplotlib.pyplot as plt
import numpy as np

class planet():
    def __init__(self,d,M,v_x,v_y=0):
        self.M=M
        self.d=d
        self.v_x=v_x
        self.v_y=v_y
        self.poz=np.array((0,d))
        self.brzina=np.array((v_x,v_y))
        self.lista_x=[]
        self.lista_y=[]
        print(M,d,self.poz,self.brzina)


class svemir():
    def __init__(self,dt,t,lista_planeta=[]):
        self.dt=dt
        self.t=t
        self.G=6.67408*(10**(-11))
        self.lista_planeta=lista_planeta
    def add_planet(planet):
        lista_planeta.append(planet)
    #self.M1=planet1.M
    #self.M2=planet2.M
    #self.poz1=planet1.poz
    #self.brzina1=planet1.brzina
    #self.poz2=planet2.poz
    #self.brzina2=planet2.brzina
    

    def pomak(self,planet):
        planet.poz=np.array((planet.poz[0]+self.dt*planet.brzina[0],planet.poz[1]+self.dt*planet.brzina[1]))
        pass
    
    def trajektorij(self):
        timer=0
        #While petlje ubaci u ovu petlju da dobijes sve permutacije planeta i medudjelovanja njihovih sila, naravno izbris jedan od dijela koda za planet1 ili 2 
        #for i, planet1 in enumerate(lista_planeta[]):
            #for j,planet2 in enumerate(lista_planeta[]):
                #if i!=j:
        while timer<self.t:

            planet2=self.lista_planeta[1] 
            planet1=self.lista_planeta[0]


            timer=timer+self.dt
            r_12=planet2.poz-planet1.poz
            v_hat1 = r_12/np.linalg.norm(r_12)
            #pomak prvog planeta(bez M1 jer djelis i mnozis s M1)
            a1=v_hat1*((planet2.M*self.G)/(np.linalg.norm(r_12)*np.linalg.norm(r_12)))
            planet1.brzina=planet1.brzina+self.dt*a1
            self.pomak(planet1)

            
            
            r_21=planet1.poz-planet2.poz
            v_hat2= r_21/np.linalg.norm(r_21)
            #pomak drugog planeta(bez M2 jer dijelis i mnozis s M2)
            a2=v_hat2*((planet1.M*self.G)/(np.linalg.norm(r_12)*np.linalg.norm(r_12)))
            planet2.brzina=planet2.brzina+self.dt*a2
            self.pomak(planet2)


            planet1.lista_x.append(planet1.poz[0])
            planet2.lista_x.append(planet2.poz[0])

            planet1.lista_y.append(planet1.poz[1])
            planet2.lista_y.append(planet2.poz[1])
            
            self.lista_planeta[0]=planet1
            self.lista_planeta[1]=planet2


        plt.plot(planet1.lista_x,planet1.lista_y)
        plt.plot(planet2.lista_x,planet2.lista_y)

        pass
        


#def __init__(self,dt,t,d,M_p1,M_p2,v_x1,v_y1=0,v_x2=0,v_y2=0):

zemlja=planet(1.486*(10**11),5.9742*(10**24),29783)
sunce=planet(0,1.989*(10**30),0)
zemlja_sunce=svemir(100,5*31556926,[zemlja,sunce])
zemlja_sunce.trajektorij()
plt.show()