print("-Conversor-")
print("\n")
print("1. Kilómetros a millas") 
print("2. Millas a kilómetros") 
print("3. Celsius a Fahrenheit") 
print("4. Fahrenheit a Celsius")

menu = int(input("\nSeleccione una opción (1-4): ")) 

if menu == 1:
    valork = float(input("Seleccione la cantidad de kilómetros a convertir: "))
    if valork < 0: 
        print("La distancia no puede ser negativa.") 
    else: 
        resultadomi = valork * 0.621371 #Equivalencia de x cantidad de km traducido en millas
        print(f"{valork} kilómetros equivalen a {resultadomi} millas.")

elif menu == 2:
    valormi = float(input("Seleccione la cantidad de millas a convertir: "))
    if valormi < 0: 
        print("La distancia no puede ser negativa.") 
    else: 
        resultadokm = valormi * 1.60934 # x cantidad de millas traducido a km
        print(f"{valormi} millas equivalen a {resultadokm:.4f} kilómetros.")

elif menu == 3:
    valorcel = float(input("Seleccione la cantidad de grados C°: "))
    resultadofa = (valorcel * (9 / 5)) + 32
    print(f"La temperatura en Fahrenheit es de {resultadofa:.0f}°F")

elif menu == 4:
    valorfa = float(input("Seleccione la cantidad de grados F°: "))
    resultadoce = (valorfa - 32) * (5/9)
    print(f"La temperatura en Celsius es de {resultadoce:.0f}°C")
else:
    print("Ingrese una opción correcta de menú.")


