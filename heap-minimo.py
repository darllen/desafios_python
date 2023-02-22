lass MinHeap:
    def __init__(self):
        self.heap = [0] 
        self.size = 0
 
    def sift_down(self, indice):
        while (indice * 2) <= self.size:
            mc = self.min_child(indice)
            if self.heap[indice] > self.heap[mc]:
                self.heap[indice], self.heap[mc] = self.heap[mc], self.heap[indice]
            indice = mc

    def sift_up(self, indice):
        Stop = False
        while (indice // 2 > 0) and Stop == False:
            if self.heap[indice] < self.heap[indice // 2]:
                self.heap[indice], self.heap[indice // 2] = self.heap[indice // 2], self.heap[indice]
            else:
                Stop = True
            indice = indice // 2

    def insert(self, valor):
        self.heap.append(valor)

        self.size += 1

        self.sift_up(self.size)

    def min_child(self, indice):
        if (indice * 2) + 1 > self.size:
            return indice * 2
        else:
            if self.heap[indice * 2] < self.heap[(indice * 2) + 1]:
                indice_min_child = indice * 2 
            else:
                indice_min_child = (indice * 2) + 1
        
        return indice_min_child
 
    def delete_min(self):
        if len(self.heap) == 1:
            return 'Empty heap'
 
        root = self.heap[1]
 
        self.heap[1] = self.heap[self.size]
 
        *self.heap, _ = self.heap
 
        self.size -= 1
 
        self.sift_down(1)
 
        return root

    
