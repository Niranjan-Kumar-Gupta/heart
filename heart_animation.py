from visual import *
from visual.graph import *
from math import*

scene.width = 1090
scene.height = 720
scene.title = "Heart"
scene.forward = (0,-.1,-1)
ball = sphere(pos=vector(1,-1,0),color = color.red, radius = 1,make_trail=True,trail_type="points",retain=300)

ball3 = sphere(pos=vector(1,-1,0),color = color.red, radius = 1,make_trail=True,trail_type="points",retain=300)
ball2 = sphere(pos=vector(-20,-1,0),color = color.red, radius = 1,make_trail=True,trail_type="points",retain=300)
name = extrusion(pos=[(0,0,0.5),(0,0,0.0)], shape="happy birthday bandana", color=color.cyan,length=20,material=materials.shiny)

l1 = local_light(pos=ball.pos, color=ball.color)
l2 = local_light(pos=ball2.pos, color=ball2.color)
l3 = local_light(pos=ball3.pos, color=color.red)
dt = 0.01
t=0
while(True):        
    rate(100)    
    m=16*sin(t)**3
    n=13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)    
    ball.pos.x =  -m    
    ball.pos.y =  n
    ball3.pos.x =  -m+26    
    ball3.pos.y =  n+15    
    ball2.pos.x = -16*sin(t)**3 -26    
    ball2.pos.y =  13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)-15
    l1.pos.x = ball.pos.x
    l1.pos.y = ball.pos.y
    l1.pos.x = ball2.pos.x
    l1.pos.y = ball2.pos.y
    l1.pos.x = ball3.pos.x
    l1.pos.y = ball3.pos.y      
    t=t+dt
    
