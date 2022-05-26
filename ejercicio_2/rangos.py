"""Ejercicio N°2
Programa que dado un rango de números enteros, obtiene la cantidad de números que contiene"""

print("-----------------------------------------")
print("---------- CANTIDAD DE NÚMEROS ----------")
print("-----------------------------------------")

# input 
print("Ingrese el primer número del rango:")
ni=int(input())
print(("Ingrese el último número del rango: "))
nf=int(input())

c=0
i=ni+1
# processing
if ni<nf:
    while i<nf:
        i=i+1
        c=c+1 
        print(ni+c)
else:
    print("ni debe ser menor que nf")

# output
print("La cantidad de números es: " +str(c))