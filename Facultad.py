class Estudiantes:
    def __init__(self,nombre,apellido,num_matricula,carrera,ID_alumno):
        self.nombre = nombre
        self.apellido = apellido
        self.num_matricula = num_matricula
        self.carrera = carrera
        self.ID_alumno = ID_alumno
        self.cursos_inscriptos = []
        
    def agregar_curso(self, curso_obj):
        self.cursos_inscriptos.append(curso_obj)
    
        
class Cursos:
    def __init__(self,nombre_curso,codigo_curso,profesor_encargado,capacidad_max):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.profesor_encargado = profesor_encargado
        self.cupo_actual = 0
        self.alumnos_inscriptos = []
        self.capacidad_max = capacidad_max

        
    def cupos_disponibles(self):
        return self.cupo_actual < self.capacidad_max
    
    def inscripciones(self,estudiante_obj):
        if self.cupo_actual < self.capacidad_max:
            self.alumnos_inscriptos.append(estudiante_obj)
            self.cupo_actual += 1
            return True
        return False
    
    def baja_del_curso(self, estudiante_obj):
        if estudiante_obj in self.alumnos_inscriptos:
            self.alumnos_inscriptos.remove(estudiante_obj)
            self.cupo_actual -= 1
            return True
        return False
    
    def __str__(self):
        print("-" * 30)
        return f"Curso: {self.nombre_curso} | codigo del curso: {self.codigo_curso} | profesor a cargo: {self.profesor_encargado} | cupos actuales: {self.cupo_actual} | cupo max: {self.capacidad_max}"
    
    
class Facultad:
    def __init__(self):
        self.clases = []
        self.estudiantes = []
        
    def agregar_clase(self,curso:Cursos):
        if isinstance(curso,Cursos):
            self.clases.append(curso)
        
    def agregar_alumno(self,estudiante:Estudiantes):
        if isinstance(estudiante,Estudiantes):
            self.estudiantes.append(estudiante)
    
    def mostrar_clase(self,codigo_curso):
        for c in self.clases:
            if c.codigo_curso == codigo_curso:
                print(f"nombre del curso: {c.nombre_curso} | codigo del curso: {c.codigo_curso} | profesor a cargo: {c.profesor_encargado} | capacidad maxima: {c.capacidad_max}")
                print("-" * 30)
                return
        print("-" * 30)
        print("Clase no encontrada")
        print("-" * 30)
    
    def mostrar_alumno(self,ID_alumno):
        for a in self.estudiantes:
            if a.ID_alumno == ID_alumno:
                print(f"nombre del alumno: {a.nombre} |  Apellido : {a.apellido} | N° matricula: {a.num_matricula} | Carrera: {a.carrera} | ID Alumno: {a.ID_alumno}")
                print("-" * 30)
                return
        print("-" * 30)
        print("alumno no encontrado")
        print("-" * 30)
    
    def inscripcion_curso(self,ID_alumno,codigo_curso):
        alumno_encontrado = None
        curso_encontrado = None

        for a in self.estudiantes:
            if a.ID_alumno == ID_alumno:
                alumno_encontrado = a
                break
        
        for c in self.clases:
            if c.codigo_curso == codigo_curso:
                curso_encontrado = c
                break

        if alumno_encontrado and curso_encontrado:
            if curso_encontrado.cupos_disponibles():
                curso_encontrado.inscripciones(alumno_encontrado)
                alumno_encontrado.agregar_curso(curso_encontrado)
                print("-" * 30)
                print(f"Se Inscribio exitosamente al Curso: {curso_encontrado.nombre_curso} el Alumno {alumno_encontrado.nombre}")
                print("-" * 30)
            else:
                print("-" * 30)
                print("No hay cupos disponibles.")
                print("-" * 30)

        else:
            print("-" * 30)
            print("Alumno o Curso no encontrado.")
            print("-" * 30)
        
    def dar_baja_curso(self,ID_alumno,codigo_curso):
        alumno_encontrado = None
        curso_encontrado = None

        for a in self.estudiantes:
            if a.ID_alumno == ID_alumno:
                alumno_encontrado = a
                break
            
        for c in self.clases:
            if c.codigo_curso == codigo_curso:
                curso_encontrado = c
                break
            
        if alumno_encontrado and curso_encontrado :
            se_dio_de_baja = curso_encontrado.baja_del_curso(alumno_encontrado)
            if se_dio_de_baja:
                alumno_encontrado.cursos_inscriptos.remove(curso_encontrado)
                print(f"Baja exitosa: {alumno_encontrado.nombre} ya no pertenece a {curso_encontrado.nombre_curso}.")
                print("-" * 30)
            else:
                print(f"Error: El alumno no estaba inscripto en el curso {curso_encontrado.nombre_curso}.")
                print("-" * 30)
        else:
            print("Error: No se encontró el Alumno o el Curso en el sistema.")
            print("-" * 30)
    
    def estado_clases(self,):
        for c in self.clases:
            print (f"Nombre de la Clase: {c.nombre_curso} | Codigo de la Clase:{c.codigo_curso} | Profesor a Cargo: {c.profesor_encargado} | Cupo Actual: {c.cupo_actual} | Cupo Maximo: {c.capacidad_max}")
            print("-" * 30)
    
    def estado_alumnos(self,):
        for a in self.estudiantes:
            print("-" * 30)
            print (f"Nombre: {a.nombre} | ID_alumno: {a.ID_alumno}")
            print ("Inscripto al curso: ")
            
            if len(a.cursos_inscriptos) == 0:
                print("   -Ninguno")
            else:
                for c in a.cursos_inscriptos:
                    print(f"-{c.nombre_curso} | Codigo de Clase: {c.codigo_curso}")
            print("-" * 30)


