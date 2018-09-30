class Queue: #implement queue
    def __init__(self):
        self.list=[]
        self.state = set()
        
    def enqueue(self,item):
        self.list.append(item) #add item to queue
        self.state.add((tuple(item.list)))
        
    def dequeue(self):
        if not self.isEmpty():
            item = self.list[0]  #remove first item from queue (FIFO)
            for i in range(len(self.list)-1):   #re-order queue since first item is removed 
                self.list[i] = self.list[i+1]
            del self.list[-1]  #delete last element to prevent duplication
            self.state.remove(tuple(item.list))
            return item
        
    def isEmpty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0