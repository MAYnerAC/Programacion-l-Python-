#Ejercicio 6

#Dada una lista de números enteros, escribir una función que:
# 1. Devuelva una lista con todos los que sean primos. 
# #2. Devuelva la sumatoria y el promedio de los valores. 
# #3. Devuelva una lista con el factorial de cada uno de esos números


l=[1,2,3,4,5,6,7,8,9,10]

def factorial(n):
    r=2
    nf=n*(n-1)
    #print(nf)
    for i in range(n):
        if n>r+1 :  
            nf=nf*(n-r)
            r=r+1
            i=i+1
            #print(nf)

    print("El resultado de ",l[i],"! es: ",nf)

#num=int(input("Ingrese un numero: "))
#factorial(num)
#################################################################

def suma():

    suma=0
    j=0
    for i in range(10):

        suma=suma+(l[i]+l[i+j])
        j=j+1

    print("La suma total seria: ")
    print(suma)
    


def multiplicacion():

    multiplica=1

    for i in range(10):

        multiplica=multiplica*(l[i]*l[i+1])

    print("La muitiplicacion total seria: ")
    print(multiplica)

################################################################
def main(lista):
    for i in range(10):
        factorial(l[i])
        i=i+1

    suma()

    multiplicacion()

main(l)