def pedir_numero(mensaje):
    dato = input(mensaje)
    while not dato.isdigit():
        print("-" * 30)
        print("Error: El valor ingresado debe contener solo números.")
        dato = input(mensaje)
    return dato


def pedir_texto(mensaje):
    dato = input(mensaje)
    while not dato.replace(" ", "").isalpha() or dato.strip() == "":
        print("-" * 30)
        print("Error: El campo solo debe contener letras y espacios.")
        dato = input(mensaje)
    return dato


def pedir_texto_obligatorio(mensaje):
    dato = input(mensaje)
    # .strip() == "" detecta si el usuario apretó Enter o dejó solo espacios
    while dato.strip() == "":
        print("-" * 30)
        print("Error: Este campo es obligatorio y no puede quedar vacío.")
        dato = input(mensaje)
    return dato


def main():
    facultad = Facultad()
    
    while True:
        print("Sistema de Gestion de la Facultad")
        print("1. Agregar Clase")
        print("2. Agregar Alumno")
        print("3. Mostrar Clase")
        print("4. Mostrar Alumno")
        print("5. Inscribirse a Cursos")
        print("6. Darse de Baja (cursos)")
        print("7. Consultar Estado Clases")
        print("8. Consultar Estado Alumnos")
        print("0. Salir")
        
        opcion = input("Seleccione una opcion: ")
        print("-" * 30)
        
        if opcion == "1":
            nombre_curso = pedir_texto_obligatorio ("ingrese el nombre de la clase: ")
            codigo_curso = int(pedir_numero ("ingrese el codigo del curso: "))
            profesor_encargado = pedir_texto("ingrese el nombre del profesor encargado: ")
            capacidad_max = int(pedir_numero("ingrese la capacidad maxima de la clase: "))
            curso = Cursos(nombre_curso,codigo_curso,profesor_encargado,capacidad_max)
            facultad.agregar_clase(curso)
            print("Curso agregado exitosamente.")
            print("-" * 30)
            
        elif opcion == "2":
            nombre = pedir_texto ("Ingrese el nombre del Alumno: ")
            apellido = pedir_texto ("Ingrese el Apellido del Alumno: ")
            num_matricula = int(pedir_numero("Ingrese el numero de la Matricula: "))
            carrera = pedir_texto_obligatorio("Ingrese el Nombre de la Carrera: ")
            ID_alumno = int(pedir_numero("Ingrese el ID del alumno: "))
            estudiante = Estudiantes(nombre,apellido,num_matricula,carrera,ID_alumno)
            facultad.agregar_alumno(estudiante)
            print("Estudiante agregado exitosamente.")
            print("-" * 30)
            
        elif opcion == "3":
            while True:
                codigo_curso_input = input("ingrese el codigo del curso: ")
                try:
                    codigo_curso = int(codigo_curso_input) 
                    facultad.mostrar_clase(codigo_curso)
                    break
                except ValueError:
                    print("-" * 30)
                    print("Error: El codigo del curso proporcionado debe ser un número válido.")
                    print("-" * 30)
                    
        elif opcion == "4":
            while True:
                ID_input = input("ingrese el ID del alumno: ")
                try:
                    ID_alumno = int(ID_input) 
                    facultad.mostrar_alumno(ID_alumno)
                    break
                except ValueError:
                    print("-" * 30)
                    print("Error: El ID proporcionado debe ser un número válido.")
                    print("-" * 30)
                    
        elif opcion == "5":
            ID_alumno = int(pedir_numero("ingrese su ID de alumno: "))
            codigo_curso = int(pedir_numero("ingrese el codigo del curso: "))
            facultad.inscripcion_curso(ID_alumno,codigo_curso)
            
        elif opcion == "6":
            ID_alumno = int(pedir_numero("ingrese su ID de alumno: "))
            codigo_curso = int(pedir_numero("ingrese el codigo del curso: "))
            facultad.dar_baja_curso(ID_alumno,codigo_curso)
            
        elif opcion == "7":
            print("--- Estado de las clases ---")
            facultad.estado_clases()
            
        elif opcion == "8":
            print("--- Estado de los alumnos ---")
            facultad.estado_alumnos()
            
        elif opcion == "0":
            print("Saliendo del sistema")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")
            print("-" * 30)
            
if __name__ == "__main__":
    main()
