import numpy as np 
import matplotlib.pyplot as plt

x = np.array([ 1,   2,   3,   4,   5,   6,   7,   8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20,   21,   22]) 
y = np.array([1.04, 1.0, 1.13, 2.84, 2.68, 3.76, 4.7, 4.17, 5.19, 6.48, 3.49, 3.85, 2.21, 2.29, 4.43, 4.24, 3.78, 8.38, 10.31, 12.21, 12.9, 16.66])
numvalores = len(x)


#PROMEDIOS DE X
sumax = 0
for valor in x:
    sumax = sumax + valor

promediox = sumax / len(x)
#print(f"La suma de x es: {sumax}")
print(f"x: {promediox}")


#PROMEDIOS DE Y
sumay = 0
for valor in y:
    sumay = sumay + valor
    
promedioy = sumay / len(y)
#print(f"La suma de y es: {sumay}")
print(f"y: {promedioy}")

multiplicacion = 0
suma = 0
sumatotal = 0

#suma de la multiplicacion de xy
aux=0
for valor in y:
    aux = aux + 1
    aux1 = valor
    #print("(",aux1,")", "(",aux,")")
    multiplicacion = aux1 * aux
    suma = suma + multiplicacion
print(f"xy: {suma}")

#suma de valores x^2
auxiliar = 0
sumas = 0
potencia = 0
for valores in y:
    auxiliar = auxiliar + 1
    #print("(",auxiliar,")")
    potencia = auxiliar * auxiliar
    sumas = sumas + potencia
print(f"x^2: {sumas}")

print(f"Cantidad de datos: {numvalores}")

mediadex = promediox * promediox
print(f"Media de x^2: {mediadex}")


b= (suma-numvalores*promediox*promedioy)/(sumas-numvalores*mediadex)
print(f"El valor de b es: {b}")

a = promedioy-b*promediox
print(f"El valor de a es: {a}")

valorprediccion = 0
valorprediccion = input("¿Qué valor desea predecir? ")

ypred = a + b * int(valorprediccion)

print(f"El valor de prediccion es: {ypred}")

x = np.append(x, valorprediccion)
y = np.append(y, ypred)



#volver valores a ndarray volviendo objetos heterogeneos y mas faciles de desempaquetar
x_valores = np.array(x)
y_valores = np.array(y)



#GRAFICA
plt.scatter(x, y, color = "r",marker = "o", s = 60) 

#mostrar la probabilidad
plt.plot(valorprediccion,ypred,marker ="o")

#mostrar pendiente
plt.plot([int(valorprediccion), int(y[0])], [int(ypred), int(x[0])], color="g")

plt.xlabel('Popularidad') 
plt.ylabel('Tiempo') 

plt.show()

