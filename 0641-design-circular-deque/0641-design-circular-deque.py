class Node:
    def __init__(self,val,next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.lim = k
        self.dummyhead = Node(-1)
        self.dummytail = Node(-1)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.count = 0
        
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = Node(value)
        curfir = self.dummyhead.next
        self.dummyhead.next = cur
        cur.next = curfir
        cur.prev = self.dummyhead
        curfir.prev = cur
        self.count += 1
        
        return True
        
        
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = Node(value)
        curlast = self.dummytail.prev
        cur.next = self.dummytail
        cur.prev = curlast
        curlast.next = cur
        self.dummytail.prev = cur
        
        self.count += 1
        
        return True
        
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        curfir = self.dummyhead.next
        cur = curfir.next
        self.dummyhead.next = cur
        cur.prev = self.dummyhead
        
        self.count -= 1 
        return True
       
            
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        first = self.dummytail.prev
        second = self.dummytail.prev.prev
        
        self.dummytail.prev = second
        second.next = self.dummytail
        
        self.count -= 1
        
        return True
        

    def getFront(self) -> int:
        return self.dummyhead.next.val
        
        

    def getRear(self) -> int:
        return self.dummytail.prev.val
        

    def isEmpty(self) -> bool:
        return self.count == 0 
        

    def isFull(self) -> bool:
        return self.count == self.lim
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()