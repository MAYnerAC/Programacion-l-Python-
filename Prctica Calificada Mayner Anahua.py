
#Ejecicio 1
mn=int(input("Ingrese una distancia en millas marinas: "))
m=mn*1852
print("La distancia es: ", m,"m")


#Ejercicio 2
#num=int(input("Ingrese un numero: "))



#Ejercicio 3
print("Ingrese su fecha de nacimiento: ")
dia=int(input("Día: "))
mes=int(input("Mes: "))
yr=int(input("Año: "))

print("La fecha de hoy es: 27/08/2021 ")
hoy=737932

edad=dia+(mes*30)+(yr*365)
edad=hoy-edad
print("Usted tiene aproximadamente: ", edad," dias de vida")

#Ejercicio 4
km=int(input("Ingrese la cantidad de kilometros recorridos: "))
pg=int(input("Ingrese el precio de la gasolina que usted pago por cada litro: "))
d=int(input("Ingrese el dinero que gasto durante su viaje: "))
h=int(input("Ingrese cuanto tiempo ha tardado su viaje en horas: "))


litros=d/pg

cdgl=litros/100   


cdgs=d/100


print("Su consumo de gasolina por cada 100 kilometros es: ")
print("En litros: ",cdgl,"L")
print("En soles: ",cdgs)
