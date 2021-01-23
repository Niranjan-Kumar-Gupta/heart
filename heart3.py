from visual import*
from visual.graph import*
import numpy as np


#trail_color=color.white
scene.background = color.white

r = 2
dtheta = np.pi/50
t = 0
circle_list = []
while(t <= 2*pi):
    circle_list.append(vector(-16*sin(t)**3,13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t),0))
    t += dtheta
circle = curve(pos=circle_list,color = color.red)

sphere2 = sphere(pos = vector(2,0,0),radius=0.1,color = color.red,make_trail=True,retain=3000)
sphere3 = sphere(pos = vector(2,0,0),radius=0.1,color = color.white,make_trail=True,retain=2800)

sphere4 = sphere(pos = vector(0,0,0),radius=0.3,color = color.red)
hit_direction = vector(2,2,0)

dt = 0.09

sphere5 = sphere(pos = vector(25,17,0),radius=0.3,color = color.red,make_trail=True,retain=2000)
sphere6 = sphere(pos = vector(-25,-17,0),radius=0.3,color = color.red,make_trail=True,retain=2000)
sphere7 = sphere(pos = vector(25,-17,0),radius=0.3,color = color.red,make_trail=True,retain=2000)
sphere8 = sphere(pos = vector(-25,17,0),radius=0.3,color = color.red,make_trail=True,retain=2000)



while(True):
    rate(500)
    magnitude = mag(sphere2.pos)
    magnitude2 = mag(sphere3.pos)
    for i in range(1,len(circle_list)):
        
        x = float(mag(circle_list[i]))    
        if magnitude + sphere2.radius >= x:
            hit_direction -= 2*sphere2.pos*dot(sphere2.pos,hit_direction)/magnitude**2
                                    
    sphere2.pos += hit_direction*dt
    sphere3.pos += hit_direction*dt
    sphere5.pos += hit_direction*dt
    sphere6.pos += hit_direction*dt
    sphere7.pos += hit_direction*dt
    sphere8.pos += hit_direction*dt

    
    

