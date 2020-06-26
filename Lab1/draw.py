from turtle import *

g = Turtle()
g.color ('red')
#g.speed(0)
g.speed(10)
for i in range (18) :
    g.circle(150)
    g.left(20)

g.clear()
g.reset()

speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
