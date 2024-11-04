def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero."
    else:
        return a / b

def mostrar_menu():
    print("\nSelecciona una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numeros():
    while True:
        try:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            return numero1, numero2
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

def main():
    print("Calculadora sencilla")

    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        elif opcion in ['1', '2', '3', '4']:
            numero1, numero2 = obtener_numeros()

            if opcion == '1':
                resultado = sumar(numero1, numero2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == '2':
                resultado = restar(numero1, numero2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == '3':
                resultado = multiplicar(numero1, numero2)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == '4':
                resultado = dividir(numero1, numero2)
                print(f"Resultado de la división: {resultado}")
        else:
            print("Error: Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()
