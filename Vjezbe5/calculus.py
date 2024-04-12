import numpy as np
import math as m
import matplotlib.pyplot as plt


def two_point(fja,x,e):
    dx=(fja(x+e)-fja(x))/e
    return dx

def three_point(fja,x, h):
    dx=(fja(x+h)-fja(x-h)) / (2 * h)
    return dx

def derivacija(fja,x,h,metoda=3,three_point=three_point,two_point=two_point):
    p=0
    if(metoda==3):
        p=three_point(fja,x,h)
    elif(metoda==2):
        p=two_point(fja,x,h)
    return p


def raspon(three_point,fja,a,b,e):
    n=m.floor(np.abs((a-b)/e))
    lista=np.linspace(a,b,n)
    lista_y=[]
    lista_ispis=[]
    for i in lista:
        y=fja(i)
        y_der=three_point(fja,i,e)
        lista_y.append(y_der)
        lista_ispis.append([[i,y],[y_der]])

    return lista_ispis
    #return [lista,lista_y]


#Funkicije integracije

def kvadratna_integracija(fja,a,b,n):

    lista_x=np.linspace(a,b,n)
    e=np.abs(float(a-b))/n
    Integral1=0
    Integral2=0
    for xi in lista_x:
        Integral1=fja(xi)*e+Integral1
        Integral2=fja(xi-e)*e+Integral2
    gornja=Integral1
    donja=Integral2
    return [Integral1,Integral2]

#def trapezna_integracija(fja,a,b,e):
    #n=m.floor(np.abs(a-b)/e)
    #lista_x=np.linspace(a,b,n)
    #Integral=0
    #for xi in lista_x:
        #Integral=((fja(xi)+fja(xi-e))/2)*e+Integral
    #return Integral

def trapezna_integracija2(fja,a,b,n):
    lista_x=np.linspace(a,b,n)
    e=np.abs(float(a-b))/n
    Integral=0
    for xi in lista_x:
        Integral=((fja(xi)+fja(xi-e))/2)*e+Integral
    return Integral
    













"""
print(two_point(funkcija,5,0.001))
print(derivacija(funkcija,5,0.001,2))
print(three_point(funkcija,5,0.001))
print(raspon(three_point,funkcija,1,5,0.5))
"""