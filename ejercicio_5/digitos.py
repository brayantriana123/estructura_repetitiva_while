"""Ejercicio N°5
Programa que dado un número determina cuántos dígitos tiene."""



print("-----------------------------------------")
print("---------- CANTIDAD DE DÍGITOS ----------")
print("-----------------------------------------")

# input 
n=int(input("Digite el valor de n: "))

conta=0
#processing
while n>0:
    n=n//10
    conta=conta+1
    
print("La cantidad de dígitos es:",conta)