#aqui se imprime el nombre
# '\n' sirve para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se define una funcion
def materias(lista):
    #esta parte ayudara a que materia si esta en lista
    for  materia in lista:
        #se imprimira los siguiente
        #osea que se puede tomar como si cada parte de la lista la divide en 'materia'
        #esto provoca que se tone como las materias posteriormente guaradadas pero
        # con la diferencia de que no tendras que escribir materia por materia
        print("Su nota es de -",materia[1], "y corresponde a: ",materia[0])
#aqui se guardan las variables
materia1 = input("Escriba la materia: "), int(input("Escriba la nota: "))
materia2 = input("Escriba la materia: "), int(input("Escriba la nota: "))
materia3 = input("Escriba la materia: "), int(input("Escriba la nota: "))

#aqui se guarfa la lista
lista = ([materia1, materia2,materia3])
#aqui se inicia una secuencia if else para ver si la materia es menor a 6 entonces se eliminara de la lista
# pop() sirve para eliminar una variable de la lista
# del sirve para lo mismo, pero solo si se coloca []
if materia1[1] < 6:
    del lista[0]
    print("\nDebes repetir la materia",materia1,"\n")
if materia2[1] < 6:
    lista.pop(1)
    print("\nDebes repetir la materia",materia2,"\n")
if materia3[1] < 6:
    print("\nDebes repetir la materia",materia3,"\n")
    lista.pop()
#se ejecuta la funcion
materias(lista)
#y se imprime la lista con los elementos ya eleminados
print("\nAprobaste: ",lista)



