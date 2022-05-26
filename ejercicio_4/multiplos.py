"""Ejercicio N°4
Programa que obtiene la cantidad de los primeros N números múltiplos de 5."""

print("------------------------------------------------")
print("---------- CANTIDAD DE MÚLTIPLOS DE 5 ----------")
print("------------------------------------------------")

# input 
a=int(1)
n=int(input("Digite el valor de n: "))

# processing
if a<n:
    cant_num=0
    a=a+1
    while a<=n:
        r=a%5
        if(r==0):
            cant_num=cant_num+1
        a=a+1
    print("La cantidad de los múltiplos de 5 es: " +str(cant_num))

else:
    print("a debe ser menor que b")