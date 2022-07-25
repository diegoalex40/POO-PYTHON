def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el ultimo mensaje....")
        funcion()
        print("Este es el primer mensaje...")
    return wrapper

@funcion_decoradora
def zumbido():
    print("Buzzzzz")
    
print(zumbido())