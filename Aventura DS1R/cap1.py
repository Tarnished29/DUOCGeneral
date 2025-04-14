print("De forma misteriosa despiertas en una celda desconocida, y tú sin saber cómo has acabado aquí.")
print("Una voz angelical y misteriosa retumba en tus oídos suavemente y te pregunta: ´Inexperimentado no muerto, cuál es tu nombre...? O más bien, tu apodo?´")

nombre = input ("Ingresa tu nombre:")

print(f"\nBienvenido, {nombre}. Tu viaje va a comenzar cuando tu voluntad propia lo decida asi...")

print("\n¿Qué deseas hacer?")
print("1. Explorar la celda")
print("2. Buscar posible ayuda")
print("3. Descansar...")

choice = input("Elige tu opción. 1, 2 o 3: ")

if choice == "1":
    print("Exploras la celda en la que te encuentras, y resulta ser una prisión de algún tipo, donde te encuentras bastantes seres sin conciencia...")
elif choice == "2":
    print("Buscas ayuda pero no hay ningún ser viviente y pensante que pueda darte alguna pista...Te quedas varado sin saber qué hacer.")
elif choice == "3":
    print("Decides no partir la exploración y te quedas quieto por ahí...Vaya explorador aventurero...")
else:
    print("Tu indecisión no te permite elegir una de las 3 dTecisiones que se te pasaron por la mente.")
    
print("\nMientras exploras, te encuentras con un robot oxidado. Su placa dice: ´Solo aquel que entienda los secretos del 1 y el 0 podrá avanzar.´")

respuesta = input("\n El robot pregunta: ¿Cuál es el resultado de 1 + 1 en binario? Tu respuesta es:")
if respuesta == "10":
    print("El robot hace un sonido y se aparta. Has aprendido algo sobre sistemas binarios!")
else:
    print("Nada...Nada ocurre. No has dado la respuesta correcta.")