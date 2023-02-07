"""10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
    - Mes de consumo - Valor kw
    - Total kw consumido en el mes - estrato"""

valorEnergia={'MesConsumo':'','estrato':'','valorKW':'','totalConsumido':''}

valorEnergia['MesConsumo']=input("Ingrese Mes a Liquidar: ")
valorEnergia['estrato']=input("Ingrese el estrato de su hogar: ")
if valorEnergia['estrato'] == 1:
    valorEnergia['valorKW']= 86
elif valorEnergia['estrato'] == 2:
    valorEnergia['valorKW']= 98
elif valorEnergia['estrato'] == 3:
    valorEnergia['valorKW']= 100
elif valorEnergia['estrato'] == 4:
    valorEnergia['valorKW']= 123
elif valorEnergia['estrato'] == 5:
    valorEnergia['valorKW']= 145
elif valorEnergia['estrato'] == 6:
    valorEnergia['valorKW']= 200

