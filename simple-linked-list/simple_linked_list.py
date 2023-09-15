class Node:
    def __init__(self, value):
        self._value=value
        self._next=None

    def value(self):
        return self._value

    def next(self):
        return self._next
    
    def set_next(self,node):
        self._next=node

class LinkedList:
    def __init__(self, values=[]):
        self._head=None
        self._counter=0
        for value in values:
            self.push(value)

    def __len__(self):
        return self._counter
    
    def __iter__(self):
        current=self._head
        while current:
            yield current.value()
            current=current.next()

    def head(self):
        if self._head:
            return self._head
        raise EmptyListException("The list is empty.")
        

    def push(self, value):
        node=Node(value)
        if self._head:
            node.set_next(self._head)
        self._head=node  
        self._counter+=1  


    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        ppd=self.head()
        self._head=self._head.next()
        self._counter-=1
        return(ppd.value())
        

    def reversed(self):
        return LinkedList(list(self))


class EmptyListException(Exception):    
    pass