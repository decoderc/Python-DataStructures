class Stack():
	def __init__(self):#başlangıç değeri istemiyorum;yani "n" yok.
		self.items=[]#items listenin elemanlarıdır.Boş bir liste oluşturduk.

	def isEmpty(self):
		return self.items==[]

	def push(self,item):#burdaki item eklenecek elemandır.
		self.items.append(item)

	def pop(self,n=None):
		if self.isEmpty():
			return None
		if n==None:
			return self.items.pop()
		else:
			return self.items.pop(n)

	def peek(self,n=None):#sadece elemanı döndürür.
		if self.isEmpty():
			return None
		if n==None:
			return self.items[len(self.items)-1]#pythonda listeler 0. indisten başlar;o yüzden len-1 aldık.
		else:
			return self.items[n]

	def size(self):
		return len(self.items)

def bin2dec(number):

    binstack=Stack()

    for bin in number:
        binstack.push(bin)

    dec=0
    while not binstack.isEmpty():
        dec=2*dec+int(binstack.pop())

    return dec
        
