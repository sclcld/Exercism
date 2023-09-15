class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None        

    def __iter__(self):
        current=self.head
        while current:
            yield current.data
            current=current.next

    def __len__(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count        

    
    def __repr__(self):        
        return f"[ {', '.join(str(val) for val in list(self))} ]"                


    def push(self,val):
        node=Node(val)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next:                
                current=current.next
            current.next=node    
            node.prev=current
    
    def pop(self):
        if not self:
            raise IndexError("List is empty") 
        if len(self)==1:
            ppd=self.head.data
            self.head=None
            return ppd
        current=self.head
        while current.next:
            current=current.next
        ppd=current.data    
        current.prev.next=None
        return ppd

    
    def shift(self):
        if not self.head:
            raise IndexError("List is empty") 
        elif len(self)==1:
            data=self.head.data
            self.head=None
            return data
        shftd=self.head.data
        self.head=self.head.next
        self.head.prev=None            
        return shftd
    
    def unshift(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
    
    def delete(self,data):
        current=self.head
        found=False
        while current:            
            if current.data==data:
                found=True
                if not current.prev and not current.next:
                    self.head=None
                elif not current.prev and current.next:
                    self.head=self.head.next
                    self.head.prev=None
                elif current.prev and current.next:                    
                    current.prev.next=current.next
                    current.next.prev=current.prev
                elif current.prev and not current.next:                    
                    current.prev.next=None
                break
            current=current.next
        if not found:
            raise ValueError("Value not found")          
          