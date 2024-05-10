import math as m
import matplotlib.pyplot as plt
import numpy as np


class planeti():
    def __init__(self,dt,t,d,M_p1,M_p2,v_x1,v_y1=0,v_x2=0,v_y2=0):
        self.dt=dt
        self.t=t

        self.M1=M_p1
        self.M2=M_p2

        self.poz1=np.array((0,0))
        self.brzina1=np.array((v_x1,v_y1))

        self.poz2=np.array((0,d))
        self.brzina2=np.array((v_x2,v_y2))

        self.G=6.67408*(10**(-11))

    def pomak1(self):
        self.poz1=np.array((self.poz1[0]+self.dt*self.brzina1[0],self.poz1[1]+self.dt*self.brzina1[1]))
        pass
    
    def pomak2(self):
        self.poz2=np.array((self.poz2[0]+self.dt*self.brzina2[0],self.poz2[1]+self.dt*self.brzina2[1]))
        pass
    def trajektorij(self):
        timer=0
        lista_x1=[]
        lista_y1=[]

        lista_x2=[]
        lista_y2=[]
        while timer<self.t:
            timer=timer+self.dt
            r_12=self.poz2-self.poz1
            r_21=-1*r_12

            v_hat1 = r_12/np.linalg.norm(r_12)
            v_hat2= r_21/np.linalg.norm(r_21)

            #pomak prvog planeta(bez M1 jer djelis i mnozis s M1)
            a1=v_hat1*((self.M2*self.G)/(np.linalg.norm(r_12)*np.linalg.norm(r_12)))

            self.brzina1=self.brzina1+self.dt*a1
            self.pomak1()

            #pomak drugog planeta(bez M2 jer dijelis i mnozis s M2)
            a2=v_hat2*((self.M1*self.G)/(np.linalg.norm(r_12)*np.linalg.norm(r_12)))

            self.brzina2=self.brzina2+self.dt*a2
            self.pomak2()


            lista_x1.append(self.poz1[0])
            lista_y1.append(self.poz1[1])

            lista_x2.append(self.poz2[0])
            lista_y2.append(self.poz2[1])
            


        plt.plot(lista_x1,lista_y1)
        plt.plot(lista_x2,lista_y2)

        pass
        





zemlja_sunce=planeti(100,31556926,1.486*(10**11),5.9742*(10**24),1.989*(10**30),29783)
zemlja_sunce.trajektorij()
plt.show()