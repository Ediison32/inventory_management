producList = [{'productName': 'banano', 'price': '45', 'availableQuantity': '54'},
              {'productName': 'manzana', 'price': '4500', 'availableQuantity': '254'},
              {'productName': 'pera', 'price': '6000', 'availableQuantity': '100'}]

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
                    print(store)
                    producList.append(store)
                    print(f"\tproduct {productName} added")
                    break
                except:
                    print("Invalid number, please try again.")
                    continue

        case = input("Do you want to add another product? yes, to add: ")

def chekProdcuto():  # consultar producto
    pass

def updatePrices():  # actualizar presios
    pass

def removeProduct():  # eliminar producto
    pass

def calculateValue():  # calcular el total del inventario 
    pass
