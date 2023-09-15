class BufferFullException(BufferError):  
  
    pass


class BufferEmptyException(BufferError):

    pass


class CircularBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = self.capacity + 1
        self.buffer = [None] * self.size
        self.clear()
        
    def clear(self):
        self.w_index = 0
        self.r_index = 0
    
    def __len__(self):        
        return (self.w_index + self.size - self.r_index ) % self.size
    
    def read(self):
        if len(self) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.r_index]
        self.r_index = (self.r_index + 1) % self.size
        return value
    
    def write(self, value):
        if len(self) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.w_index] = value
        self.w_index = (self.w_index + 1) % self.size

    def overwrite(self,value): 
        if len(self) == self.capacity:
            self.read()        
        self.write(value)      
