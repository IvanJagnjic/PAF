import math as m
def aritm(lista_brojeva):
    suma=0
    for i in lista_brojeva:
        suma=suma+i
    sredina=suma/float(len(lista_brojeva))
    return sredina

def standardna_devijacija(lista_brojeva):
    suma=0
    arr=aritm(lista_brojeva)
    for i in lista_brojeva:
        suma=suma+(i-float(arr))*(i-float(arr))
    sredina=suma/(float(len(lista_brojeva))*(float(len(lista_brojeva)))-1)
    return m.sqrt(sredina)

lista=[1,2,3]
print(aritm([1,2,3,4,5,6,7,8,9,10]))
print(standardna_devijacija([20,40,44,55]))