"""9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
    *Nombre * Teléfono *Año de ingreso a la empresa
    *Apellidos *Edad."""



informacion={'nombre':'','apellidos':'','telefono':'','edad':'','añoIngreso':''}
informacion['nombre']=input("Porfavor ingrese su Nombre: ")
informacion['apellidos']=input("Porfavor ingrese su Apellido: ")
informacion['telefono']=input("Porfavor ingrese su Numero Telefono: ")
informacion['edad']=input("Porfavor ingrese su Edad: ")
informacion['añoIngreso']=input("Porfavor ingrese su Año de Ingreso: ")
print(list(informacion))