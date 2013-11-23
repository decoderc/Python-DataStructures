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

import string
def infixToPostfix(infixexpr):

    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1

    opStack=Stack()
    postfixList=[]

    tokenList=infixepr.split()

    for token in tokenList:
        if token in string.uppercase:
            postfixList.append(token)
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                postfixList.append(topToken)

        else:
            while (not opStack.isEmpty())and\
                  (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())

                opStack.push(token)

            while not opStack.isEmpty():
                postfixlist.append(opStack.pop())

                return string.join(postfixList)
