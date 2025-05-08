producList = [{'productName': 'banano', 'price': 45, 'availableQuantity': 54},
              {'productName': 'manzana', 'price': 4500, 'availableQuantity': 254},
              {'productName': 'pera', 'price': 6000, 'availableQuantity': 100}]

tupla= ()

def addProduct():   #consultar producto
    case = "yes" 
    while "yes" in case:
        

        productName = input("Please enter the name of the product: ")

        for name in producList:
            if name["productName"]== productName:
                print("The product name already exist !")
                break
        else:
            while True:
                try:
                    price =float(input("Please enter the price of the product: "))
                    availableQuantity = int(input("Please enter the quintity of the product: "))
                    store ={
                        "productName" : productName,
                        "price":price,
                        "availableQuantity": availableQuantity,
                    } 
                    producList.append(store)
                    print(f"\tproduct {productName} added")
                    #print(producList)
                    break
                except:
                    print("Invalid number, please try again.")
                    continue

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
        print("You have no added products!")

def updatePrices():  # actualizar presios

    if(len(producList) > 0):

        productName = input(" Please enter the name of the product to search: ")
        flag = None
        for product in producList:
            if product["productName"] == productName:
                value = float(input("Please enter the new prece:  "))
                product["price"] = value
                print("Update product ")
                print(f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                flag =True
        if not flag:
            print(" The product does not exist !") 
    else:
        print("You have no added products!")

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