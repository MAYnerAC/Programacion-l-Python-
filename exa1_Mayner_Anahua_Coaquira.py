
#Ejercicio 1
def ejercicio01():

    print("Carta de Sandwich Rickys")
    print("Hamburguesa......$10.........(1)")
    print("Hot-dog..........$7..........(2)")
    print("Lomo saltado.....$10.........(3)")


    sandw=int(input("Ingrese en numero correspondiente de su pedido: "))

    if sandw==1 :
        precio=10
    elif sandw==2 :
        precio=7 
    elif sandw==3 :
        precio=10

    print("Ingredientes adicionales")
    print("Ninguno........0$..........(0)")
    print("Huevo..........2$..........(1)")
    print("Jamon..........3$..........(2)")
    print("Queso..........3$..........(3)")
    
    ad=int(input("Ingrese algun ingrediente adicional:"))

    if ad==1 :
        adicional=2
    elif ad==2 :
        adicional=3 
    elif ad==3 :
        adicional=3
    else:
        adicional=0

    precio=precio+adicional
    
    print("El precio de su compra es:",precio,"$")

ejercicio01()



#Ejercicio 2
#Ejercicio 3
#Ejercicio 4
def ejercicio04():

    print("Ingrese la cantidad a pagar por un prestamo:")
    prestamo=3580
    xmes=(54/12)/100

    mfinal=prestamo*(xmes)#^(18)

    print("El monto final es:",mfinal)


ejercicio04()