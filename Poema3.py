from turtle import *

setup(1200)
bgcolor("black")
pencolor("brown")
speed(20)
penup()
goto(140, 250)
pendown()
pensize(3)

def linea(posicion, distancia):
    seth(posicion)
    forward(distancia)

def circ(posicion, radio, grado):
    seth(posicion)
    circle(radio, grado)


#Las rosas son rojas
write('Las rosas son rojas', True, "center", 
        ('Courier', 30, 'italic', 'bold') )
penup()
goto(120, 0)
pendown()

angulo = 0

for i in range(10):
    fillcolor("brown2")
    begin_fill()
    linea(angulo, 40)
    circ(angulo, 60, 220)
    forward(40)
    angulo+=40
    end_fill()

penup()
goto(90, 30)
pendown()

angulo = 20
for i in range(10):
    fillcolor("brown1")
    begin_fill()
    linea(angulo, 30)
    circ(angulo, 45, 220)
    forward(30)
    angulo+=40
    end_fill()

penup()
goto(70, 0)
pendown()

angulo=0
for i in range(10):
    fillcolor("red")
    begin_fill()
    linea(angulo, 20)
    circ(angulo, 35, 220)
    forward(20)
    angulo+=40
    end_fill()

penup()
goto(74, -10)
pendown()

angulo = 90
color("saddlebrown")
for i in range(22):
    fillcolor("salmon4")
    begin_fill()
    circ(angulo, 10, 360)
    penup()
    end_fill()
    linea(angulo, 23)
    pendown()
    angulo+=16.5

penup()
goto(60, -10)
pendown()

angulo = 90
color("saddlebrown")
for i in range(18):
    fillcolor("salmon4")
    begin_fill()
    circ(angulo, 10, 360)
    penup()
    end_fill()
    linea(angulo, 23)
    pendown()
    angulo+=20

penup()
goto(45.5, -7.5)
pendown()

angulo = 90
color("saddlebrown")
for i in range(16):
    fillcolor("salmon4")
    begin_fill()
    circ(angulo, 8, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=22.5

penup()
goto(32, -7.2)
pendown()

angulo = 90
color("saddlebrown")
for i in range(13):
    fillcolor("salmon4")
    begin_fill()
    circ(angulo, 8, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=30

penup()
goto(20, -7.2)
pendown()

angulo = 90
color("saddlebrown")
for i in range(9):
    fillcolor("salmon4")
    begin_fill()
    circ(angulo, 8, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=45

penup()
goto(-3.5, -6)
pendown()

fillcolor("salmon4")
begin_fill()
circ(0, 10, 360)
end_fill()

penup()
goto(0, -120)
circ(0, 120, 360)



#Las violetas son azules
clearscreen()
bgcolor("black")
speed(0)
pensize(3)
goto(140, 250)
pendown()
pencolor("blue")
write('Las violetas son azules', True, 'center', 
        ('Courier', 30, 'italic', 'bold'))

penup()
goto(40, 0)
pendown()
color('blueviolet')

angulo = 72
for i in range(5):
    fillcolor('blue4')
    begin_fill()
    linea(angulo, 60)
    circ(angulo, 80, 240)
    forward(60)
    end_fill()
    angulo+=72

penup()
goto(35, 0)
pendown()

angulo = 170
color("orange")
for i in range(20):
    fillcolor("gold")
    begin_fill()
    circ(angulo, 8, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=18

penup()
goto(35, -13)
pendown()

angulo = 167.5
color("orange")
for i in range(17):
    fillcolor("gold")
    begin_fill()
    circ(angulo, 8, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=22.5

penup()
goto(35, -29)
pendown()

angulo = 160
color("orange")
for i in range(12):
    fillcolor("gold")
    begin_fill()
    circ(angulo, 7.7, 360)
    penup()
    end_fill()
    linea(angulo, 20)
    pendown()
    angulo+=30.5

penup()
goto(33, -43)
pendown()

angulo = 156
color("orange")
for i in range(8):
    fillcolor("gold")
    begin_fill()
    circ(angulo, 6.9, 360)
    penup()
    end_fill()
    linea(angulo, 18.8)
    pendown()
    angulo+=44.2

penup()
goto(15, -50)
pendown()
fillcolor('gold')
begin_fill()
circ(180, 10, 360)
end_fill()


#Y mis momentos contigo son los más dulces
clearscreen()
bgcolor("black")
speed(0)
goto(0, 250)
pencolor("red2")
write('Y mis momentos contigo son los más dulces', False, 
        'center', ('Courier', 30, 'italic', 'bold'))

penup()
goto(0, 0)
pendown()

for i in range(14):
    x = i * 10
    fillcolor('red')
    begin_fill()
    linea(45, x * 2)
    circ(45, x, 180)
    circ(135, x, 180)
    linea(315, x * 2)
    end_fill()
    penup()
    linea(270, 20)
    pendown()


hideturtle()
done()
