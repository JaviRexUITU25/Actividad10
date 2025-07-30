products = {}
print("-"*8 + "BIENVENIDO AL INVENTARIO DE PRODUCTOS" + "-"*8)
quantity = int(input("Ingrese cuantos productos desea ingresar: "))
for i in range(quantity):
    print(f"Producto #{i+1}: ")
    while True:
        code = input("Ingrese el codigo de producto(s) a ingresar: ")
        if code in products:
            print("Este codigo ya existe")
        else:
            break
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
for code, dates in products.items():
    print(f"Producto #{code}: ")
    print(f" Nombre: {dates["name"]}")
    print(f" categoria: {dates["category"]}")
    print(f" talla: {dates["size"]}")
    print(f" precio unitario: Q{dates["unity"]} quetzales")
    print(f" stock: {dates["stock"]} productos")
print("-" * 8 + "Bienvenido a la busqueda de productos\n" + "-" * 8)
search = int(input("Ingrese el codigo del producto que desea ingresar: "))
if search in products:
    print("¡Producto encontrado!")
    print(f"Codigo del producto #{search}: {products['code']}")
    print(f" Nombre del producto #{search}: {products['name']}")
    print(f"Categoria del producto #{search}: {products['category']}")
    print(f"Talla del producto #{search}: {products['size']}")
    print(f"precio unitario del producto #{search}: Q{products['unity']}")
    print(f"Quedan: {search}: #{products['stock']} productos")
else:
    print(f"Codigo del producto invalido")