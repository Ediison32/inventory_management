
import os
from funciones import addProduct,chekProdcuto,updatePrices,removeProduct,calculateValue,showInventory



#1  añadir                        cantidad de productos
# productos { name, price, availableQuantity}

#2 consultar
# buscar producto por nombre y como resultado va a tener =  price and availableQuiatity 
# si el producto no esta no existe, notificar 

#3 actualizar price
# seleccionar un producto y cambiar su precio y cantidad disponible y que se actualice

#4 eliminar
# eliminar cualquier producto y esto elimina los demas items como price available

#5 calcular  el valor total inventario 
# calcular el valor total del inventario y mostrarlo 
# ---usar funcion anonima LAMBDA 

# Ejemplo de estructura que se va a usar 
# { productName : banano,  price : 45.4, }
""" 


lista = ["jose", "mauro", "alber", "jose","ana","jhon","max"]
print(lista)
del lista[1:3]
print(lista)

"""

menu=('''
    Selecciones\n 
    1. Add product.
    2. Check product. 
    3. Update price.
    4. Delete product. 
    5. Total value in inventory.
    6. Show inventory. 
    \n    Please enter an option: ''')

while True:

    case=input(menu)
    if case == '1':
        addProduct()
    elif case =='2':
        print(chekProdcuto())
    elif case == '3':
        updatePrices()
    elif case == '4':
        removeProduct()
    elif case == '5':
        calculateValue()
    elif case == '6':
        showInventory()
    else:
        os.system("clear")
        print("Error, please try again. ")

