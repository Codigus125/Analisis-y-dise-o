#Hacer un programa que explique la permutación 
#y la comvianción con python en modo grafico
import random
import math
import tkinter
from tkinter import *

lista = [1,2,3,4]
lista1 = []
L = []
c = int
d = 5
e = 3

Pr = (math.factorial(d-1))/(math.factorial((d-1)-(e+1)))
#print(Pr)

def permu(d,e, lista, lista1):
    lista1.clear()
    lista = [1,2,3,4]
    while d != 1:
        c = random.randint(0, e)
        #print("c",c)
        v = lista.pop(c)
        #print("v",v)
        #print("lista",lista)
        lista1.append(v)
        e = e - 1
        d = d - 1
    #print("",lista1)
    lista = lista1
    return lista1
        
#def LPermu():
    n = 0
    v = -1
    temp = 0
    print("1",L)
    while n < Pr+1:
        if v == -1:
            f = permu(d, e, lista, lista1)
            L.append(f)
            v = v + 1
            n = n + 1
            print("2",L)
        else:
            while v < Pr+1:
                b = L[temp]
                f = permu(d, e, lista, lista1)
                if f == b:
                    v = v + 1
                    print("3",L)
                    f = permu(d, e, lista, lista1)
                else:
                    L.append(f)
                    n = n + 1
                    v = v + 1
                    print("4",L)
                    temp = temp + 1
                
    


#Fun = LPermu()
#print("6",Fun)

def Permutacion():
    texto = permu(d , e, lista, lista1)
    #print("1",texto)
    x.set(texto)


    
root = Tk()
root.geometry("400x200")

x = StringVar()


Label(root, text="Permutar: acción de ordenar TODOS los miembros de un conjunto").pack()
Label(root, text="en donde SI importa el orden").pack()
Entry(root, justify= "center" ,textvariable=x, state="disable").pack()
Button(root, text="Permutar", command=Permutacion).pack()

root.mainloop()
