class Document:
    def __init__(self, id: int, contenido: dict = None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}
        
    def obtener_valor(self, clave: str) -> str:
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave: str, valor: str) -> None:
        self.contenido[clave] = valor
        
    def __str__(self) -> str:
        return f'Documento | ID {self.id}\n{self.contenido}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "contenido": self.contenido
        }
    
class Collection:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.documentos = {}
    
    def añadir_documento(self, documento: Document) -> None:
        if (type(documento) != Document):
            raise TypeError('No se ha ingresado un documento valido')
        self.documentos[documento.id] = documento
        
    def eliminar_documento(self, id_documento: int) -> None:
        if id_documento in self.documentos:
            del self.documentos[id_documento]
            
    def buscar_documento(self, id_documento: int) -> Document | None:
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return f'Coleccion {self.nombre} | {len(self.documentos)} Documento/s registrados'
    
class DBDocument:
    def __init__(self):
        self.colecciones = {}
        
    def crear_coleccion(self, nombre_coleccion: str) -> None:
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
            
    def eliminar_coleccion(self, nombre_coleccion: str) -> None:
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def obtener_coleccion(self, nombre_coleccion: str) -> Collection | None:
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f'BDDocument {self.nombre} | {len(self.documentos)} Coleccion/es registrados'