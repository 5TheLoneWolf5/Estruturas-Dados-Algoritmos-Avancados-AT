"""

Respostas:

Arrays armazenam coleções de elementos do mesmo tipo, ordenados e os mesmos são guardados em um espaço contínuo de memória, o que as deixa mais eficientes ao manipular grandes quantidades de dados comparado a listas ordenadas e não ordenadas.

Dada a natureza baseada em prioridade de uma estrutura Heap, ela otimiza o processamento de pacotes em um roteador ao eficientemente implementar filas de prioridade, o que permite os roteadores identificarem rapidamente os pacotes baseado na prioridade.

"""

import numpy as np

element_dtype = np.dtype([('id', np.int32), ('prioridade', np.int32), ('tempo', np.int32)])

class MinHeap:
    def __init__(self):
        self.heap = np.empty(0, dtype=element_dtype) # Criando array com numpy.
    
    def insert(self, item):
        new_item = np.array(item, dtype=element_dtype)
        self.heap = np.append(self.heap, new_item)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            item = self.heap[0]
            self.heap = np.empty(0, dtype=element_dtype)
            return item
    
        root = self.heap[0].copy()
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self._heapify_down(0)
        return root

    def modify_priority(self, idItem, newPriority):
        indices = np.where(self.heap['id'] == idItem)[0]
        
        if len(indices) != 1:
            print("Nenhum valor encontrado (OU múltiplos itens com o mesmo ID).")
            return
        
        index = indices[0]
        self.heap[index]['prioridade'] = newPriority

        self._heapify_up(index)
        self._heapify_down(index)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index]['prioridade'] < self.heap[parent_index]['prioridade']:
            self.heap[[index, parent_index]] = self.heap[[parent_index, index]]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child]['prioridade'] < self.heap[smallest]['prioridade']:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]['prioridade'] < self.heap[smallest]['prioridade']:
            smallest = right_child

        if smallest != index:
            self.heap[[index, smallest]] = self.heap[[smallest, index]]
            self._heapify_down(smallest)

pacotes = [(1, 5, 342), (2, 4, 376), (3, 3, 887), (4, 2, 1765)]

heap = MinHeap()
for p in pacotes:
    heap.insert(p)

heap.modify_priority(1, 1)

print("- Pacotes:")
while len(heap.heap) > 0:
    item = heap.pop()
    print(f"\tID: {item['id']} - Prioridade: {item['prioridade']} - Tempo: {item['tempo']}")