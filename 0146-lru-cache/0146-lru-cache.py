class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashm = {}
        self.capacity = capacity
        self.dummyH = Node(None, None)
        self.dummyT = Node(None, None)
        self.dummyT.prev = self.dummyH
        self.dummyH.next = self.dummyT

    def get(self, key: int) -> int:
        if key in self.hashm:
            node = self.hashm[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashm:
            self._remove(self.hashm[key])
        node = Node(key, value)
        self._add(node)
        self.hashm[key] = node
        if len(self.hashm) > self.capacity:
            rem = self.dummyH.next
            self._remove(rem)
            del self.hashm[rem.key]

    def _remove(self, node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node: Node):
        p = self.dummyT.prev
        p.next = node
        node.prev = p
        node.next = self.dummyT
        self.dummyT.prev = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)