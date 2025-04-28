estdec = 0.15
clientefdec = 0.10

precio = float(input("Ingrese el precio del producto: "))

es_est = input("El cliente es estudiante? (s/n): ").lower() == 's' 
es_clientef = input("¿Es usted cliente frecuente? (s/n): ").lower() == 's' 

descuento = 0

if es_est:
    descuento = estdec
elif es_clientef:
    descuento = clientefdec

desct = precio * descuento
preciofinal = precio - desct

print(f"Precio normal del producto: ${precio}")

if descuento > 0: 
    print(f"Descuento aplicado: {descuento*100}% (${desct})") 
else:
    print("No se aplicaron descuentos") 
print(f"Precio final: ${preciofinal}")