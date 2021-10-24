#Ejercicio 1
#Ejercicio 3
def ejercicio3():

    h=int(input("Ingrese la herencia a repartir: "))

    n=int(input("Ingrese la cantidad de hijos que tiene: "))


    if n<4:
        i=1
        h=h/n
        
        while i<=n:
            print("Para el hijo ",i," le corresponde",h)
            i=i+1
            

    elif n>=4 : 
        i=2
        mayor=h/2
        menor=mayor/(n-1)
        
        while i<=n:
            print("Para el hijo mayor le corresponde",mayor)
            print("Para el resto de hijos: ")
            print("Para el hijo ",i," le corresponde",menor)
            i=i+1
            

ejercicio3()