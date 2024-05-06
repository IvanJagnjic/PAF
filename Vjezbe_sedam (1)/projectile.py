import math as m
import matplotlib.pyplot as plt
import numpy as np
#    r=self.v_x*(self.v_y+m.sqrt(self.v_y*self.v_y+2*g*self.y0))/g
class cestica:
    def __init__(self,brzina,kut,x0,y0,dt,p,Cd,A,masa):

        self.brzina=brzina
        self.kut=kut
        self.x0=x0
        self.y0=y0
        self.v_x=m.cos(m.radians(self.kut))*self.brzina
        self.v_y=m.sin(m.radians(self.kut))*self.brzina
        self.dt=dt
        self.p=p
        self.Cd=Cd
        self.A=A
        self.masa=masa

    #pomak
    def otpor(self,v,p,Cd,A):
        otpor=-1*np.sign(v)*float(v)*v*p*Cd*A/2
        return otpor
    
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
        #racunamo silu otpora na x i y komponenti
        otpor_x=self.otpor(self.v_x,self.p,self.Cd,self.A)
        otpor_y=self.otpor(self.v_y,self.p,self.Cd,self.A)
        #racunamo utjecaj otpora zraka na akceleracije u x i y smjeru
        acc_otp_x=otpor_x/self.masa
        acc_otp_y=otpor_y/self.masa
        g=-9.81
        #finalne x,y akceleracije
        a_x=acc_otp_x
        a_y=acc_otp_y+g

        dt=self.dt
        while self.y0>=0:
            [a,b]=self.move(dt)
            self.x0=a
            self.y0=b
            self.v_y=self.v_y+a_x*dt
            self.v_x=self.v_x+a_y*dt

        return(self.x0)

    def range_s_poz(self):
        x_lista=[]
        y_lista=[]
        dt=self.dt
        #Privremeno mijenjamo vrijednosti
        x=self.x0
        y=self.y0
        v_y=self.v_y
        v_x=self.v_x
        while self.y0>=0:

            #racunamo silu otpora na x i y komponenti
            otpor_x=self.otpor(self.v_x,self.p,self.Cd,self.A)
            otpor_y=self.otpor(self.v_y,self.p,self.Cd,self.A)
            #racunamo utjecaj otpora zraka na akceleracije u x i y smjeru
            acc_otp_x=otpor_x/self.masa
            acc_otp_y=otpor_y/self.masa
            g=-9.81
            #finale x,y akceleracije
            a_y=acc_otp_y+g
            a_x=acc_otp_x

            #self.poz()
            self.v_y=self.v_y+a_y*dt
            self.v_x=self.v_x+a_x*dt
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
        plt.plot(x, y,color="blue")
        

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

    def runge_kuta(self,x,y,v_x,v_y,dt,p,Cd,A,m):
        #Provjeri ovu runge kutu da nisi nesto zamisa
        ############################################
        #runge kuta za x koordinatu/ovisnost x o t
        k1_vx=(-1*np.sign(v_x)*float(v_x)*v_x*p*Cd*A/2)/m*dt
        k1_x=v_x*dt

        k2_vx=-1*dt*np.sign(v_x+0.5*k1_vx)*float(v_x+k1_vx*0.5)*(v_x+k1_vx*0.5)*p*Cd*A/(2*m)
        k2_x=(v_x+0.5*k1_x)*dt

        k3_vx=-1*dt*np.sign(v_x+0.5*k2_vx)*float(v_x+k2_vx*0.5)*(v_x+k2_vx*0.5)*p*Cd*A/(2*m)
        k3_x=(v_x+0.5*k2_x)*dt

        k4_vx=-1*dt*np.sign(v_x+0.5*k3_vx)*float(v_x+k3_vx*0.5)*(v_x+k3_vx*0.5)*p*Cd*A/(2*m)
        k4_x=(v_x+0.5*k3_x)*dt

        x=x+(k1_x+k2_x+k3_x+k4_x)/6
        v_x=v_x+(k1_vx+k2_vx+k3_vx+k4_vx)/6

        #runge kuta za y koordinatu/ovisnost y o t
        k1_vy=-1*dt*np.sign(v_y)*float(v_y)*v_y*p*Cd*A/(2*m)-9.81*dt
        k1_y=v_y*dt

        k2_vy=-1*dt*np.sign(v_y+0.5*k1_vy)*float(v_y+k1_vy*0.5)*(v_y+k1_vy*0.5)*p*Cd*A/(2*m)*dt-9.81*dt
        k2_y=(v_y+0.5*k1_y)*dt

        k3_vy= - 1*dt*np.sign(v_y+0.5*k2_vy)*float(v_y+k2_vy*0.5)*(v_y+k2_vy*0.5)*p*Cd*A/(2*m)*dt-9.81*dt
        k3_y=(v_y+0.5*k2_x)*dt

        k4_vy=-1*dt*np.sign(v_y+k3_vy)*float(v_y+k3_vy)*(v_y+k3_vy)*p*Cd*A/(2*m)*dt-9.81*dt
        k4_y=(v_y + k3_y)*dt

        y=y+(k1_y+k2_y+k3_y+k4_y)/6
        v_y=v_y+(k1_vy+k2_vy+k3_vy+k4_vy)/6

        self.x0=x
        self.y0=y
        self.v_x=v_x
        self.v_y=v_y

        pass
    
    def graf_kuta(self):
        lista_x=[]
        lista_y=[]
        while self.y0>0:
            self.runge_kuta(self.x0,self.y0,self.v_x,self.v_y,self.dt,self.p,self.Cd,self.A,self.masa)
            print("X;",self.x0,"Y",self.y0)
            lista_x.append(self.x0)
            lista_y.append(self.y0)
        plt.plot(lista_x,lista_y)
        pass


        
