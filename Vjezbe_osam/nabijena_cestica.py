import math as m
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

class nabijena_cestica:
    def __init__(self,dt,q,m,v_x,v_y,v_z,B,E_x,E_y,E_z,x=0,y=0,z=0):
        self.q=q
        self.m=m
        self.brzina=np.array((v_x,v_y,v_z))
        self.E=np.array((E_x,E_y,E_z))
        self.B=np.array((0,0,B))
        self.poz=np.array((x,y,z))
        self.dt=dt

    
    def pomak(self):
        self.poz=np.array((self.poz[0]+self.dt*self.brzina[0],self.poz[1]+self.dt*self.brzina[1],self.poz[2]+self.dt*self.brzina[2]))
        pass

    def trajektorij(self,ax):
        timer=0
        lista_x=[]
        lista_y=[]
        lista_z=[] 
        while timer<1000:
            timer=timer+self.dt
            #namistas kod
            a=(float(self.q)/self.m)*(self.E+np.cross(self.brzina,self.B))
            self.brzina=self.brzina+self.dt*(a)
            self.pomak()
            lista_x.append(self.poz[0])
            lista_y.append(self.poz[1])
            lista_z.append(self.poz[2])
        ax.plot3D(lista_x,lista_y,lista_z)
        pass

cestica1=nabijena_cestica(0.01,1,1,0.1,0.1,0.1,0.1,0,0,0,0,0,0)
cestica2=nabijena_cestica(0.01,-1,1,0.1,0.1,0.1,0.1,0,0,0,0,0,0)
fig = plt.figure()
ax = plt.axes(projection='3d')
cestica1.trajektorij(ax)
cestica2.trajektorij(ax)
plt.show()
        
        


        

