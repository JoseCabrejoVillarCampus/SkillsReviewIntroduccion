"""8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados."""


print("-----------SUMA Y RESTA--------------\n"
"(SUMA)  Opcion A \n"
"(RESTA) Opcion B \n"
)


opcion=""
opcion=input("Porfavor ingrese una opcion: ")

if opcion=="A":
    num1=input("porfavor ingrese el primer numero entero positivo: ")
    num2=input("porfavor ingrese el segundo numero entero positivo: ")
    print(num1+num2)
elif opcion=="B":
    num1=input("porfavor ingrese el primer numero entero positivo: ")
    num2=input("porfavor ingrese el segundo numero entero positivo: ")
    print(num1-num2)
else:
    print("Opcion no correcta")
    