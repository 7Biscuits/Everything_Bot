# Modules:

import pyttsx3
import turtle
from turtle import *
from turtle import Shape, Turtle, mainloop, Vec2D as Vec
import datetime
from datetime import datetime
from datetime import date
import os
import random

# Name & Age:

name = input("Enter your name: ")
print("Hey there " + name)
age = int(input("Enter your age: "))

if age < 5:
    print("Sorry you are not eligible to visit here")
else:
    print("Welcome " + name)

if age >= 5:
    look = input("What are you looking for? ")

# Calculator:

if look == "Calculator":
    #print("Oh so you are looking for a calculator, here you go")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")

    if operator == '+':
        print("The sum of the numbers = ", num1 + num2)
    elif operator == '-':
        print("The difference of the numbers = ", num1 - num2)
    elif operator == '*':
        print("The multiplication of the numbers = ", num1 * num2)
    elif operator == '/':
        print("The difference of the number = ", num1 / num2)
    else:
        print("Invalid Input")

# Contents of this programs:

elif look == "Keywords of this program":
    print('''Keywords:
        * Calculator
        * Clock
        * Computer speak
        * Integer identifier
        * Bot Keywords
        * Animation
        * Animation2
        * YinYang
        * Bot
        * Credits
        * Speak credits
        * Time
        * Speak time
        * Date
        * Speak date
        * Paint
        * Earth and moon
        * Wish Me
        * generate random number
        * toss
        * reverse word
        * speed distance time finder''')

# Clock:

elif look == "Clock":
    print("Please open the python turtle graphics window to see the clock")
    def jump(distanz, winkel=0):
        penup()
        right(winkel)
        forward(distanz)
        left(winkel)
        pendown()

    def hand(laenge, spitze):
        fd(laenge*1.15)
        rt(90)
        fd(spitze/2.0)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze/2.0)

    def make_hand_shape(name, laenge, spitze):
        reset()
        jump(-laenge*0.15)
        begin_poly()
        hand(laenge, spitze)
        end_poly()
        hand_form = get_poly()
        register_shape(name, hand_form)

    def clockface(radius):
        reset()
        pensize(7)
        for i in range(60):
            jump(radius)
            if i % 5 == 0:
                fd(25)
                jump(-radius-25)
            else:
                dot(3)
                jump(-radius)
            rt(6)

    def setup():
        global second_hand, minute_hand, hour_hand, writer
        mode("logo")
        make_hand_shape("second_hand", 125, 25)
        make_hand_shape("minute_hand",  130, 25)
        make_hand_shape("hour_hand", 90, 25)
        clockface(160)
        second_hand = Turtle()
        second_hand.shape("second_hand")
        second_hand.color("gray20", "gray80")
        minute_hand = Turtle()
        minute_hand.shape("minute_hand")
        minute_hand.color("blue1", "red1")
        hour_hand = Turtle()
        hour_hand.shape("hour_hand")
        hour_hand.color("blue3", "red3")
        for hand in second_hand, minute_hand, hour_hand:
            hand.resizemode("user")
            hand.shapesize(1, 1, 3)
            hand.speed(0)
        ht()
        writer = Turtle()
        writer.ht()
        writer.pu()
        writer.bk(85)

    def wochentag(t):
        wochentag = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
        return wochentag[t.weekday()]

    def datum(z):
        monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
        j = z.year
        m = monat[z.month - 1]
        t = z.day
        return "%s %d %d" % (m, t, j)

    def tick():
        t = datetime.today()
        sekunde = t.second + t.microsecond*0.000001
        minute = t.minute + sekunde/60.0
        stunde = t.hour + minute/60.0
        try:
            tracer(False)
            writer.clear()
            writer.home()
            writer.forward(65)
            writer.write(wochentag(t),
                        align="center", font=("Courier", 14, "bold"))
            writer.back(150)
            writer.write(datum(t),
                        align="center", font=("Courier", 14, "bold"))
            writer.forward(85)
            tracer(True)
            second_hand.setheading(6*sekunde)  # or here
            minute_hand.setheading(6*minute)
            hour_hand.setheading(30*stunde)
            tracer(True)
            ontimer(tick, 100)
        except Terminator:
            pass

    def main():
        tracer(False)
        setup()
        tracer(True)
        tick()
        return "EVENTLOOP"

    if __name__ == "__main__":
        mode("logo")
        msg = main()
        print(msg)
        mainloop()

# Credits:

elif look == "Credits":
    print("This program is made by Rudransh Srivastav in python")

# Speak credits:

elif look == "Speak credits":
     engine = pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[0].id)

     def speak(audio):
        engine.say(audio)
        engine.runAndWait()

     speak("This program was made by Rudransh Srivastav in python")

# Computer speak

