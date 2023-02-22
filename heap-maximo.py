class MaxHeap:
    def __init__(self):
        self.heap = [0] 
        self.size = 0
 
    def sift_up(self, indice):
        Stop = False
        while (indice // 2 > 0) and Stop == False:
            if self.heap[indice] > self.heap[indice // 2]:
                self.heap[indice], self.heap[indice // 2] = self.heap[indice // 2], self.heap[indice]
            else:
                Stop = True
            indice = indice // 2

    def insert(self, valor):
        self.heap.append(valor)
        self.size += 1
        self.sift_up(self.size)

    def sift_down(self, indice):
        while (indice * 2) <= self.size:
            mc = self.max_child(indice)
            if self.heap[indice] < self.heap[mc]:
                self.heap[indice], self.heap[mc] = self.heap[mc], self.heap[indice]
            indice = mc

    def max_child(self, indice):
        if (indice * 2) + 1 > self.size:
            return indice * 2
        else:
            if self.heap[indice * 2] > self.heap[(indice * 2) + 1]:
                indice_max_child = indice * 2 
            else:
                indice_max_child = (indice * 2) + 1
        
        return indice_max_child
 
    def delete_max(self):
        if len(self.heap) == 1:
            return 'Empty heap'

        root = self.heap[1]

        self.heap[1] = self.heap[self.size]
 
        *self.heap, _ = self.heap
 
        self.size -= 1
 
        self.sift_down(1)

        return root
    
    def crias(self, element):
        if element in self.heap:
            if self.heap.index(element) * 2 <= self.size:
                left = self.heap[self.heap.index(element) * 2]
            else:
                left = None
            
            if (self.heap.index(element) * 2) + 1 <= self.size:
                right = self.heap[(self.heap.index(element) * 2) + 1]
            else:
                right = None

            filhos = [left, right]

            return filhos
        else: 
            return 'Elemento tá aqui não'
            
    
heap = MaxHeap()

heap.insert(5)
heap.insert(6)
heap.insert(7)

print(heap.heap)
heap.delete_max()
print(heap.heap)
print(heap.heap[1])
print(heap.crias(10))
