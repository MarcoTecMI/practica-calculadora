def multiplicacion(a, b):
    return a * b

def main():
    print("Función de multiplicación")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = multiplicacion(num1, num2)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()