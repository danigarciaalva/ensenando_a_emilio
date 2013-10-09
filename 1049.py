import sys

for linea in sys.stdin:
	l = []
	l = linea.split(" ")
	if l[0] == '0\n' and len(l) == 1:
		break
	aux = []
	for i in l:
		aux.append(int(i))
	l = aux
	posicion = 0
	mayor = l[0]
	for i in range(0, len(l)):
		if l[i] > mayor:
			mayor = l[i]
			posicion = i
	del l[posicion]
	mayor = mayor**2
	suma = 0
	for i in l:
		suma += i**2
	if mayor == suma:
		print "right"
	else:
		print "wrong"
		
	

