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
        print("Su materia es -",materia[0],"-", "y creditos conseguidos: ",materia[1])

#aqui se guardan las variables
materia1 = input("Escriba la materia: "), int(input("Escriba los creditos conseguidos: "))
materia2 = input("Escriba la materia: "), int(input("Escriba los creditos conseguidos: "))
materia3 = input("Escriba la materia: "), int(input("Escriba los creditos conseguidos: "))

#aqui se guarfa la lista
#posteriormente se imprime la lista
#por ultimo se ejecuta la funcion
lista = [materia1, materia2,materia3]
print(" ")
print(lista)
print(" ")
materias(lista)
print(" ")
#aqui se hace una operacion para sumar todos los creditos
credits = (materia1[1] + materia2[1]  + materia3[1] )
#aqui se imprime el resultado
print("Total de creditos: ",credits)