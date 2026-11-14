class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if cur == None:
                return -1
            else:
                cur = cur.next
        
        return cur.val if cur != None else -1 
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        

    def insertTail(self, val: int) -> None:
        cur = self.head
        node = Node(val)

        if self.head == None:
            self.head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node    

    def remove(self, index: int) -> bool:
        cur = self.head
        prev = None

        if self.head == None:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True


        for i in range(index):
            if cur.next == None:
                return False
            else:
                prev = cur
                cur = cur.next
        
        prev.next = cur.next
        del cur
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur != None:
            res.append(cur.val)
            cur = cur.next
        return res
        
