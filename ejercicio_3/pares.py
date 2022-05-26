"""Ejercicio N°3
Programa que dado un rango de números enteros obtiene la cantidad de números pares que contiene."""

print("-----------------------------------------------")
print("---------- CANTIDAD DE NÚMEROS PARES ----------")
print("-----------------------------------------------")

# input 
a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))

# processing
if a<b:
    cant_num=0
    a=a+1
    while a<b:
        r=a%2
        if(r==0):
            cant_num=cant_num+1
        a=a+1
    print("La cantidad de números pares es: " +str(cant_num))

else:
    print("a debe ser menor que b")