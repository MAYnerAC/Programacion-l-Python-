c=("d","e","r","t")
d=("","","","")
print(type(c))
print(c[1:])
print(c[:3])
print(c[1:2])
print(c+d)
print(c*3)
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
print(tup1<tup2)
q=["ana",34,45,67,[2,4,6],"rocio",3.5,7.8]
t=(3,5,8,"ana")
d={"nombre":"Lili","apellido":"Vega","edad":12,3:4}
q.append("german")
print(q)

d["edad"]=25    #Cambio de un valor dentro del diccionario

print(d["apellido"],d["edad"])

def claves():
    clave1=input("ingrese una clave para el diccionario")
    clave2=input("ingrese una clave para el diccionario")
    clave3=input("ingrese una clave para el diccionario")
    return 


def main():
    valor1=input("")

print("Creando diccionario...")




    



q=["ana",34,45,67,[2,4,6],"rocio",3.5,7.8]              #lista
t=(3,5,8,"ana")                                         #tupla
d={"nombre":"Lili","apellido":"Vega","edad":12,3:4}     #dicccionario

q.append("german")      #Agreaga en la ultima posicion lo indicado "german"

                        #Se considera el primer valor desde "0", como: 0,1,2,3,4,...

q.insert(3,"german")    #Inserta en una posicion espesifica segun lo indicado "3", el valor "german"
