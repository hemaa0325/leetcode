class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [None]*k
        self.k = k
        self.f = 0
        self.r = -1
        self.c = 0
        

    def enQueue(self, value):
        if self.isFull():
            return False
        self.r = (self.r+1)%self.k
        self.q[self.r]=value
        self.c+=1
        return True
        

    def deQueue(self):
        if self.isEmpty():
            return False
        self.q[self.f]=None
        self.f = (self.f+1)%self.k
        self.c-=1
        return True
        

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.f]
        

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[self.r]
        

    def isEmpty(self):
        return self.c == 0
        

    def isFull(self):
        return self.c == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()