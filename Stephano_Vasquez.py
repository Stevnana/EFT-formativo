asignaturas = {
    "DSY1103" : ["Fullstack", "L4", 7, 42, 12],
    "FPY1101" : ["Programacion", "L6", 7, 21, 23],
    "OCY1101" : ["Cyberseguridad", "online", 4, 31, 14],
    "DSY1101" : ["Cloud Computing", "L3", 4, 31, 6],
    "DSY1105" : ["Aplicaciones Mobile", "L9", 5, 15, 21],
    "MDY3131" : ["Base de Datos", "L3", 5, 11, 12]
}

def iniciafuncion(nombre):
    print("inicia la funcion", nombre)
iniciafuncion("totalalumnos")

def totalalumnos(codigo):
    iniciafuncion("totalalumnos")
    asignatura = asignaturas[codigo]
    total = asignatura[3] + asignatura[4]
    print(total)
    return total

   
