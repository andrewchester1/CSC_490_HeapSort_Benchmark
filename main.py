import timeit
import random

#the left sibling child position is parent * 2, right sibling child position is parrent * 2 + 1
def GetParentPosition(position):    #get the parent position from child position
    return position // 2


class MinHeap:
    array = []
    count = 0
    def __init__(self):
        self.array.append({
            "value": 0,
            "index": 0,
            "connect": 0
        })

    def HeapPush(self, value, index, connect):  #add a new node to the tree
        self.array.append({
            "value": value,
            "index": index,
            "connect": connect
        })
        self.count += 1
        self.HeapifyUp(self.Size())

    def ExtrudeMin(self):   #take out the root and rebalance the tree
        returnNode = self.GetNode(1)
        lastNode = self.array.pop()
        self.count -= 1
        if self.count > 0:
            self.array[1] = lastNode
        self.HeapifyDown(1)
        return returnNode

    def HeapifyUp(self, position):  #balance the Heap Tree from low to high
        if position <= 1:
            return

        parentPosition = GetParentPosition(position)
        parentNode = self.GetNode(parentPosition)

        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)

        node = 0 #node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]

        if node != 0:
            self.HeapifyUp(parentPosition)


    def HeapifyDown(self, position):    #balance the tree from high to low
        parentPosition = position
        parentNode = self.GetNode(parentPosition)

        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)

        node = 0  # node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (
                node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2

        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
            self.HeapifyDown(leftPosition)
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]
            self.HeapifyDown(rightPosition)

    def DecreaseValue(self, value, index, connect): #update the value of the node, since it is decreasing the value, only need heapifyup
        pass

    def Size(self):
        return self.count

    def GetNode(self, position):    #when position is not out of array range, return node. Otherwise return None
        if position > self.count:
            return None #python has None as not exist
        else:
            return self.array[position]

@profile
def HeapSort(array):
    heap = MinHeap()
    for i in array:
        heap.HeapPush(i, i, i)
    counter = 0
    while heap.Size() > 0:
        array[counter] = heap.ExtrudeMin()["value"]
        counter += 1
    return array


def GenerateArray(size):
    array = []
    for i in range(size):
        array.append(i)
    random.shuffle(array)
    return array


def test():
    arr = GenerateArray(100000)
    HeapSort(arr)

print(timeit.Timer(test).timeit(number=10))
# test()

