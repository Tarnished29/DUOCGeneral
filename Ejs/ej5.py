libros = ["1984", "El túnel", "1Q84", "Fahrenheit 451", "Un mundo feliz"]

print("¿Qué quieres hacer respecto a los libros?")
print("1. Ver los libros.") 
print("2. Buscar libro.") 
print("3. Agregar libro (no existente en la lista actual).") 
print("4. Eliminar un libro existente.")

menu = int(input("Seleccione una opción: "))

if menu == 1:
       if len(libros) == 0:
              print("No hay libros disponibles actualmente.")
       else:
              print("Los libros que actualmente existen en la biblioteca son: ")
              print(libros[0])
              print(libros[1])
              print(libros[2])
              print(libros[3])
              print(libros[4])

elif menu == 2:
       blib = str(input("Indique el nombre del libro que desea buscar: "))
       enc = False

       for libro in libros: 
        if blib.lower() in libro.lower(): 
            print(f"Libro encontrado: {libro}") 
            enc = True
       
       if not enc:
             print("El libro no se ha encontrado en la biblioteca.")

elif menu == 3:
      nlib = str(input("Agregue el nombre del nuevo libro: "))



       