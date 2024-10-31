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
materia4 = input("Escriba la materia: "), int(input("Escriba la nota: "))
materia5 = input("Escriba la materia: "), int(input("Escriba la nota: "))
#aqui se guarfa la lista
lista = ([materia1, materia2,materia3,materia4,materia5])
#aqui se ejecuta la funcion
materias(lista)
