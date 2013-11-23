#ftastemur hanoi towers game 2011

def print_hanoi(i,a, b, c):
	print "Asama %s: " % (i)
	a.show("\tSol :")
	b.show("\tOrt :")
	c.show("\tSag :")
	i += 1
	return i

def move(X, Y):
	xp = X.peek()
	yp = Y.peek()

	if xp == None and yp == None:
		exit() # bitti
	elif xp == None:
		X.push(Y.pop()) # Y -> X
	elif yp == None:
		Y.push(X.pop()) # X -> Y
	elif yp < xp:
		X.push(Y.pop()) # Y -> X
	else:
		Y.push(X.pop()) # X -> Y

# main
from stack import Stack
a = Stack()
b = Stack()
c = Stack()

n = input("disk sayisi: ")
for i in range(n, 0, -1):
	a.push(i)

i = print_hanoi(0,a,b,c)
while True:
	if n%2 == 1:
		move(a, c)
		i = print_hanoi(i,a,b,c)
		move(a, b)
		i = print_hanoi(i,a,b,c)
		move(b, c)
		i = print_hanoi(i,a,b,c)
	else:
		move(a, b)
		i = print_hanoi(i,a,b,c)
		move(a, c)
		i = print_hanoi(i,a,b,c)
		move(b, c)
		i = print_hanoi(i,a,b,c)
