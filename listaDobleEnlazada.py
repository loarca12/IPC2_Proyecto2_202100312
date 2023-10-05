from nodo import *

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
        self.size += 1

    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        self.size += 1

    def eliminar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior

                return
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        x = ""
        while actual:
            if actual.siguiente is not None:
                x+= actual.dato.dron + "\n"
            else:
                x += actual.dato.dron
            actual = actual.siguiente
        return x
    
    def ordenamiento_seleccion(self):
        if self.inicio is None:
            return

        actual = self.inicio
        while actual:
            min_nodo = actual
            siguiente_nodo = actual.siguiente
            while siguiente_nodo:
                if siguiente_nodo.dato.dron < min_nodo.dato.dron:
                    min_nodo = siguiente_nodo
                siguiente_nodo = siguiente_nodo.siguiente

            if min_nodo != actual:
                # Intercambiar datos entre actual y min_nodo
                actual.dato.dron, min_nodo.dato.dron = min_nodo.dato.dron, actual.dato.dron

            actual = actual.siguiente
