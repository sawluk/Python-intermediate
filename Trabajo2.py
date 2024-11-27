class Publicacion:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print("Este material fue hecho por: " + self.autor)
        print("Publicado en el año: " + str(self.anio_publicacion))
        print("Bajo el título '" + self.titulo + "'")


class Libro(Publicacion):
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tiene", self.numero_paginas, " páginas.")


class Revista(Libro):
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas, numero_edicion):
        super().__init__(titulo, autor, anio_publicacion, numero_paginas)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Es la edición número " + str(self.numero_edicion) + ".")


class Periodico(Revista):
    def __init__(
        self, titulo, autor, anio_publicacion, numero_paginas, numero_edicion, fecha
    ):
        super().__init__(
            titulo, autor, anio_publicacion, numero_paginas, numero_edicion
        )
        self.fecha = fecha

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(
            f"Y se publicó en la fecha {self.fecha}, dando como resultado {self.numero_paginas}"
        )


class Articulo(Revista):  # nueva clase articulo
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas, numero_edicion):
        super().__init__(
            titulo, autor, anio_publicacion, numero_paginas, numero_edicion
        )

    def mostrar_informacion(self):
        super().mostrar_informacion()


def pedir_datos_comunes():
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    anio_publicacion = int(input("Ingrese el año de publicación: "))
    return titulo, autor, anio_publicacion


opcion = input(
    "Seleccione una opción 1,2,3, 4 y 5 (Publicacion, Libro, Revista, Periodico, Articulo): "
)

if opcion == "1":
    print("----Publicacion-----")
    titulo, autor, anio_publicacion = pedir_datos_comunes()
    publicacion = Publicacion(titulo, autor, anio_publicacion)
    publicacion.mostrar_informacion()

elif opcion == "2":
    print("----Libro-----")
    titulo, autor, anio_publicacion = pedir_datos_comunes()
    numero_paginas = int(input("Ingrese el número de páginas: "))
    libro = Libro(titulo, autor, anio_publicacion, numero_paginas)
    libro.mostrar_informacion()

elif opcion == "3":
    print("----Revista-----")
    titulo, autor, anio_publicacion = pedir_datos_comunes()
    numero_paginas = int(input("Ingrese el número de páginas: "))
    numero_edicion = int(input("Ingrese el número de edición: "))
    revista = Revista(titulo, autor, anio_publicacion, numero_paginas, numero_edicion)
    revista.mostrar_informacion()

elif opcion == "4":
    print("----Periodico-----")
    titulo, autor, anio_publicacion = pedir_datos_comunes()
    numero_paginas = int(input("Ingrese el número de páginas: "))
    numero_edicion = int(input("Ingrese el número de edición: "))
    fecha = input("Ingrese la fecha de publicación: dd-mm-yyyy ")
    periodico = Periodico(
        titulo, autor, anio_publicacion, numero_paginas, numero_edicion, fecha
    )
    periodico.mostrar_informacion()

elif opcion == "5":
    print("----Articulo-----")
    titulo, autor, anio_publicacion = pedir_datos_comunes()
    numero_paginas = int(input("Ingrese el número de páginas: "))
    numero_edicion = int(input("Ingrese el número de edición: "))
    articulo = Articulo(titulo, autor, anio_publicacion, numero_paginas, numero_edicion)
    articulo.mostrar_informacion()
else:
    print("Opción no válida. Por favor, seleccione una de las opciones proporcionadas.")
