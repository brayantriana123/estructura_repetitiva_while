"""Ejercicio N°6
Programa que lea un capital C, y que averigua e imprime en cuántos meses se duplica, a un interés compuesto del 5% mensual."""

print("----------------------")
print("------ CAPITAL -------")
print("----------------------")

# input
c=int(input("Ingrese su capital: "))

d=2*c
n=0

# processing
while c<d:
    c=c*0.05+c
    n=n+1
print("El capital se duplica en: " +str(n) +" meses.")