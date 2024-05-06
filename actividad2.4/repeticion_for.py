#El ciclo FOR permite ejecutar una tarea, un determinado número de veces (finito por lo general).
#for elemento in secuencia:
    # Código a ejecutar en cada iteración

#Function RANGE
    #start	Optional. An integer number specifying at which position to start. Default is 0
    #stop	Required. An integer number specifying at which position to stop (not included).
    #step	Optional. An integer number specifying the incrementation. Default is 1


#Ejemplo 1
#for i in range(9):
    #print(f"No debo botar la basura parte: {i}")

#Ejemplo 2
print("Resultado Ejemplo 2:")
for i in range(0,9,3):
    i =  i + 1
    print(f"No debo botar la basura parte: {i}", end="")

#Ejemplo 3
print("\n\nResultado Ejemplo 3:")
x = range(0,9,3)
for i in x:
    i =  i + 1
    print(f"No debo botar la basura parte: {i}", end="")

#Ejemplo 4
print("\n\nResultado Ejemplo 4:")
for i in range(-1,9,2):
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1, 

#Ejemplo 5
print("\n\nResultado Ejemplo 5:")
for i in range(-1,9,2):
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1, 

#Ejemplo 6
print("\n\nResultado Ejemplo 6:")
for i in "Hola":
    print(f"Letra: {i}")

#Ejemplo 7
print("\n\nResultado Ejemplo 7:")
x = "hola"
for i in range(len(x)):
    print(f"Letra: {x[i]} - {i}")

