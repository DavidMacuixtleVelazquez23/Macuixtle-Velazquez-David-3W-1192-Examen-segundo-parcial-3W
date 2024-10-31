#aqui se imprime el nombre
# '\n' sirve para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se guardaran varios datos
nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
dirre = input("Escriba su direccion: ")
num = input("Escriba su numero telefonico: ")
#aqui se declara el diccionario con {}
diccio = {
    "Tu nombre es": nombre,
    "Tienes: " :  edad,
    "tu direccin es: " : dirre,
    "No.Telefonico: " : num
}
#aqui se imprime el diccionario
print(diccio)