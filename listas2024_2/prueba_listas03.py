from listas_enlazadas import ListaDoble
lista_02 = ListaDoble()
#Adicionar al Inicio
lista_02.adicionarAlInicio(10)
lista_02.adicionarAlInicio(20)
lista_02.adicionarAlInicio(30)
lista_02.adicionarAlInicio(40)
lista_02.adicionarAlInicio(50)
lista_02.adicionarAlInicio(60)
print("Lista 02:", lista_02)
#Eliminar información
print("Eliminar 01:",lista_02.eliminarInfo(100))
print("Lista 02:", lista_02)
print("Eliminar 02:",lista_02.eliminarInfo(30))
print("Lista 02:", lista_02)
print("Eliminar 03:",lista_02.eliminarInfo(60))
print("Lista 02:", lista_02)
print("Eliminar 04:",lista_02.eliminarInfo(40))
print("Lista 02:", lista_02)