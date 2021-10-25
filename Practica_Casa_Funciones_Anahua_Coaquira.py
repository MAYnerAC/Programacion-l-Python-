
#from Practica_Ejercicios_Funciones_Anahua_Coaquira import cuenta_regresiva

#Ejercicio 1

#Escribe una función que devuelva el término N (siendo N un número
#entero positivo) de la serie de Fibonacci, esta sigue la siguiente serie: 1, 1,
#2, 3, 5, 8, 13, 21… y así sucesivamente. Date cuenta, que para obtener un
#numero, suma los dos números anteriores. Por ejemplo, si introducimos
#un 3, la función nos devuelve el 2.

def fibo(r):
    a=0
    b=1
    for i in range(r):
        c=a+b
        a=b
        b=c
        print(a)
    print("Su numero es: ",a)

print("SERIE FIBONACCI")
n=int(input("Ingrese un numero: "))
fibo(n)  

#Ejercicio 2
#Ejercicio 3

#Ejercicio 4
#######Creación de una función que retorna el mayor de 3 números entero recibidos en sus parámetros.###########

def mayor(a,b,c):
    if a>b and a>c:
        print("El numero mayor es: ",a)
    elif b>a and b>c:
        print("El numero mayor es: ",b)
    elif c>a and c>b:
        print("El numero mayor es: ",c)

print("NUMERO MAYOR")    
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
z=int(input("Ingrese otro numero: "))
mayor(x,y,z)

#return

#def may(a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    elif c>a and c>b:
#        return c
#
#x=int(input("Ingrese un numero: "))
#y=int(input("Ingrese otro numero: "))
#z=int(input("Ingrese otro numero: "))
#may(x,y,z)
#print("El numero mayor es mayyy: ",may(x,y,z))




#Ejercicio 5

#Realice una función llamada TablaPotencias( N ), que genere en pantalla
#la tabla de potencias del numero decimal N recibido como parámetro.
#Observe a la derecha un ejemplo del resultado de esta función

def TablaPotencias(N):
    p=0
    for i in range(6):              #(Hasta la potencia 5 "6-1") #Se puede elegir hasta q potencia mostrar la tabla
        rpta=pow(N,p)
        print(N,"^",p," = ",round(rpta,2)," |")       #p=p+1                          #diferente#
        p=p+1                           #print(N,"^",p-1," = ",rpta)    #orden#

print("TABLA DE POTENCIAS")
a=float(input("Ingrese un numero decimal: "))
TablaPotencias(a)


#Ejercicio 6 (En otro archivo)


#Ejercicio 7
#Realiza una función que indique si un número pasado por parámetro es par o impar.

def par_impar(n):
    n=n%2
    if n==0:
        print("Su numero en PAR")
    else :
        print("Su numero es IMPAR")


print("NUMERO PAR E IMPAR")
s=int(input("Ingrese un numero: "))
par_impar(s)

#Ejercicio 8

#Crea una función que dados dos números mostrará todos los números que hay entre ellos.

def numeros(a,b):
    print("Entre",a,"y",b," se encuentran los siguientes numeros enteros: ")
    for i in range(a,b):
        if a<b:
            a=a+1
            i=i+1
            if a!=b:
                print(a)

print("TODOS LOS NUMEROS ENTRE...")
inicio=int(input("Ingrese el primer numero: "))
final=int(input("Ingrese el segundo numero: "))
numeros(inicio,final)


#Ejercicio 9

#Calcular el factorial de un número, usando funciones. (con for, while y con la función factorial) 

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

print("FACTORIAL CON FOR")
num=int(input("Ingrese un numero: "))
factorial(num)



def factorial_2_while(n): #incompleto
    n=n+1
    i=0
    r=2
    nf=n*(n-1)
    print(nf)
    while i-1<n:
        if n>r+1:  
            nf=nf*(n-r)
            r=r+1
            i=i+1
            print(nf)
        break

    print("El resultado de ",fact_w,"! es: ",nf)

print("FACTORIAL CON WHILE")
fact_w=int(input("Ingrese un numero: "))
factorial_2_while(fact_w)   