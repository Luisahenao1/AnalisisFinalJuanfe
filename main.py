#COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd

#2. traer los datos
from data.simulador import generar_ventas

#3. convertir los datos en un DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())

#4. aplciar los filtros (5)
#print(dataFrame)

#Yo como administrador de la tienda quiero obtener las ventas de Eliana Restrepo
filtroUno=dataFrame.query("vendedor=='Eliana Restrepo'")
#print(filtroUno)

#Yo como administrador de la tienda quiero ver ventas con mas productos
filtroDos=dataFrame.query("cantidad >=3")
#print(filtroDos)

#Yo como administrador de la tienda quiero ver ventas por valores de mas de 900 mil
filtroTres=dataFrame.query("total >=900000")
#print(filtroTres)

#Yo como administrador de la tienda quiero ver las ventas de camisetas polo
filtroCuatro=dataFrame.query("producto=='camiseta POLO'")
#print(filtroCuatro)

#Yo como administrador de la tienda quiero ver las ventas de los productos que menos venden
filtroCinco=dataFrame.query("cantidad <=1")
print(filtroCinco)