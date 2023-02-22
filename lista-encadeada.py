class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False


    def get(self, index):
        pointer = self.head
        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                return 'IndexError: list index out of range'

        if pointer is not None:
            return pointer.data
        else:
            return 'IndexError: list index out of range'


    def set(self, index, elemento):
        pointer = self.head
        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                return 'IndexError: list index out of range'

            if pointer is not None:
                pointer.data = elemento
            else: 
                return 'IndexError: list index out of range'

    # acidiona o valor no inicio da lista
    def add(self, elemento):
        node = Node(elemento)
        node.next = self.head
        self.head = node


    def append(self, elemento):
        if self.head is not None:
            pointer = self.head

            while (pointer.next is not None): 
                pointer = pointer.next

            pointer.next = Node(elemento)
        else: 
            self.head = Node(elemento) 
        self.size += 1 


    def insert(self, index, elemento):
        node = Node(elemento)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(index-1):
                if pointer is not None:                
                    pointer = pointer.next
                else: 
                    return 'IndexError: list index out of range'

            node.next = pointer.next
            pointer.next = node
        self.size += 1


    def tamanho(self):
        return self.size

        
    def remove(self, elemento):
        if self.head is None:
            return f'ValueError: {elemento} is not in list'
        elif self.head.data == elemento:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next 
            while(pointer is not None):
                if pointer.data == elemento:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.size -= 1
                ancestor = pointer
                pointer = pointer.next
            return True        
        return f'ValueError: {elemento} is not in list'

    
    def pop(self):
        if self.head is None:
            return None
    
        result = self.head.data   
        self.head = self.head.next
   
        return self.head

    # retorna o indice do elemento na lista
    def index(self, elemento):
        pointer = self.head
        indice = 0
        found = False
        while pointer != None and not found:
            if pointer.data == elemento:
                found = True
            else:
                pointer = pointer.next
            
                indice += 1
        return indice


    def search(self, elemento):
        pointer = self.head
        found = False
        while pointer != None and not found:
            if pointer.data == elemento:
                found = True
            else:
                pointer = pointer.next
        return found

    def printLista(self):
        pointer = self.head
        lista = []
        while pointer is not None:
            lista += [pointer.data]
            pointer = pointer.next
        return print(lista)



import random
random.seed(77)
def lista_aleatoria():
    values = random.sample(range(1, 100), 5)
    lst = LinkedList()
    for v in values:
        lst.append(v)
    return lst

lista = lista_aleatoria()

lista.printLista()
lista.insert(4, 22)
lista.printLista()


lista.pop()

lista.printLista()

print(lista.index(31))
lista.search(88)

