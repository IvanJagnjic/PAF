import numpy as np
import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(v_pocetna,kut,m,F,t,preciznost,x=0,y=0):
    #akceleracija
    a=F/float(m)
    #rastavljamo na komponente
    v_x=math.cos(math.radians(kut))*v_pocetna
    v_y=math.sin(math.radians(kut))*v_pocetna
    #koliko koraka uzimamo
    broj=preciznost
    #definiramo liste vremena. x-pozicije i brzina ovisno o vremenu
    vremena=np.linspace(0,t,num=broj)
    dt=vremena[1]-vremena[0]

    lista_x=[]
    lista_y=[]
    for i in vremena:
        y=dt*v_y+y
        x=dt*v_x+x

        v_y=v_y+dt*a
        lista_x.append(x)
        lista_y.append(y)

    fig,(ax1,ax2,ax3) = plt.subplots(3)
    ax1.plot(lista_x,lista_y)
    ax2.plot(vremena,lista_x)
    ax3.plot(vremena,lista_y)
    plt.show()


def horizontalni_hitac(v_pocetna,kut,t,preciznost,x=0,y=0):
    #akceleracija
    a=-9.81
    #rastavljamo na komponente
    v_x=math.cos(math.radians(kut))*v_pocetna
    v_y=math.sin(math.radians(kut))*v_pocetna
    #koliko koraka uzimamo
    broj=preciznost
    #definiramo liste vremena. x-pozicije i brzina ovisno o vremenu
    vremena=np.linspace(0,t,num=broj)
    dt=vremena[1]-vremena[0]

    lista_x=[]
    lista_y=[]
    for i in vremena:
        y=dt*v_y+y
        x=dt*v_x+x

        v_y=v_y+dt*a
        print(v_y)
        lista_x.append(x)
        lista_y.append(y)

    fig,(ax1,ax2,ax3) = plt.subplots(3)
    ax1.plot(lista_x,lista_y)
    ax2.plot(vremena,lista_x)
    ax3.plot(vremena,lista_y)
    plt.show()

def horizontalni_hitac_bez_vremena(v_pocetna,kut,preciznost,x=0,y=0):
    #akceleracija
    a=-9.81
    #rastavljamo na komponente
    v_x=math.cos(math.radians(kut))*v_pocetna
    v_y=math.sin(math.radians(kut))*v_pocetna
    #koliko koraka uzimamo
    broj=preciznost
    #definiramo liste vremena. x-pozicije i brzina ovisno o vremenu
    dt=1/float(preciznost)
    vremena=[]
    t=0
    lista_x=[]
    lista_y=[]
    while y>0:
        t=t+dt
        y=dt*v_y+y
        x=dt*v_x+x

        v_y=v_y+dt*a
        print(y)
        vremena.append(t)
        lista_x.append(x)
        lista_y.append(y)

    fig,(ax1,ax2,ax3) = plt.subplots(3)
    ax1.plot(lista_x,lista_y)
    ax2.plot(vremena,lista_x)
    ax3.plot(vremena,lista_y)
    plt.show()









#jednoliko_gibanje(10,30,50,100,10,200,250,250)
#horizontalni_hitac(20,45,10,100)
#horizontalni_hitac_bez_vremena(20,45,100,0,200)