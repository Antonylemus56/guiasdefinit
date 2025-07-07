
"""
1) Suponga que una pila S inicialmente vacía ha ejecutado (en cualquier orden) un total de 25
operaciones push, 12 operaciones top, y 10 operaciones pop, 3 de las cuales lanzaron
excepciones de tipo Empty que fueron capturadas e ignoradas ¿Cuál es el tamaño actual de S?

R: La pila tiene 18 elementos porque se hicieron 25 push y solo 7 pop efectivos (3 fallaron).
Las operaciones top no afectan el tamaño.
"""

"""
2) Proporcione un implementación recursiva de un método que remueva todos los elementos de un
pila.
pila = [1,2,3,3,4,4,5,6,6,22,1]
def vaciar_pila(pila):
   for i in pila:
    pila.pop()        
    vaciar_pila(pila) 
    return pila
print(vaciar_pila(pila))

"""

"""
3) Suponga que tiene una Cola Doblemente Terminada D, que contiene los números (1, 2, 3, 4, 5,
6, 7, 8) en este orden. Suponga además que usted tiene una Cola Q, inicialmente vacía. Escriba
un fragmento de código que use las solamente variables D y Q y haga que los elementos en D
estén almacenados en el orden (1, 2, 3, 5, 4, 6, 7, 8) (observe el cambio entre 5 y 4).



from collections import deque

X = [1, 2, 3, 4, 5, 6, 7, 8]
D = deque(X)
Q = deque()

# Guardamos el tamaño original antes de modificar D
n = len(D)
i = 0

while i < n:
    valor = D.popleft()

    if i == 3:
        temp = valor              # valor = 4
        siguiente = D.popleft()   # valor = 5
        Q.append(siguiente)       # primero 5
        Q.append(temp)            # luego 4
        i += 2                    # ya procesamos dos valores
    else:
        Q.append(valor)
        i += 1

# Resultado final
D = Q
print(D)  # deque([1, 2, 3, 5, 4, 6, 7, 8])

"""
"""


4) Explique cuál es el error en el método añadir del siguiente ArregloDinamico (estudie el método
original y luego intente hacerlo sin compararlo en éste):
def añadir(self, obj):
    if self._n == self._capacidad:
        self._A = self._redimensionar(2 * self._capacidad)
    self._A[self._n] = obj
    self._n += 1


def redimensionar(self, c):
    B = self._reservar_memoria(c)
    for k in range(self._n):
        B[k] = self._A[k]
    self._A = B
    self._capacidad = c

"""



"""
5) Suponga que usted tiene tres pilas no vacías R, S y T. Describa una secuencia de operaciones
que ocasione que S almacene todos los elementos que originalmente estaban en T debajo de
todos los elementos que S ya contenía, manteniendo el orden original que tenían dichos grupos
de elementos en S y T. La pila R puede usarse pero debe quedar con los mismos valores y orden
originales. Por ejemplo, si R = [1, 2, 3], S = [4, 5], y T = [6, 7, 8, 9], entonces después de las
operaciones deberían de quedar así: R = [1, 2, 3], T = [] y S = [6, 7, 8, 9, 4, 5] (observe que
consideramos que el tope de la pila es el elemento más a la derecha de la misma).




# Ejemplo inicial
R = [1, 2, 3]  # No debe cambiar
S = [4, 5]
T = [6, 7, 8, 9]

# Paso 1: Mover de T a R (esto invierte T temporalmente)
aux_R = []  # Usamos aux_R para guardar lo que se movió a R, para restaurar luego
while T:
    value = T.pop()
    R.append(value)  # Se altera R temporalmente
    aux_R.append(value)  # Para restaurar

# Paso 2: Mover de R (los nuevos elementos) a S
for i in range(len(aux_R)):
    value = R.pop()
    S.insert(0, value)  # Insertar al fondo de S (al inicio de la lista)

# Paso 3: Restaurar R a su estado original
while aux_R:
    value = aux_R.pop()
    if len(R) < 0:
     R.pop()  # Eliminar el valor agregado

# Resultado
print("R:", R)  # Debe ser [1, 2, 3]
print("S:", S)  # Debe ser [6, 7, 8, 9, 4, 5]
print("T:", T)  # Debe ser []

"""


"""
6) Describa cómo sería posible implementar el TDA Cola usando dos Pilas para almacenar sus
datos (los datos de las pilas sólo pueden ser accedidos mediante las operaciones push, top y
pop).
class ColaConPilas:
    def __init__(self):
        self.entrada = []  # Pila para insertar elementos (push)
        self.salida = []   # Pila para eliminar elementos (pop)

    def encolar(self, elemento):
        # Siempre se hace push en la pila de entrada
        self.entrada.append(elemento)

    def desencolar(self):
        if not self.salida:
            # Si la pila de salida está vacía, vaciamos la pila de entrada en ella
            while self.entrada:
                self.salida.append(self.entrada.pop())
        if not self.salida:
            raise IndexError("Cola vacía")
        return self.salida.pop()

    def frente(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())
        if not self.salida:
            raise IndexError("Cola vacía")
        return self.salida[-1]  # Equivale a top()

    def esta_vacia(self):
        return not self.entrada and not self.salida

# Ejemplo de uso
cola = ColaConPilas()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.desencolar())  # Sale 1
print(cola.frente())      # Muestra 2 (el nuevo frente)
print(cola.desencolar())  # Sale 2

"""

"""
7) Determine cuál es el error en el siguiente método para eliminar el último nodo de una Lista
Individualmente Enlazada:
def delete_last(self):
    self.tail.next = None
    self.tail = None

def delete_last(self)
    self.tail.prev = tail
    self.tail.next = none

"""


"""
8) Las Pilas son comúnmente usadas para proveer la función “undo” en muchos programas, y
dependiendo de la complejidad del programa, buena parte de éstos define un tamaño máximo
para el “undo history” (cantidad de elementos en la Pila). Si definimos una Pila con tamaño
máximo básica lo que ocurrirá es que al llegar a su capacidad máxima, se lanzará una excepción
si se solicita añadir un elemento más. Pero es más común que lo que ocurra es que se acepte
este nuevo elemento y se elimine de forma silenciosa el elemento más antiguo en el fondo de la
Pila para hacerle espacio al nuevo. Utilizando un arreglo circular escriba el código necesario para
implementar un Pila que se comporte de esta manera.



"""



    
    
    
   

"""
9. Escriba un algoritmo que permita encontrar el penúltimo nodo de una Lista Individualmente
Enlazada.


"""




 
 