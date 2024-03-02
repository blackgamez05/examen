#Ejercicio para calcular las 4 operaciones basicas.
import os
os.system("cls || clear")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero."
def main():
    try:
        opcion = input("¿Qué operación deseas realizar? (sumar, restar, multiplicar, dividir): ")
        if opcion in ['sumar', 'restar', 'multiplicar', 'dividir']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if opcion == 'sumar':
                print("El resultado de la suma es:", sumar(num1, num2))
            elif opcion == 'restar':
                print("El resultado de la resta es:", restar(num1, num2))
            elif opcion == 'multiplicar':
                print("El resultado de la multiplicación es:", multiplicar(num1, num2))
            elif opcion == 'dividir':
                print("El resultado de la división es:", dividir(num1, num2))
        else:
            print("Opción inválida. Por favor, elige una operación válida.")
    except ValueError:
        print("Por favor, ingresa números válidos.")
