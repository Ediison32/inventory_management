producList = []

def addProduct():   #consultar producto 
    priceName = input("Enter the product name: ")
    price =input("Enter the price of the product: ")
    availableQuantity = input("Enter the quintity of the product: ")
    store ={
        store["priceName"] : priceName,
        store["price"]:price,
        store["availableQuantity"]: availableQuantity
     } 
    print(store)
    producList.append(store)


def chekProdcuto():  # consultar producto
    pass

def updatePrices():  # actualizar presios
    pass

def removeProduct():  # eliminar producto
    pass

def calculateValue():  # calcular el total del inventario 
    pass
