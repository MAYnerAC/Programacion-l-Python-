

def operaciones(a,b):
    suma=a+b
    resta=a-b
    multiplica=a*b
    divide=a/b
    return(suma,resta,multiplica,divide)


def main():
    num1=int(input("Ingrese un valor: "))
    num2=int(input("Ingrese otro valor: "))

    suma,resta,multiplica,divide=operaciones(num1,num2)
    print("El valor de la suma es: ",suma)
    print("El valor de la resta es: ",resta)
    print("El valor de la multiplicacion es: ",multiplica)
    print("El valor de la division es: ",divide)

main()
