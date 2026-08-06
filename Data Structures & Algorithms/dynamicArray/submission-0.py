class DynamicArray:
    
    def __init__(self, capacity: int):
        self.list1 = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.list1[i]

    def set(self, i: int, n: int) -> None:
        self.list1[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        
        self.list1.append(n)



    def popback(self) -> int:
        last = self.list1[len(self.list1)-1]
        self.list1.pop()
        return last

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.list1)
    
    def getCapacity(self) -> int:
        return self.capacity
