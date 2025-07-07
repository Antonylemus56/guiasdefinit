class ArbolBinario:
    def izquierda(self,p):
        raise NotImplementedError('debe ser implementado por la subclase')
    
    def derecha(self,p):
        raise NotImplementedError('debe ser implementado por la subclase')
    
    def hermano(self, p):
        padre = self.padre(p)
        if padre is None:
            return None
        else:
            if p == self.izquierda(padre):
                return self.derecha(padre)
            else:
                return self.izquierda(padre)
            
    def hijos(self,p):
        if self.izquierda(p) is not None:
            yield self.izquierda(p)
        if self.derecha(p) is not   None:
            yield self.derecha(p)


class Arbol_Binario_Enlazado(ArbolBinario):
    class _Nodo:
        __slots__ = '_elemento', '_padre', '_izquierda', '_derecha'

        def __init__(self,elemento, padre = None, izquierda = None, derecha = None):
            self._elemento = elemento
            self._padre = padre
            self._izquierda = izquierda
            self._derecha = derecha

    class Posicion:
        def __init__(self, contenedor, nodo):
            self._contenedor = contenedor
            self._nodo = nodo

        def elemento(self):
            return self._nodo._elemeto
        
        def __eq__(self, otro):
            return type(otro) is type(self) and otro._nodo is self._nodo
        
    def __init__(self):
        self._raiz = None
        self._tamano = 0

    def __len__(self):
        return self._tamano
    
    def _hacer_posicion(self,nodo):
        return self.Posicion(self, nodo) if nodo is not None else None
    
    def _validar(self, p):
        if not isinstance(p, self.Posicion):
            raise TypeError('p debe ser funcion de tipo propia')
        if p._contenedor is not self:
            raise ValueError('p no pertenece al contenedor ')
        if p._nodo._padre is p._nodo:
            raise ValueError('P no es valido')
        return p._nodo
    
    def raiz(self):
        return self._hacer_posicion(self._raiz)
    
    def padre(self,p):
        nodo = self._validar(p)
        return self._hacer_posicion(nodo._padre)
    
    def izquierda(self, p):
        nodo = self._validar(p)
        return self._hacer_posicion(nodo._izquierda)

    def derecha(self, p):
        nodo = self._validar(p)
        return self._hacer_posicion(nodo._derecha)
    
    def numero_d_hijos(self,p):
        nodo = self._validar(p)
        contador = 0
        if nodo._izquieda is not None:
            contador += 1
        if nodo._derecja is not None:
            contador += 1
        return contador
    
    def _agg_raiz(self, e):
        if self._raiz is not None:
            raise ValueError('La raiz ya existe')
        self._tamano = 1
        self._raiz = self._Nodo(e)
        return self._hacer_posicion(self._raiz)
    
    def _agg_izquierda(self,p, e):
        nodo = self._validar(p)
        if nodo._izquierda is not None:
            raise ValueError('hijo izquierdo ya existe')
        self._tamano += 1
        nodo._izquierda = self._Nodo(e, nodo)
        return self._hacer_posicion(nodo._izquierda)
    
    def _agg_derecha(self,p, e):
        nodo = self._validar(p)
        if nodo._derecha is not None:
            raise ValueError('hijo derecho ya existe')
        self._tamano += 1
        nodo._derecha = self._Nodo(e, nodo)
        return self._hacer_posicion(nodo._derecha)
    
    def _remplazar(self,p,e):
        nodo = self._validar(p)
        if self.numero_d_hijos(p) == 2:
            raise ValueError('La posicion ya tiene dos hijos')
        hijo = nodo._izquierda if nodo._izquierda else nodo._derecha
        if hijo is not None:
            hijo._padre = nodo._padre
        if nodo is self._raiz:
            self._raiz = hijo
        else:
            padre = nodo._padre
            if nodo is padre._izquierda:
                padre._izquierda =  hijo
            else:
                padre._derecha = hijo
            
        self._tamano -= 1
        nodo._padre = nodo
        return nodo._elemento
    
    def _adjuntar(self, p, t1, t2):
            nodo = self._validar(p)
            if self.numero_d_hijos(p) != 0:
                raise ValueError('La posicion debe ser una hoja')
            if not type(self) is type(t1) is type(t2):
                raise TypeError('El tipo de arbol debe coincidir')
            self._tamano+= len(t1) + len(t2)
            if not t1._raiz is None:
                t1._raiz._parent = nodo
                nodo._izquierda = t1._raiz
                t1._raiz = None
                t1._tamano = 0
            if not t2._raiz is None:
                t2._raiz._parent = nodo
                nodo._right = t2._raiz
                t2._raiz = None
                t2._tamano = 0

