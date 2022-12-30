from turtle import *
import numpy as np

tt=Turtle()
wn=Screen()
wn.title("Video1")
wn.bgcolor("white")
tt.shape("circle")
tt.color("black","green")
tt.speed(0)
tt.penup()
wn.screensize(canvwidth=500,canvheight=500,bg="white")
a = 150
n = 1000
t=np.linspace(0,2*np.pi,513)
x=(a*np.cos(t))/(1+(np.sin(t))*(np.sin(t)))
y=(a*np.sin(t)*np.cos(t))/(1+(np.sin(t))*(np.sin(t)))
for i in range(512):
    for i in range(512):
        tt.goto(x[i+1],y[i+1])
done()
