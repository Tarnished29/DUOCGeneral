usuario = ""
contraseña = ""
realus = "Ashen" #Usuario real
realcont = "theashen" #Contraseña real
print("Ingrese el usuario: ")
usuario = input()
print("Ahora ingrese la contraseña: ")
contraseña = input()

primeraletra = "theashen"[0]

if usuario == realus and contraseña == realcont:
    print(f"Bienvenido, {realus}.")
elif usuario != realus and contraseña != realcont:
    print("Credenciales incorrectas. Se bloqueará el equipo por 5 minutos. Inténtelo de nuevo más tarde.")
elif usuario == realus and contraseña != realcont:
    print(f"La primera letra de la contraseña es \"{primeraletra}\".")
else:
    print("Ingrese los datos de nuevo pero correctamente.")