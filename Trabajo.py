class Publicacion:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print("Este material fue hecho por: " + self.autor)
        print("Publicado en el año: " + str(self.anio_publicacion) )
        print("Bajo el título '" + self.titulo)

class Libro(Publicacion):
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        super().mostrar_informacion() 
        print("Tiene " + str(self.numero_paginas) + " páginas.")

class Revista(Libro):
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas, numero_edicion):
        super().__init__(titulo, autor, anio_publicacion, numero_paginas)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Es la edición número " + str(self.numero_edicion) + ".")

class Periodico(Revista):
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas, numero_edicion, fecha):
        super().__init__(titulo, autor, anio_publicacion, numero_paginas, numero_edicion)
        self.fecha = fecha

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Y se publicó en la fecha " + str(self.fecha) + ".")

class Foto(Publicacion):
    def ver_foto(self):
        print("ver foto")
    def ver_informacion(self):
        super().mostrar_informacion()

opcion = input("Seleccione una opción 1,2,3 y 4 (Publicacion, Libro, Revista, Periodico): ")
if opcion == "1":
    print("----Publicacion-----")
    titulo = input("Ingrese el título de la publicación: ")
    autor = input("Ingrese el autor de la publicación: ")
    anio_publicacion = int(input("Ingrese el año de publicación: "))
    publicacion = Publicacion(titulo, autor, anio_publicacion)
    print("----Informacion----")
    publicacion.mostrar_informacion()

elif opcion == "2":
    print("----Libro-----")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio_publicacion = int(input("Ingrese el año de publicación: "))
    numero_paginas = int(input("Ingrese el número de páginas: "))
    libro = Libro(titulo, autor, anio_publicacion, numero_paginas)
    print("----Informacion----")
    libro.mostrar_informacion()

elif opcion == "3":
    print("----Revista-----")
    titulo = input("Ingrese el título de la revista: ")
    autor = input("Ingrese el autor de la revista: ")
    anio_publicacion = int(input("Ingrese el año de publicación: "))
    numero_paginas = int(input("Ingrese el número de páginas: "))
    numero_edicion = int(input("Ingrese el número de edición: "))
    revista = Revista(titulo, autor, anio_publicacion, numero_paginas,numero_edicion)
    print("----Informacion----")
    revista.mostrar_informacion()

elif opcion == "4":
    print("----Periodico-----")
    titulo = input("Ingrese el título del periódico: ")
    autor = input("Ingrese el autor del periódico: ")
    anio_publicacion = int(input("Ingrese el año de publicación: "))
    numero_paginas = int(input("Ingrese el número de páginas: "))
    numero_edicion = int(input("Ingrese el número de edición: "))
    fecha = input("Ingrese la fecha de publicación: dd-mm-yyyy ")
    periodico = Periodico(titulo, autor, anio_publicacion, numero_paginas,numero_edicion, fecha)
    print("----Informacion----")
    periodico.mostrar_informacion()

else:
    print("Opción no válida. Por favor, seleccione una de las opciones proporcionadas.")
    mifoto = Foto("familia", "noguera", 2024)
    mifoto.mostrar_informacion()