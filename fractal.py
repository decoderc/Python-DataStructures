def fractal(taban,derinlik):
	for i in 0,1,2,3:
		turtle.forward(taban*derinlik)
		turtle.left(90)
	for i in 0,1,2,3,4,5:
		if i==0 or i==1 or i==5:
			turtle.forward((taban*derinlik)/4)
			turtle.left(90)
		elif i==2 or i==3 or i==4:
			turtle.forward((taban*derinlik)/2)
			turtle.left(90)
	turtle.up()
	turtle.left(180)
	turtle.forward((taban*derinlik)*3/4)
	for i in 0,1,2,3,4,5:
		if i==0 or i==1 or i==5:
			if i==0:
				turtle.forward((taban*derinlik)/4)
				turtle.left(90)
			else:
				turtle.down()
				turtle.forward((taban*derinlik)/4)
				turtle.left(90)
		elif i==2 or i==3 or i==4:
			turtle.down()
			turtle.forward((taban*derinlik)/2)
			turtle.left(90)
	turtle.up()
	turtle.right(90)
	turtle.forward((taban*derinlik))
	for i in 0,1,2,3,4:
		if i==0 or i==4:
			turtle.down()
			turtle.forward((taban*derinlik)/4)
			turtle.left(90)
		else:
			turtle.down()
			turtle.forward((taban*derinlik)/2)
			turtle.left(90)
	turtle.up()
	turtle.forward((taban*derinlik)*3/2)
	turtle.right(90)
	for i in 0,1,2,3,4:
		if i==0 or i==4:
			turtle.down()
			turtle.forward((taban*derinlik)/4)
			turtle.right(90)
		else:
			turtle.down()
			turtle.forward((taban*derinlik)/2)
			turtle.right(90)
