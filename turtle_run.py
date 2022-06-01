from turtle import Turtle, Screen, goto, mainloop, setworldcoordinates
from time import sleep


class anim(Turtle):
    counter = 0

    def first(self):
        anim.counter += 1
        self.speed(0)
        self.width(3)
        self.hideturtle()

        if anim.counter == 1:
            # print('i am 1', anim.counter)
            self.up()
            self.goto(-600, 0)
            self.down()
        elif anim.counter == 2:
            # print('i am 2', anim.counter)
            self.up()
            self.goto(600, 0)
            self.down()
        elif anim.counter == 3:
            # print('i am 2', anim.counter)
            self.up()
            self.goto(0,500)
            self.down()

    def curve(self):
        for i in range(200):
            self.right(1)
            self.forward(1)

    def draw_art(self, color):
        self.color(color)
        self.begin_fill()
        self.left(140)
        self.forward(113)
        self.curve()
        self.left(120)
        self.curve()
        self.forward(112)
        self.end_fill()

    def broken(self,color):
        self.pencolor(color)
        self.pensize(5)
        for i in range(3):
            self.left(75)
            self.forward(40)
            self.right(65)
            self.forward(40)



if __name__ == '__main__':
    screen = Screen()
    screen.tracer(0)
    pin = anim()
    pin.first()
    pin2 = anim()
    pin2.first()
    pin3 = anim()
    pin3.first()

    def h3(p=False):
        for i in range(1000):
            pin3.clear()
            if i > 270:
                pin3.setheading(150)
                print(i)
                h1(True)
                if i == 271:
                    h2(True)

            else:
                pin3.setheading(270)
            pin3.forward(2)
            pin3.setheading(0)
            pin3.draw_art('green')
            screen.update()

    def h2(p=False):
        if p:
            pin2.clear()
            pin2.setheading(0)
            pin2.back(2)
            pin2.seth(0)
            pin2.draw_art('black')
            pin2.seth(30)
            pin2.broken('white')
        else:
            pin2.clear()
            pin2.setheading(0)
            pin2.back(2)
            pin2.seth(0)
            pin2.draw_art('red')

    def h1(p=False):
        pin.clear()
        if p:
            pin.setheading(150)
        else:
            pin.setheading(0)
        pin.forward(2)
        pin.seth(0)
        pin.draw_art('red')
    
    for i in range(1000):
        h1()
        h2()
        screen.update()
        if i > 290:
            h3()
            # print(i)
    
    mainloop
