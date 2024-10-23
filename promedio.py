suma = 0
cantidad = 4

for i in range(cantidad):
	num = float(input("Escribe un número: "))
	suma += num

print(f"El promedio es: {suma / cantidad}")
