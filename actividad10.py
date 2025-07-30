products = {}
print("-"*8 + "BIENVENIDO AL INVENTARIO DE PRODUCTOS" + "-"*8)
quantity = int(input("Ingrese cuantos productos desea ingresar: "))
for i in range(quantity):
    print(f"Producto #{i+1}: ")
    code = input("Ingrese el codigo de producto(s) a ingresar: ")
    name = input("Ingrese el nombre de producto(s) a ingresar: ")
    category = input("Ingrese la categoria de producto(s) a ingresar: ")
    size = input("Ingrese la talla de producto(s) a ingresar: ")
    unity = input("Ingrese el precio unitario de producto(s) a ingresar: ")
    stock = input("Ingrese el stock de producto(s) a ingresar: ")
    products[code] = {
        "code": code,
        "name": name,
        "category": category,
        "size": size,
        "unity": unity,
        "stock": stock,
    }
print("lISTA DE PRODUCTOS\n")
for code in products:
    print(f"Producto #{code}: ")
    code = products[code]["code"]
    name = products[code]["name"]
    category = products[code]["category"]
    size = products[code]["size"]
    unity = products[code]["unity"]
    stock = products[code]["stock"]
print("-" * 8 + "Bienvenido a la busqueda de productos\n" + "-" * 8)
search = int(input("Ingrese el codigo del producto que desea ingresar: "))
