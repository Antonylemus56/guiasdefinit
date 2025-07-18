class BinaryTree:
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)


    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if self.num_children(p) != 0:
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1._root is None:
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2._root is None:
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0



"""


# Crear el árbol de la imagen y recorrerlo en posorden

def build_example_tree():
    tree = LinkedBinaryTree()
    raiz = tree._add_root(2)
    p1 = tree._add_left(raiz, 7)
    p2 = tree._add_right(raiz, 5)
    p2_1 = tree._add_left(p1, 2)
    p2_2 = tree._add_right(p1, 6)
    tree._add_left(p2_2, 5)
    tree._add_right(p2_2, 11)
    p2_3 = tree._add_right(p2, 9)
    tree._add_left(p2_3, 4)
    return tree

"""


"""

def postorder(tree, p, result):
    for c in tree.children(p):
        postorder(tree, c, result)
    result.append(p.element())



"""





if __name__ == "__main__":
    
    t1 = LinkedBinaryTree() 
    t2 = LinkedBinaryTree() 
    t3 = LinkedBinaryTree() 
    t1._add_root('x') 
    t2._add_root('y') 
    t3._add_root('z') 
    t2._add_left(t2.root(), 'y-l') 
    t3._add_left(t3.root(), 'z-l') 
    t3._add_right(t3.root(), 'z-r') 
    t1._attach(t1.root(), t2,t3) 
    t1._delete(t1.left(t1.root())) 
    print(t1.left(t1.right(t1.root())).element())