elif look == "Computer speak":
    engine_2 = pyttsx3.init('sapi5')
    voices = engine_2.getProperty('voices')
    engine_2.setProperty('voice', voices[0].id)

    def say(audio):
        engine_2.say(audio)
        engine_2.runAndWait()


    x = input("What do you want the computer to speak: ")
    say(x)

# Positive or negetive or 0 integer identifier:

elif look == "Integer identifier":

    x = float(input("Enter a number: "))

    if x < 0:
        print(x, " is a negetive number")
    elif x > 0:
        print(x, " is a positive number")
    elif x == 0:
        print("Number entered is 0")

# speed distance time:

elif look == 'speed distance time finder':
    x = input("Enter what you want to find(speed, distance or time): ")

    if x == "speed":
        dis = float(input("Enter the distance(in m): "))
        t = float(input("Enter the time(in sec): "))
        print("The speed = ", dis/t, "m/sec")

    elif x == "distance":
        tim = float(input("Enter the time(in sec): "))
        sp = float(input("Enter the speed(in m/sec): "))
        print("The distance = ", tim * sp, "m")

    elif x == "time":
        diis = float(input("Enter the distance(in m): "))
        sspeed = float(input("Enter the speed(in m/sec): "))
        print("The time = ", diis/sspeed, "sec")

    else:
        print("Invalid input")

# Bot Keywords:

elif look == "Bot keywords":
    print("hello")
    print("how are you")
    print("what do you like to eat")
    print("who is your favorite youtuber")
    print("what is your favorite anime")
    print("who are you")
    print("what do you love the most")
    print("which biscuit do you like the most")
    print("which programming language is the best")
    print("what do you hate the most")
    print("which country is the best in the world")
    print("Integer identifier")
    print("where do you live")
    print("bye")

# 1st Animation:

elif look == "Animation":
    print("Please open python turtle graphics window appeared on your taskbar to see the animation")
    trtl = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(400,300)
    screen.bgcolor('black')
    trtl.pencolor('red')
    trtl.pensize(5)
    trtl.speed(1)
    trtl.shape('turtle')
    trtl.forward(100)
    trtl.right(90)
    trtl.forward(100)
    trtl.right(90)
    trtl.forward(100)
    trtl.right(90)
    trtl.forward(100)
    trtl.penup()
    trtl.setpos(-120,100)
    trtl.pendown()
    trtl.pencolor('green')
    trtl.write('Animation by Rudransh',font=("Frenchscript",16))
    trtl.penup()
    trtl.ht()

# 2nd Animation:

elif look == "Animation2":
    print("Please open python turtle graphics window appeared on your taskbar to see the animation")
    try:
        import turtle
    except ImportError:
        os.system('python -m pip install -U pythonturtle')
        import turtle

    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)

# YinYang formation:

elif look == "YinYang":
    print("Please open python turtle graphics window shell appered on your taskbar to see the yinyang formation")
    def yin(radius, color1, color2):
        width(3)
        color("black", color1)
        begin_fill()
        circle(radius/2., 180)
        circle(radius, 180)
        left(180)
        circle(-radius/2., 180)
        end_fill()
        left(90)
        up()
        forward(radius*0.35)
        right(90)
        down()
        color(color1, color2)
        begin_fill()
        circle(radius*0.15)
        end_fill()
        left(90)
        up()
        backward(radius*0.35)
        down()
        left(90)

    def main():
        reset()
        yin(200, "black", "white")
        yin(200, "white", "black")
        ht()
        return "Done!"

    if __name__ == '__main__':
        main()
        mainloop()

# Earth and moon:

elif look == "Earth and moon":
    print("Please open the turtle graphics window appeared on your task bar to see the animation")
    G = 8
    class GravSys(object):
        def __init__(self):
            self.planets = []
            self.t = 0
            self.dt = 0.01
        def init(self):
            for p in self.planets:
                p.init()
        def start(self):
            for i in range(10000):
                self.t += self.dt
                for p in self.planets:
                    p.step()

    class Star(Turtle):
        def __init__(self, m, x, v, gravSys, shape):
            Turtle.__init__(self, shape=shape)
            self.penup()
            self.m = m
            self.setpos(x)
            self.v = v
            gravSys.planets.append(self)
            self.gravSys = gravSys
            self.resizemode("user")
            self.pendown()
        def init(self):
            dt = self.gravSys.dt
            self.a = self.acc()
            self.v = self.v + 0.5*dt*self.a
        def acc(self):
            a = Vec(0,0)
            for planet in self.gravSys.planets:
                if planet != self:
                    v = planet.pos()-self.pos()
                    a += (G*planet.m/abs(v)**3)*v
            return a
        def step(self):
            dt = self.gravSys.dt
            self.setpos(self.pos() + dt*self.v)
            if self.gravSys.planets.index(self) != 0:
                self.setheading(self.towards(self.gravSys.planets[0]))
            self.a = self.acc()
            self.v = self.v + dt*self.a

    # creating compound yellow/blue turtleshape for Earth

    def main():
        s = Turtle()
        s.reset()
        s.getscreen().tracer(0,0)
        s.ht()
        s.pu()
        s.fd(6)
        s.lt(90)
        s.begin_poly()
        s.circle(6, 180)
        s.end_poly()
        m1 = s.get_poly()
        s.begin_poly()
        s.circle(6,180)
        s.end_poly()
        m2 = s.get_poly()

        planetshape = Shape("compound")
        planetshape.addcomponent(m1,"orange")
        planetshape.addcomponent(m2,"blue")
        s.getscreen().register_shape("planet", planetshape)
        s.getscreen().tracer(1,0)

        # gravitational system setup
        gs = GravSys()
        sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
        sun.color("yellow")
        sun.shapesize(1.8)
        sun.pu()
        earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
        earth.pencolor("green")
        earth.shapesize(0.8)
        moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
        moon.pencolor("blue")
        moon.shapesize(0.5)
        gs.init()
        gs.start()
        return "Done!"

    if __name__ == '__main__':
        main()
        mainloop()

