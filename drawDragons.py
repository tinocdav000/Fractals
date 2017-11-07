import dragonGen as g
import turtle as t

it = g.iterChoose(15)
print(it)

t.lt(90)

t.Screen()

t.speed(0)
t.tracer(1000)

def draw(it,size):
    for i in it:
        t.fd(size)
        if i == True:
            t.rt(90)
        elif i == False:
            t.lt(90)
    t.fd(size)

    t.exitonclick()

draw(it,2)
