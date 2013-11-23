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
		pass # bitti
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

n = 7
for i in range(n, 0, -1):
	a.push(i)

i = print_hanoi(0,a,b,c)
while True:
	move(a, c)
	i = print_hanoi(i,a,b,c)
	if i > (2**n - 1):	break
	move(a, b)
	i = print_hanoi(i,a,b,c)
	if i > (2**n - 1):	break
	move(b, c)
	i = print_hanoi(i,a,b,c)
	if i > (2**n - 1):	break


