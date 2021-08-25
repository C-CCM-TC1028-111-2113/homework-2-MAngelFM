def main():
    #Escribe tu código debajo de esta línea
    age = int(input("Ingresa tu edad "))
    if age >= 18:
        ID = str(input("¿Tienes ID oficia? (s/n)"))
        if ID == str("s"):
            print("Tramite de Licencia Consedido")
        elif ID == str("n"):
            print("No cumples con los requisitos")
        else:
            print("Respuesta Incorrecta")
    else:
        print("No cumples con los requisitos")
    pass

if __name__ == '__main__':
    main()
