class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas

   
    def __init__(self, dato):
        self.raiz = Nodo(dato)
        self._size = 0
    
   

  
        
    def _agregar_izq(self, p, e):
        
        self._size += 1
        Nodo._left = self.Node(e, Nodo)
        return self._make_position(Nodo._left)
    
    def _agregar_der(self, p, e):
        node = self._validate(p)
        if node.derecha is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node.derecha = self._Node(e, node)
        return self._make_position(node.derecha)
        
        
      

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        

    def agregar(self, dato):
            self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


arbol = Arbol(input("Ingrese raiz: "))


pregunta = input("Donde desea agreagar hijo?")

if pregunta == "si":
        lado = input("Ingrese lado del hijo?")
        if lado == "i":
            Arbol._agregar_izq(input("Ingrese hijo izquierdo: "))
        elif lado == 'd':
            Arbol._agregar_izq(input("Ingrese hijo Derrecho : "))
        else:
            print("EEROR: COMANDO DESCONOCIDO")
else:
        print('xd')



arbol.preorden()
