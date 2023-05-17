#Cree una clase Libro que modele la informacion que se mantiene en una biblioteca 
#sobre cada libro: IdLibro (unico para cada libro), 
#titulo, autor, ISBN, paginas, edicion, editorial, lugar (ciudad y pais) 
#y si esta disponible. 
#La clase debe tener: propiedades, constructores. 
class Libro(object):
    iva=0.13
    def __init__(self,id_Libro,Titulo,Autor,ISBN,Paginas,Edicion,Editorial,Pais,Disponible,Precio):
        self.id_Libro=id_Libro
        self.Titulo=Titulo
        self.Autor=Autor
        self.ISBN=ISBN
        self.Paginas=Paginas
        self.Edicion=Edicion
        self.Editorial=Editorial
        self.Pais=Pais
        self.Disponible=Disponible
        self.Precio=Precio
        
    def precio_mas_iva(self):
        if self.Precio:
            precio = float(self.Precio)
            return precio + (precio * Libro.iva)
        else:
            return 0.0


  