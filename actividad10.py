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

