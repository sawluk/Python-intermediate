#David Noguera Y Samuel Bolaños

class Libro:
    def __init__(self, titulo, codigo, autor, año_publicacion, disponibilidad):
        self.libro = {
            "titulo": titulo,
            "codigo": codigo,
            "autor": autor,
            "año_publicacion": año_publicacion,
            "disponibilidad": disponibilidad,  
        }
    
    def estadoDis(self):
        print(f"Este libro está: {self.libro['disponibilidad']}")

class Biblioteca:
    def __init__(self):
        self.librosL = []
    
    def agregar_libro(self):
            print("--------- AGREGANDO UN LIBRO ----------")
            titulo = input("Ingrese el titulo del libro: ")
            codigo = input("Ingrese el codigo del libro: ")
            for libro in self.librosL:
                    if libro.libro["codigo"] == codigo:
                        print(f"El codigo {codigo} ya esta registrado para el libro '{libro.libro['titulo']}'.")
                        return  
            autor = input("Ingrese el autor del libro: ")
            año_publicacion = input("Ingrese el año de publicacion: ")
            disponibilidad = "Disponible"
            nuevo_libro = Libro(titulo, codigo, autor, año_publicacion, disponibilidad)
            self.librosL.append(nuevo_libro)
            print(f"El libro {titulo} se ha añadido a la lista.")
   
    
    def listar_libros(self):
        if not self.librosL:  
            print("No hay libros disponibles por el momento")
        else:
            print("--------- LIBROS DISPONIBLES ----------")
            for libro in self.librosL:
                print(f"Titulo: {libro.libro['titulo']}, Su estado es: {libro.libro['disponibilidad']} y su codigo es {libro.libro['codigo']}")


    def prestar_libro(self):
        print("--------- PRESTANDO UN LIBRO ----------")
        codigo = input("Ingrese el codigo del libro que desea prestar: ")
        for libro in self.librosL:
            if libro.libro['codigo'] == codigo:
                if libro.libro['disponibilidad'] == "Disponible":
                    libro.libro['disponibilidad'] = "Prestado"
                    print(f"El libro {libro.libro['titulo']} se ha prestado con exito")
                elif libro.libro['disponibilidad'] != "Disponible":
                    print(f"Lo siento, el libro {libro.libro['titulo']} no esta disponible, espere su devolucion")
    
    def devolver_libro(self):
        print("--------- DEVOLVIENDO UN LIBRO ----------")
        codigo = input("Ingrese el codigo del libro que desea devolver: ")
        for libro in self.librosL:
            if libro.libro['codigo'] == codigo:
                if libro.libro['disponibilidad'] == "Prestado":
                    libro.libro['disponibilidad'] = "Disponible"
                    print(f"El libro {libro.libro['titulo']} se ha regresado con exito")
                elif libro.libro['disponibilidad'] != "Prestado":
                    print(f"El libro {libro.libro['titulo']} puede que ya haya sido regresado o a ocurrido un error")

    def buscar_libro(self):
        print("--------- BUSQUEDA DE LIBRO ----------")
        consulta = input("Ingrese el codigo O nombre del libro que busca: ")
        for libro in self.librosL:
            if libro.libro['titulo'] == consulta or libro.libro['codigo'] == consulta:
                print(f"El libro encontrado es el siguiente: ") 
                print(f"Titulo: {libro.libro['titulo']}")
                print(f"Codigo: {libro.libro['codigo']}")
                print(f"Autor: {libro.libro['autor']}")
                print(f"Año de Publicacion: {libro.libro['año_publicacion']}")
                print(f"Disponibilidad: {libro.libro['disponibilidad']}")
                print("No es lo que esperabas? prueba ver los libros disponibles de forma general")
            else:
                print("Lo siento, no se encontro el libro que buscas")
                print("No es lo que esperabas? prueba ver los libros disponibles de forma general")

    def menu(self):
        print("--------- MENU ----------")
        opcion = input("Por favor, digite una opción \n 1) Agregar un libro \n 2) Ver lista de libros \n 3) Préstamo de libro \n 4) Devolución de libro \n 5) Búsqueda de libro \n 0) Cierre del menú \n Opción: ")   
        while opcion != "0":  
            if opcion == "1":
                self.agregar_libro()
                print("")
            elif opcion == "2":
                self.listar_libros()
                print("")
            elif opcion == "3":
                self.prestar_libro()
                print("")
            elif opcion == "4":
                self.devolver_libro()
                print("")
            elif opcion == "5":
                self.buscar_libro()
                print("")
            else:
                print("Opción inválida, por favor vuelva a intentarlo")
            
            opcion = input("Por favor, digite una opción válida \n 1) Agregar un libro \n 2) Ver lista de libros \n 3) Préstamo de libro \n 4) Devolución de libro \n 5) Búsqueda de libro \n 0) Cierre del menú \n Opción: ")
        
        print("Fin del programa gracias")


                  
biblioteca = Biblioteca()
biblioteca.menu()



    