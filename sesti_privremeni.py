# Fel=-k*x
# Fg=-9.81
#x poc=0
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

    def move(self,dt):
        self.x0=self.x0+dt*self.brzina
        return x0

    def poz(self):
        print("X:", self.x0)

    def period_titranja_analiticki(self):
        period=0
        x_pocetna=self.x0
        while period==0 and self.x0!=x_pocetna:
            poz(Oscilator)
            Fel=-1*self.k*self.x0*np.sign()
            Fg=-1*self.m*9.81
