#Ejemplo1
a = 5
while(a > 0):
	print(f"el valor de a es :{a}")
	a = int(input("Ingrese un valor: "))
	
#Ejemplo2   
x = 5
while x > 0:
    x -=1
    print(x, end=" ")

# Salida: 4,3,2,1,0
    
#Ejemplo3 - Evitar esto !!
while True:
    print("Loop Infinito")