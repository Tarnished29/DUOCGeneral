print("Nivel facil")
print("\n")
print("1.-")
nombre = "Martín"
edad = 18
estatura = 1.74
print("Datos:")
print(nombre)
print(edad)
print(estatura)
print("\n")
print("2.-")
nacim = 2006
print("Año de nacimiento:", nacim)
nacact = 2025
print("Año actual:", nacact)
edadact = nacact - nacim
print("Mi edad es:", edadact - 1)
print("Nivel medio")
print("\n")
print("3.-")
precio = 15000
preciodec = float(precio * 0.15)
preciof = precio - preciodec
print("El precio con descuento es:", preciof)
print("\n")
print("4.-")
edadmeses = (edad * 12)
print("Mi edad en meses es:", edadmeses, "horas.")
edadsemanas = (edad * 52)
print("Mi edad en semanas es:", edadsemanas, "semanas.")
edaddias = (edad * 365)
print("Mi edad en días es:", edaddias, "días.")
edadhoras = (edad * 365 * 24)
print("Mi edad en horas es:", edadhoras, "horas.")
print("\n")
print("Nivel dificil")
print("5.-")
exa1 = 6.5
exa2 = 2.4
exa3 = 3.0
promedio = float(exa1 + exa2 + exa3) // 3
if promedio >= 4.0:
    print("Aprobaste! Tu nota finalmente fue", promedio)
elif promedio <= 4.0:
    print("Reprobaste...Tu nota fue", promedio)