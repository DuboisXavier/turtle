import os
from turtle import *

x = -300
y = -300
compteur = 0

couleur1 = input("couleur 1?")
couleur2 = input("couleur 2?")
couleur3 = input("couleur 3?")

while compteur <= 20:
	x = x + 60

	speed(0)
	up()
	goto(x,y)
	down()
	ht()

	fillcolor(couleur1)
	begin_fill()
	forward(20)
	left(120)
	forward(20)
	left(60)
	forward(20)
	left(120)
	forward(20)
	end_fill()

	fillcolor(couleur2)
	begin_fill()
	left(180)
	forward(20)
	left(120)
	forward(20)
	left(60)
	forward(20)
	left(120)
	forward(20)
	end_fill()

	fillcolor(couleur3)
	begin_fill()
	right(60)
	forward(20)
	right(120)
	forward(20)
	right(60)
	forward(20)
	right(120)
	forward(20)
	right(60)
	end_fill()

	if x >= 300:

		compteur = compteur + 1
		if compteur % 2 == 1:
			y = y + 18
			x = -270
			
		else:
			y = y + 16
			x = -300

os.system("pause")
