class Stack:
    def __init__(self,N):
        self.sinir=N
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):
       
        if len(self.items)+1 < self.sinir:
        
            self.items.append(item)
        else:
            print "limit doldu lutfen baska sayi girmeyiniz"
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

        

