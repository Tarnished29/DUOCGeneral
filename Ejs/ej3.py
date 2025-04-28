duracion = float(input("Ingrese la duración de la canción en minutos: "))
genero = str(input("Ingrese el género músical: "))
año = int(input("Por último, el año de lanzamiento: "))

duracionR = 2.5 <= duracion <= 4.5
generoR = genero in ["rock", "pop", "indie"] 
añoL = año >= 2010

if duracionR and generoR and añoL:
    print(f"La canción si entra en la playlist por tener la duración requerida \"({duracion} minutos)\", pertenecer al género \"({genero} es el género)\" y año \"(la canción es del año {año})\".")
else:
    print(f"La canción no cumple con las condiciones para ser parte de la playlist: ")
print("\n")
if not duracionR: 
        print(f"La canción elegida tiene una duración de {duracion} minutos, lo cual está fuera de lo solicitado (2.5-4.5 min).") 

if not generoR:
     print(f"La canción no pertenece a los géneros seleccionados por defecto, los cuales son \"pop\", \"indie\" y \"rock\".")

if not añoL:
     print(f"La canción es anterior al año 2010, específicamente se lanzó el año {año}.")