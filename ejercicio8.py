"""8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados."""


print("-----------SUMA Y RESTA--------------\n"
"(SUMA)  Opcion A \n"
"(RESTA) Opcion B \n"
)
opcion=""
opcion=input("Porfavor ingrese una opcion: ")


if opcion=="A":
    print("Has Elegido Sumar")
    num1=int(input("porfavor ingrese el primer numero entero: "))
    if num1%2==0:
        print("has elegido un numero par")
    else: 
        print("Has elegido un numero impar")
    num2=int(input("porfavor ingrese el segundo numero entero: "))
    if num1%2==0:
        print("has elegido un numero par")
    else: 
        print("Has elegido un numero impar")
    print(num1+num2)
elif opcion=="B":
    num1=int(input("porfavor ingrese el primer numero: entero"))
    if num1%2==0:
        print("has elegido un numero par")
    else: 
        print("Has elegido un numero impar")
    num2=int(input("porfavor ingrese el segundo numero: entero"))
    if num1%2==0:
        print("has elegido un numero par")
    else: 
        print("Has elegido un numero impar")
    print(num1-num2)
else:
    print("Opcion no correcta")
    