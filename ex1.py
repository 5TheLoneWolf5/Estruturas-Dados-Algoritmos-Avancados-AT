"""

Respostas:

Uma estrutura de dados Heap pode ser utilizada em vários casos onde existe uma fila de prioridade baseado em um valor, como uma fila médica, por exemplo.

Utilizar uma estrutura Heap pode melhorar a performance e simplicidade ao implementar de um conjunto de dados baseado em prioridade (é possível acessar e remover elementos com maior prioridade) comparado a uma lista, como exemplo.

"""

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def modify_priority(self, idItem, newPriority):
        self.heap[idItem] = (self.heap[idItem][0], self.heap[idItem][1], newPriority)
        self._heapify_up(len(self.heap) - 1)
        self._heapify_down(0)

    def modify_priority(self, idItem, newPriority):
        right_tuple = [i for i in self.heap if i[0] == idItem]
        if len(right_tuple) != 1:
            print("Nenhum valor encontrado (OU múltiplos itens com o mesmo ID).")
            return
        index = self.heap.index(right_tuple[0])
        self.heap[index] = (right_tuple[0][0], right_tuple[0][1], newPriority)
        self._heapify_up(index)
        self._heapify_down(index)
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][2] < self.heap[parent_index][2]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child][2] < self.heap[smallest][2]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][2] < self.heap[smallest][2]:
            smallest = right_child
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# ID, tempo de execução (ms) e prioridade.

tarefas = [(1, 443, 2), (2, 988, 3), (3, 854, 1), (4, 6554, 4)]

heap = MinHeap()

for i in tarefas:
    heap.insert(i)

heap.modify_priority(3, 5)

print("- Tarefas: ")

while len(heap.heap) > 0:
    _id, tempo, prioridade  = heap.pop()
    print(f"\t{_id} - {tempo} - {prioridade}")