class Libro:
    def __init__(self,titulo,autor,ISBN,ejemplar):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.ejemplar = ejemplar
        self.total_ejemplares = ejemplar
        
    def estaDisponible(self):
        return self.ejemplar >= 1
            
        
    def prestarLibro(self):
        if self.ejemplar >= 1:
            self.ejemplar -=1
            return True
        
    def devolverLibro(self):
        if self.ejemplar < self.total_ejemplares:
            self.ejemplar += 1
    
    def __str__(self):
        print("-" * 30)
        return f"Libro: {self.titulo} | ISBN: {self.ISBN} | Stock: {self.ejemplar}/{self.total_ejemplares}"
        
class Miembro:
    def __init__(self,nombre,DNI):
        self.nombre = nombre
        self.DNI = DNI
        self.libros_prestados = []
        
    def prestar(self,libro_obj):
        self.libros_prestados.append(libro_obj)
                
    def devolver(self,ISBN):
        for x in self.libros_prestados:
            if x.ISBN == ISBN:
                self.libros_prestados.remove(x)
                break
    
    def __str__(self):
        libros_nombres = [lib.titulo for lib in self.libros_prestados]
        print("-" * 30)
        return f"Miembro: {self.nombre} | DNI: {self.DNI} | Posee: {libros_nombres}"
    
            
        
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []
        
        
        ## opcion 1
    def agregar_libro(self,libro:Libro):
        if isinstance(libro,Libro):
            self.libros.append(libro)
    
    
        ## opcion 2
    def agregar_miembro(self,miembro:Miembro):        
        if isinstance(miembro,Miembro):
            self.miembros.append(miembro)
        
        
        ## opcion 3
    def mostrarMiembro(self,dni):  
        try:
            for m in self.miembros:
                if int(m.DNI) == int(dni):
                    print(f"Nombre: {m.nombre} | DNI: {m.DNI}")
                    print("-" * 30)
                    return
            print("Miembro no encontrado")
            print("-" * 30)
        except ValueError:
            print("Error: El DNI proporcionado no es un número válido.")
            print("-" * 30)
            
            
        ## opcion 4
    def mostrarLibro(self,isbn):  
        for l in self.libros:
            if l.ISBN == isbn:
                print(f"Título: {l.titulo} | Autor: {l.autor} | ISBN: {l.ISBN} | Ejemplares: {l.ejemplar} de {l.total_ejemplares}")
                print("-" * 30)
                return
        print("Libro no encontrado")
        print("-" * 30)

        
        
        ## opcion 5
    def prestarLibro(self, dni, isbn):  
        miembro_encontrado = None
        libro_encontrado = None

        for m in self.miembros:
            if m.DNI == dni:
                miembro_encontrado = m
                break
        
        for l in self.libros:
            if l.ISBN == isbn:
                libro_encontrado = l
                break

        if miembro_encontrado and libro_encontrado:
            if libro_encontrado.estaDisponible():
                libro_encontrado.prestarLibro()
                miembro_encontrado.prestar(libro_encontrado)
                print(f"Prestamo exitoso: {libro_encontrado.titulo} a {miembro_encontrado.nombre}")
                print("-" * 30)
            else:
                print("No hay ejemplares disponibles.")
                print("-" * 30)

        else:
            print("Miembro o Libro no encontrado.")
            print("-" * 30)
                
                
        ## opcion 6
    def devolverLibro(self, dni, isbn):  
        miembro_encontrado = None
        libro_encontrado = None

        for m in self.miembros:
            if m.DNI == dni:
                miembro_encontrado = m
                break
            
        for l in self.libros:
            if l.ISBN == isbn:
                libro_encontrado = l
                break
            
        if miembro_encontrado != None and libro_encontrado != None:
            if libro_encontrado in miembro_encontrado.libros_prestados:
                miembro_encontrado.devolver(isbn)
                libro_encontrado.devolverLibro()
                print(f"El libro '{libro_encontrado.titulo}' fue devuelto por: {miembro_encontrado.nombre}")  
                print("-" * 30)
            else:
                print(f"Error: {miembro_encontrado.nombre} no tiene este libro bajo su préstamo.")
                print("-" * 30)
        else:
            print("Error: No se pudo encontrar el miembro o el libro.")
            print("-" * 30)
                
                
        ## opcion 7
    def estadoLibros(self):  
        for l in self.libros:
            print (f"Titulo: {l.titulo} | ISBN:{l.ISBN} | Disponibles: {l.ejemplar} | Total: {l.total_ejemplares}")
            print("-" * 30)

            
        ## opcion 8
    def estadoMiembros(self):  
        for m in self.miembros:
            print (f"Nombre: {m.nombre} | DNI: {m.DNI}")
            print ("Libros prestados: ")
            
            if len(m.libros_prestados) == 0:
                print("   -Ninguno")
            else:
                for libro in m.libros_prestados:
                    print(f"   - {libro.titulo} (ISBN: {libro.ISBN})")
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
    biblioteca = Biblioteca()
    
    while True:
        print("Sistema de Gestion de Biblioteca")
        print("1. Agregar Libro")
        print("2. Agregar Miembro")
        print("3. Mostrar Miembro")
        print("4. Mostrar Libro")
        print("5. Prestar Libro")
        print("6. Devolver Libro")
        print("7. Consultar Estado Libros")
        print("8. Consultar Estado Miembros")
        print("0. Salir")
        
        opcion = input("Seleccione una opcion: ")
        print("-" * 30)
        if opcion == "1":
            titulo = pedir_texto_obligatorio ("ingrese el titulo del libro: ")
            autor = pedir_texto_obligatorio ("ingrese el autor del libro: ")
            isbn = int(pedir_numero("Ingrese el ISBN del libro: "))
            ejemplares = int(pedir_numero("Ingrese la cantidad de ejemplares: "))
            libro = Libro(titulo,autor,isbn,ejemplares)
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")
            print("-" * 30)
                
        elif opcion == "2":
            nombre = pedir_texto ("ingrese el nombre del miembro: ")
            dni = int(pedir_numero("ingrese el el dni del miembro: "))
            miembro = Miembro(nombre,dni)
            biblioteca.agregar_miembro(miembro)
            print("Miembro agregado exitosamente.")
            print("-" * 30)
                
        elif opcion == "3":
            while True:
                dni_input = input("ingrese el dni del miembro: ")
                try:
                    dni = int(dni_input) 
                    biblioteca.mostrarMiembro(dni)
                    break
                except ValueError:
                    print("-" * 30)
                    print("Error: El DNI proporcionado debe ser un número válido.")
                    print("-" * 30)
                
        elif opcion == "4":
            while True:
                isbn_input = input("ingrese el ISBN del Libro: ")
                try:
                    isbn = int(isbn_input) 
                    biblioteca.mostrarLibro(isbn)
                    break
                except ValueError:
                    print("-" * 30)
                    print("Error: El ISBN proporcionado debe ser un número válido.")
                    print("-" * 30)
                
        elif opcion == "5":
            dni = int(pedir_numero("ingrese el el dni del miembro: "))
            isbn = int(pedir_numero("ingrese el isbn del libro: "))
            biblioteca.prestarLibro(dni,isbn)
                
        elif opcion == "6":
            dni = int(pedir_numero("ingrese el el dni del miembro: "))
            isbn = int(pedir_numero("ingrese el isbn del libro: "))
            biblioteca.devolverLibro(dni,isbn)
                
        elif opcion == "7":
            print("--- Estado del Catálogo ---")
            biblioteca.estadoLibros()
                
        elif opcion == "8":
            print("--- Estado de los Miembros ---")
            biblioteca.estadoMiembros()
                
        elif opcion == "0":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            print("-" * 30)
if __name__ == "__main__":
    main()