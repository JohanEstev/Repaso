#Ejercisio 3

"""

segundos=int(input("Esciba la cantidad de  seguntos: "))

dias=segundos//(24*60*60)
segundos=segundos %(24*60*60)
horas =segundos //(60*60)
segundos=segundos %(60*60)
minutos=segundos //60
segundos=segundos//60


print("Dias:  {} - Horas: {} - Minutos :{} - Segundos:{}".format(dias,horas,minutos,segundos))


"""

"""

#Ejercisio 4


Asignaturas = ["Matematicas" ,"Fisica" , "Quimica" , "Historia", "Lenguaje"]

for Asignatura in Asignaturas:
    
    print("yo estudio "+ Asignatura)

"""

#Ejercisio 5 

Materias=["Matematicas","Fisica","Quimica" , "Historia", "lenguaje "]
Notas=[]

for Materia in Materias:
    Nota =(input("Que nota  has sacado " + Materia+"?" ))
    Notas.append(Nota)

for i in range(len(Materias)):
    
    print ("En"  + Materias[i] + "has sacado " + Notas[i])
  
    



