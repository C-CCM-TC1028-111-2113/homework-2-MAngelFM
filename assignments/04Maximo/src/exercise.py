def main():
# Escribe el código adecuado para completar el programa
    num1 = int(input("Ingresa el primer numero "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))
    if num2 < num1 > num3:
        print("",num1)
    elif num1 < num2 > num3:
        print("",num2)
    elif num1 < num3 > num2:
        print("",num3)
 

if __name__ == '__main__':
    main()