# Generate random number:

elif look == "generate random number":
    print("Don't enter a float number")
    rand_num1 = int(input("Enter the first number you want the random number to be in between: "))
    rand_num2 = int(input("Enter the second number you want the random number to be in between: "))
    rand_gen = random.randint(rand_num1, rand_num2)
    print("Random number generated between", rand_num1, "and", rand_num2, "is ", rand_gen)

# Reverse word:

elif look == 'reverse word':
    rev_str = input("Enter the word you want to reverse: ")
    print(rev_str[::-1])

# Toss:

elif look == "toss":
    toss = ['heads', 'tails']
    rand_tos = random.choice(toss)

    user_res = input("heads or tails? ")

    if user_res == rand_tos:
        print("Congrats you have won the toss")

    elif user_res != rand_tos:
        print("Sorry, you have the toss")

# Fibonacci series:

elif look == "Fibonacci series":
    x = int(input("Enter the level upto which the series needs to be printed: "))
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1, x + 1):
        c = a + b
        print(c)
        a = b
        b = c

# Date:

elif look == "Date":
    today = date.today()
    print("Today's date:", today)

# Speak date:

elif look == "Speak date":
    today = date.today()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Todays date is ")
    speak(today)

# Time:

elif look == "Time":
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

# Speak time:

elif look == "Speak time":
    get = datetime.now()
    currenttime = get.strftime("%Hhours %Mminutes %Sseconds")

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Time is" + currenttime)

# Wish Me:

elif look == "Wish Me":
    import datetime
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wish():
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour <= 12:
            speak("Good Morning!")
            speak("Hope you will have a great day!")

        elif hour >=12 and hour <= 18:
            speak("Good Afternoon!")
            speak("Hope you are having a good day")

        else:
            speak("Good Evening!")
            speak("Hope you are having a great day")

    if __name__ == "__main__":
        wish()

# Paint:

elif look == "Paint":
    print("Please open python turtle graphics window appeared on your taskbar to access paint")
    def switchupdown(x=0, y=0):
        if pen()["pendown"]:
            end_fill()
            up()
        else:
            down()
            begin_fill()

    def changecolor(x=0, y=0):
        global colors
        colors = colors[1:]+colors[:1]
        color(colors[0])

    def main():
        global colors
        shape("circle")
        resizemode("user")
        shapesize(.5)
        width(3)
        colors=["red", "green", "blue", "yellow"]
        color(colors[0])
        switchupdown()
        onscreenclick(goto,1)
        onscreenclick(changecolor,2)
        onscreenclick(switchupdown,3)
        return "EVENTLOOP"

    if __name__ == "__main__":
        msg = main()
        print(msg)
        mainloop()

# Using paint:

elif look == "Using paint":
    print("Press left mouse button to move the paint cursor")
    print("Press middle mouse button to change color")
    print("Press right mouse button to toggle between pen up and pen down")
    print("NO line is drawn while paint cursor moves until you press right mouse button")

# Bot:

elif look == "Bot":
    print("Ok here you go")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    x = input("Type: ")

    if x == 'hello':
        speak("Hello how are you")
    elif x == 'how are you':
        speak("I am fine thanks for asking")
    elif x == 'what do you like to eat':
        speak("i love eating biscuits")
    elif x == 'what is your favorite anime':
        speak("My favorite anime is deathnote")
    elif x == 'who are you':
        speak("i am elon musk........hahaha just kidding i am just a bot")
    elif x == 'bye':
        speak("ok bye see you soon later")
    elif x == 'what do you love the most':
        speak("i love biscuits more than my life")
    elif x == 'which programming language is the best':
        speak("PYthon is the best programming language")
    elif x == 'what do you hate the most':
        speak("ofcourse i hate schools the most")
    elif x == 'where do you live':
        speak("I live on mars")
    else:
        speak("sorry i am not programmed to reply to this message")

else:
    print("Sorry I am not programmed to perform the given task")
