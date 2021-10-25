


def saludo(nombre):
    print('¡Hola ' + nombre +'!')

saludo("Liliana")
saludo('Mercedes')


#######################area de ciindro y circulo###############################
def area_circulo(radio):
    pi = 3.1415
    area=pi*radio**2
    return(area)

def volumen_cilindro(area, altura):
    volumen=area*altura
    return volumen

print("El area del circulo es: ",area_circulo(3))

print("El volumen del cilindro es: ",volumen_cilindro(4,5))



##############################Una función que cacula el cuadrado de los números dados.#########################

list1=(1,2,3,4,5)
list2=(2.3, 5.7, 6.8, 9.7, 12.1, 15.6)



def cuadrados():

    list1_2=1
    list2_2=1

    print("El cuadrado de los numeros de ",list1,"es: ")
    for i in range(5):
    
        list1_2=(list1[i])*(list1[i])

        print(list1_2)

    print("El cuadrado de los numeros de ",list2,"es: ")
    for i in range(6):
        
        list2_2=(list2[i])*(list2[i])

        print(list2_2)


def main():
    
    cuadrados()

main()

##########################crear una función que realice la Cuenta regresiva hasta cero a partir de un número###########


def cuenta_regresiva (s):
    print(s)
    for i in range(s):
        s=s-1
        i=i+1
        print(s)
    print("Se acabo!!!")

print("CUENTA REGRESIVA")
numpartida=int(input("Ingrese un numero para comenzar: "))
cuenta_regresiva(numpartida)



########################crear una función que cacule el factorial de un número#####################


def factorial(n):
    r=2
    nf=n*(n-1)
    print(nf)
    for i in range(n):
        if n>r+1 :  
            nf=nf*(n-r)
            r=r+1
            i=i+1
            print(nf)
    if nf==0:
        nf=1
    print("El resultado de ",num,"! es: ",nf)

print("FACTORIAL DE UN NUMERO")
num=int(input("Ingrese un numero: "))
factorial(num)







