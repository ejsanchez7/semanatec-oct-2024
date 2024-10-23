suma = 0
cantidad = 5
i = 0

while i < cantidad :
	num = float(input("Escribe un número: "))
	suma += num
	i += 1

print(f"El promedio es: {suma / cantidad}")
