
abrir_menu =  False
print("1.- Abrir menú.")
print("2.- Otra opción.")
print("3.- Salir.")

eleccion = int(input())

def menu(opcion_elegida):
    if opcion_elegida == 1:
        print("Abrió el menú.")
        global abrir_menu
        abrir_menu = True
    if opcion_elegida == 2:
        print("Abrió otra cosa.")
    if opcion_elegida == 3:
        print("Cerró el menú.")

menu(eleccion)


while abrir_menu:
    print("Menú extendido.")