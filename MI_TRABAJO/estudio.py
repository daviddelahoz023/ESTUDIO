class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
    #def __str__(self):
     #   return str(self.dato)
    #def __eq__ (self,other):
     #   if not isinstance(other,nodo):
      #      return False 
       # return self.dato == other.dato

minombre = nodo("David")
minombre1 = "Andres"
if not isinstance (minombre1,nodo):
    print("Mi perro no es")
if  isinstance(minombre,nodo):
    print("es mi perro")