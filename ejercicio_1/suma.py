"""Ejercicio N°1
Programa que calcula la suma de los n primeros números naturales"""

print("-------------------------------")
print("--------- SUMA N NUMEROS ------")
print("-------------------------------")

suma=0
j=1

# input
print("Dame el valor de n:\n")
n=int(input())

# processing
while j<=n:
    suma=suma+j
    j=j+1

# output
print("La suma de los " +str(n) +" primeros números " +"= " +str(suma))