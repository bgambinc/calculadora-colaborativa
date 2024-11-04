def umar(a, b):
    return 

def restar(a, b):
    return a - b

def multiplicar(a, b):
    
    return  

def dividir(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    return 



    
# Bloque principal
if __name__ == "__main__":

    while True:
        print("\n--- Calculadora Básica ---")
        print("Selecciona una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        try:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))

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
                if resultado is not None:
                    print(f"Resultado de la división: {resultado}")

        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

