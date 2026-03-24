def division(a, b):
    if b == 0:
        print("Error: no se puede dividir entre 0")
        return None
    return a / b


def main():
    print("Función de división")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = division(num1, num2)

    if resultado != None:
        print("Resultado:", resultado)


if __name__ == "__main__":
    main()