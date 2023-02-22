ROOT = "root"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, data=None, node=None):
        if node is not None:
            self.root = node
        elif data is not None:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percorrer em ordem
    def inOrder(self, node=None):
        if node is None:
            node = self.root 
        
        if node.left is not None:
            self.inOrder(node.left)

        print(node, end=' ')

        if node.right is not None:
            self.inOrder(node.right)

    # Percorrer em pós ordem
    def pos_ordem(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.pos_ordem(node.left)
        
        if node.right is not None:
            self.pos_ordem(node.right)
                
        print(node, end="")

    # Altura da árvore ou da subárvore
    def height(self, node=None):
        if node is None:
            node = self.root

        h_left = 0
        h_right = 0
        if node.left is not None:
            h_left = self.height(node.left)
        
        if node.right is not None:
            h_right = self.height(node.right)
                
        if h_left > h_right:
            return h_left + 1
        else:
            return h_right + 1 

    # Percorrer em nível
    ROOT = "root"
    def levelOrder(self, node=ROOT):
        if node == ROOT:
            node = self.root

        fila = Queue()
        fila.push(node)
        while len(fila):
            node = fila.pop()
            if node.left is not None:
                fila.push(node.left)
            if node.right is not None:
                fila.push(node.right)
            print(node, end=' ')

    # Inserir elemento
    def insert(self, value):
        pai = None
        aux = self.root

        while(aux is not None):
            pai = aux
            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right

        if pai is None:
            self.root = Node(value)
        elif value < pai.data:
            pai.left = Node(value)
        else:
            pai.right = Node(value)

    # Buscar elemento
    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return Tree(node)
        if value < node.data:
            return self._find(value, node.left)
        
        return self._find(value, node.right)
    
    # Valor Mínimo
    ROOT = "root"
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
            
        while(node.left is not None): 
            node = node.left
        
        return node.data
    
    # Valor Máximo
    ROOT = "root"
    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        
        while(node.right is not None):
            node = node.right
        
        return node.data
    
    # Nó Sucessor
    def sucessor(self, chave):
        valores = self.valores(self.root)

        if chave in valores:
            posicao = valores.index(chave)
            
        if 0 <= posicao < len(valores) - 1:
            return valores[posicao + 1]

        return None

    # Nó antecessor
    def valores(self, node):
        if node is not None:
            lista = []

        if node.left is not None:
            esquerda = self.valores(node.left)
            lista = lista + esquerda

        lista = lista + [node.data]

        if node.right is not None:
            direita = self.valores(node.right)
            lista = lista + direita

        return lista
    