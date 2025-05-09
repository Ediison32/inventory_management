

producList = [{'productName': 'banano', 'price': 45, 'availableQuantity': 54},
              {'productName': 'manzana', 'price': 4500, 'availableQuantity': 254},
              {'productName': 'pera', 'price': 6000, 'availableQuantity': 100}]

tupla= ()

def verif(msg, msge, tipo=str, extravalidation=None):
    while True:
        try:
            val = tipo(input(msg))
            if extravalidation and not extravalidation(val):
                print(msge )
                continue
            return val
        except:
            print(msge)

def addProduct():   #consultar producto
    case = "yes" 
    while "yes" in case:
        productName = input("Please enter the name of the product: ")
        for name in producList:
            if name["productName"]== productName:
                print("The product name already exist !")
                break
        price =verif("Please enter the price of the product: ","\tInvalid number, please try again ",float, lambda x: x >= 0)
        availableQuantity = verif("Please enter the quintity of the product: ", "\tInvalid number, please try again", int,lambda x: x >= 0)
        store ={
            "productName" : productName,
            "price":price,
            "availableQuantity": availableQuantity,
        } 
        producList.append(store)
        print(f"\tproduct {productName} added")
        
            #print(producList)      
        case = input("Do you want to add another product? yes, to add: ")

def chekProdcuto():  # consultar producto
    
    if len(producList)> 0:
        productName=input(" Please enter the name of the product to search: ")
        flag = None
        for product in producList:
                if product["productName"]== productName:
                    foundProduct = (f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                    flag =True
                    return foundProduct
        if not flag:
            print(" The product does not exist !")        
    else:
        print("You have no added any products!")

def updatePrices():  # actualizar presios

    if(len(producList) > 0):

        productName = input(" Please enter the name of the product to search: ")
        flag = None
        for product in producList:
            if product["productName"] == productName:
                #value = float(input("Please enter the new prece:  "))
                value = verif("Please enter the new prece:  ","\t Invalid number, please try again",float,lambda x: x >= 0)
                product["price"] = value
                print("Update product ")
                print(f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                flag =True
        if not flag:
            print(" The product does not exist !") 
    else:
        print("You have no added any products!")

def removeProduct():  # eliminar producto
    if(len(producList) > 0):
            productName = input(" Please enter the name of the product you want to delete: ")
            flag = None
            for i,product in enumerate(producList,0):
                    if product["productName"] == productName:
                        del producList[i]
                        print(f"Product removed!")
                        flag =True

            if not flag:
                    print(" The product does not exist !") 

def calculateValue():  # calcular el total del inventario 
    global tupla
    calculate = sum( map( lambda product : product["price"] * product["availableQuantity"],producList))
    x = list(tupla)
    x.append(calculate) 
    tupla=tuple(x)
    print(f"\n\tTotal inventory {tupla}")


def showInventory():
    if len(producList)> 0:
        print("\n\t|\t\t SHOW INVENTORY ")
        print("\t|"+ "-"*60+ " |")
        for product in producList:
            print(f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} ")
            
    else:
        print("You have no added products!")

