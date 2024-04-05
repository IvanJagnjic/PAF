import math as m
import matplotlib.pyplot as plt
#    r=self.v_x*(self.v_y+m.sqrt(self.v_y*self.v_y+2*g*self.y0))/g
class cestica:
    def __init__(self,brzina,kut,x0,y0,dt):
        self.brzina=brzina
        self.kut=kut
        self.x0=x0
        self.y0=y0
        self.v_x=m.cos(m.radians(self.kut))*self.brzina
        self.v_y=m.sin(m.radians(self.kut))*self.brzina
        self.dt=dt
    #pomak
    def move(self,dt):
        pomak_x=dt*self.v_x
        pomak_y=dt*self.v_y

        self.x0=pomak_x+self.x0
        self.y0=pomak_y+self.y0
        #print("Pomak je:",self.x0)
        #p1.poz()
        return[self.x0,self.y0]
    #pozicija
    def poz(self):
        print("X:", self.x0, "Y:", self.y0)
    #domet
    def range(self):
        g=-9.81
        dt=self.dt
        while self.y0>=0:
            [a,b]=self.move(dt)
            self.x0=a
            self.y0=b
            self.v_y=self.v_y+g*dt

        return(self.x0)

    def range_s_poz(self):
        x_lista=[]
        y_lista=[]
        g=-9.81
        dt=self.dt
        #Privremeno mijenjamo vrijednosti
        x=self.x0
        y=self.y0
        v_y=self.v_y
        v_x=self.v_x

        while self.y0>=0:
            self.v_y=self.v_y+g*dt
            [a,b]=self.move(dt)
            self.x0=a
            self.y0=b
            x_lista.append(a)
            y_lista.append(b)
        self.x0=x
        self.y0=y
        self.v_y=v_y
        self.v_x=v_x
        return [x_lista,y_lista]
    
    def plot_trajectory(self):
        x,y=self.range_s_poz()
        plt.plot(x, y)
        

    def reset(self):
        self.brzina=0
        self.kut=0
        self.x0=0
        self.y0=0
        self.v_x=0
        self.v_y=0
    
    def racun(self):
        v0=self.brzina
        rj=self.v_x*(self.v_y+m.sqrt(self.v_y*self.v_y+2*9.81*self.y0))/9.81
        return rj
    

        



