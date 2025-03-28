#trabajo
estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = input("Ingrese las materias aprobadas (separadas por coma): ").split(",")
    materias = [m.strip() for m in materias]
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print("Estudiante agregado con éxito.")
def mostrar_estudiantes():
    print("Lista de estudiantes:")
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Materias: {', '.join(datos['materias'])}")
        print()
def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print("Estudiante eliminado con éxito.")
    else:
        print("Estudiante no encontrado.")
def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Materias: {', '.join(datos['materias'])}")
    else:
        print("Estudiante no encontrado.")
def buscar_palabra_clave():
    palabra = input("Ingrese la palabra clave a buscar: ")
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados:")
        for nombre in encontrados:
            print(nombre)
    else:
        print("No se encontraron estudiantes con la palabra clave.")
def main():
    while True:
        print("Menú:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Buscar palabra clave")
        print("6. Salir")
        opcion = input("Ingrese la opción: ")
        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                buscar_palabra_clave()
            case "6":
                print("Adiós.")
                break
            case _:
                print("Opción inválida. Por favor, intente nuevamente.")
if __name__ == "__main__":
    main()