import numpy as np
import statistics as stat
import random
import matplotlib.pyplot as plt

d = 0
e = 1
lista = []
grafico = []
c = int
while d < 1000000:
    c = random.randint(1,100)
    lista.append(c)
    d = d + 1
p25 = np.percentile(lista, 25)
p50 = np.percentile(lista, 50)
p75 = np.percentile(lista, 75)
p100 = np.percentile(lista, 100)
promedio = np.mean(lista)
moda = stat.mode(lista)
mediana = np.median(lista)
#print("Lista: ",lista)
lista.sort()
#print("Lista ordenada: ", lista)
rango25 = 0
rango50 = 0
rango75 = 0
rango100 = 0

while e < 26:
    y = lista.count(e)
    rango25 = rango25 + y
    e = e + 1
while e < 51:
    y = lista.count(e)
    rango50 = rango50 + y
    e = e + 1
while e < 76:
    y = lista.count(e)
    rango75 = rango75 + y
    e = e + 1
while e < 101:
    y = lista.count(e)
    rango100 = rango100 + y
    e = e + 1
  
grafico.append(rango25)
grafico.append(rango50)
grafico.append(rango75)
grafico.append(rango100)

print("rango25:" ,rango25)
print("rango50:" ,rango50)
print("rango75:" ,rango75)
print("rango100:" ,rango100)
#print("total", total)
print("promedio: ",promedio)
print("mediana: ",mediana)
print("moda: ",moda)

nombres = ['1-25', '26-50' , '51-75' ,'76-100']

plt.plot(nombres, grafico, marker = "o")
plt.show()


