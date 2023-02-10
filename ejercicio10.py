"""10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
    - Mes de consumo - Valor kw
    - Total kw consumido en el mes - estrato"""

valorEnergia={'Mes_de_Consumo':'','estrato':'','valorKW':'','total_Consumido':''}

valorEnergia['Mes_de_Consumo']=input("Ingrese Mes a Liquidar: ")
valorEnergia['estrato']=int(input("Ingrese el estrato de su hogar: "))
if valorEnergia['estrato'] == 1:
    valorEnergia['valorKW']= 325.6
elif valorEnergia['estrato'] == 2:
    valorEnergia['valorKW']= 394.5
elif valorEnergia['estrato'] == 3:
    valorEnergia['valorKW']= 667.9
elif valorEnergia['estrato'] == 4:
    valorEnergia['valorKW']= 785.8
elif valorEnergia['estrato'] == 5:
    valorEnergia['valorKW']= 942.9
elif valorEnergia['estrato'] == 6:
    valorEnergia['valorKW']= 1200.5
valorEnergia['total_Consumido']= int(input("Ingrese el total consumido: "))

valorEnergiaPagar=float(valorEnergia['valorKW']*valorEnergia['total_Consumido'])

print(list[valorEnergia])
print("El Valor a Pagar es:", valorEnergiaPagar)
