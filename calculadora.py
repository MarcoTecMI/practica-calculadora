def main():
    n1 = float(input("Dame el primer número: "))
    n2 = float(input("Dame el segundo número: "))

    print(f"Suma: {n1 + n2}")
    print(f"Resta: {n1 - n2}")
    print(f"Multiplicación: {n1 * n2}")
    
    if n2 != 0:
        print(f"División: {n1 / n2}")
    else:
        print("División: Error, no se puede dividir entre 0")

if __name__ == "__main__":
    main()