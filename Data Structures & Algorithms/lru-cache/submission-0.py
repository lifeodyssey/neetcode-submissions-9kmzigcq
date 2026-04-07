class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.val=val
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.map={}        
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    def _remove(self,node:Node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev

    def _add_to_tail(self,node:Node):
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node=self.map[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node=self.map[key]
            node.val=value
            self._remove(node)
            self._add_to_tail(node)
            return
        node=Node(key,value)
        self.map[key]=node
        self._add_to_tail(node)
        if len(self.map)>self.cap:
            lru=self.head.next
            self._remove(lru)
            self.map.pop(lru.key)
