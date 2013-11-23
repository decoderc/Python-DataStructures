class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist,N):

    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size>1:
        for i in range(N):
            simqueue.enqueue(simqueue.dequeue())

            simqueue.dequeue()

            return simqueue.dequeue()
