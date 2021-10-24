

tupla1=(3,6,8,12)
tupla2=(4,9,2,5)

def suma():

    suma=0

    for i in range(4):

        suma=suma+(tupla1[i]+tupla2[i])

    print("La suma total seria: ")
    print(suma)
    


def multiplicacion():

    multiplica=1

    for i in range(4):

        multiplica=multiplica*(tupla1[i]*tupla2[i])

    print("La muitiplicacion total seria: ")
    print(multiplica)


def main():

    suma()
    multiplicacion()

main()