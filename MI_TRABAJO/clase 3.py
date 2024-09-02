#clase nodo
class Nodo:
     #constructor
     def __init__ (self,dato):
         self.dato = dato
         self.siguiente = None
         
     def __str__(self) -> str:
          return str(self.dato)
class Lista:
    def __init__(self) -> None:
         self.inicial = None
    def adicionarInicio(self,dato):
        #lista vacia
        if self.inicial == None:
            self.inicial = Nodo(dato)
        else:
            nodo_nuevo = Nodo(dato)
            nodo_nuevo.siguiente = self.inicial
            self.inicial = nodo_nuevo             
    def __str__(self) -> str:
        recorrido = ""
        nodo_actual = self.inicial
        while nodo_actual != None :
            recorrido += str(nodo_actual)+ "  "
            nodo_actual = nodo_actual.siguiente
        return recorrido
    def adicionarFinal(self,dato):
        #lista vacia
        if self.inicial == None:
            self.inicial = Nodo(dato)
        else:
            nodo_actual = self.inicial
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = None(dato)
    def eliminarInicio(self):
        #Lista vacia
        if self.inicial == None:
            return "No hay datos"
        else:
            #lista con datos
            dato = self.inicial.dato
            self.inicial = self.inicial.siguiente
            return dato
    def eliminarInfo(self,dato):
        #Lista vacia
        if self.inicial == None:
            return "No hay datos"
        
        #primero de la lista
        if self.inicial.dato == dato:
            self.eliminarInicio()
            return True
        
        #buscar el valor a eliminar
        nodo_actual = self.inicial
        nodo_previo = None  
        while nodo_actual != None and nodo_actual.dato != dato :
            nodo_previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
        #Caso 1: Dato no encontrado
        if nodo_actual == None :
            return "No se encontro el dato"
        #Caso 2 : Dato encontrado
        nodo_previo.siguiente = nodo_actual.siguiente
        return "Dato encontrado" 
    #+def eliminarFinal(self):