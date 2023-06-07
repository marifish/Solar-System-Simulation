# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:26:02 2023

@author: an.medinacolmenero
"""

from vpython import *
import pyautogui
from time import *
import numpy as np
import sys
import random
import pandas as pd

program_exec = True

# Function to handle button click event
def button_click(evt):
    if evt.text == "Close":
        print("Button 1 clicked!")
        global program_exec
        program_exec = False
        print("program exec", program_exec)
        pyautogui.hotkey('ctrl', 'w')
        print("close window")
    elif evt.text == "Pause":
        print("Button 2 clicked!")
    elif evt.text == "Play":
        print("Button 3 clicked!")
        
        
def Color(red, green, blue):
    
    return vector(red/255, green/255, blue/255)

def color_(col = "red"):
    col = col.lower()
    
    cols = {'red': Color(255, 0,0),
              'green': Color(0,255,0),
              'blue': Color(0,0,255),
              'yellow': Color(255,255,0),
              'cyan': Color(0,255,255),
              'magenta': Color(0,0,255),
              'white': Color(255,255,255),
              'black': Color(0,0,0),
              'gray': Color(128,128,128),
              'orange': Color(255,165,0),
              'light': Color(224,255,255)
              }
    
    return cols[col]


class Body:
    
    def __init__(self, name, radius, color__, init_position, scale = 1):
        self._name = name
        self._sphere = sphere(radius = scale * radius, color = color__)
        self._sphere.pos = vector(*init_position)
        self._trayectory = curve(vector(*init_position), color = color__)
        #self._ring = ring(pos = vector(*init_position),axis = vector(0, 0, 1),radius=1e9, thickness=1e8, color= color_)

    def get_name(self):
        return self._name

    def update_position(self, new_position):
        self._sphere.pos = vector(*new_position)
        self._trayectory.append(vector(*new_position))
       # self._ring.pos = vector(*new_position)
        
# Create buttons
# Create a VPython canvas
scene = canvas()

button1 = button(text="Close", bind=button_click)
button2 = button(text="Pause", bind=button_click)
button3 = button(text="Play",  bind=button_click)

num_stars = 1000
stars = []

for _ in range(num_stars):
    phi = random.uniform(0, 2*np.pi)
    thetha = random.uniform(0, np.pi) 
    r = random.uniform(6e12, 7e12)
    star = sphere(pos=vector(r*np.sin(thetha)*np.cos(phi), r*np.sin(thetha)*np.sin(phi) ,r*np.cos(thetha)),
                  radius=random.uniform(1e10,2e10 ),
                  color=color.white,
                  emissive=True,
                  shininess=0)
    stars.append(star)

num_asteroids = 1000
asteroids = []

for _ in range(num_asteroids):
    phi = random.uniform(0, 2*np.pi)
   # thetha = random.uniform(0, np.pi) 
    r = random.uniform(400e9, 450e9)
    asteroid = sphere(pos=vector(r*np.cos(phi), r*np.sin(phi) ,0),
                  radius=random.uniform(1e9,2e9 ),
                  color=color.white,
                  emissive=True,
                  shininess=0)
    asteroids.append(asteroid)


def play_speed(s):
    wt.text = '{:1.1f}x'.format(s.value)
    
sl = slider(min=1, max=5, value=1, length=220, step =1, bind=play_speed, right=0)

wt = wtext(text='{:1.1f}x'.format(sl.value))

#def draw_planets(color):
#   sphere(radius=0.1*mRadius,color = color.red
#planets[]

df = pd.read_csv("data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")


print(df.columns)

df2 = df[["Name", "Color", "Radius (km)"]]

print(df2)

def build_animation_body(file_data = ""):
    
    df = pd.read_csv(file_data)
 
  #  sep = 0
    bodies = []
    for i in df.index:
        data = df.loc[i]
        name = data["Name"]
        radius = 1000 * data["Radius (km)"]
        col  = color_(data["Color"])
        init_position = np.array([data["Position X (m)"],
                                  data["Position Y (m)"],
                                  data["Position Z (m)"]])
        
        body = Body(name = name,radius = radius, color__ = col, init_position = init_position)
        bodies.append(body)
        
   #     sep +=1
    return bodies
    
    
planets = build_animation_body("data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")
sun = build_animation_body("data/sun_data.csv")

bodies = planets + sun
    
# Create background 
"""
num_stars = 1000
stars = []

for _ in range(num_stars):
    phi = random.uniform(0, 2*np.pi)
    thetha = random.uniform(0, np.pi) 
    r = random.uniform(100, 120)
    star = sphere(pos=vector(r*np.sin(thetha)*np.cos(phi), r*np.sin(thetha)*np.sin(phi) ,r*np.cos(thetha)),
                  radius=random.uniform(0.01, 0.5),
                  color=color.white,
                  emissive=True,
                  shininess=0)
    stars.append(star)
"""

"""
#Create 
mRadius=2
circunference_radius = 10
Earth=sphere(radius=0.2*mRadius,texture = textures.earth)
Mercury=sphere(radius=0.1*mRadius,color = color.red)
Venus=sphere(radius=0.2*mRadius,color = color.red)
Mars=sphere(radius=0.15*mRadius,color = color.red)
Jupyter=sphere(radius=0.4*mRadius,color = color.red)
Saturn=sphere(radius=0.3*mRadius,color = color.red)
Uranus=sphere(radius=0.3*mRadius,color = color.red)
Neptune=sphere(radius=0.3*mRadius,color = color.red)

Sun=sphere(radius=2*mRadius, color= color.yellow, emissive=True, shininess=0)
Sun.pos = vector(0,0,0)
deltaTheta=.01
theta = 0
curve1 = curve(vector(10,0,0), color = color.red)
curve2 = curve(vector(20,0,0), color = color.red)
curve3 = curve(vector(30,0,0), color = color.blue)
curve4 = curve(vector(40,0,0), color = color.red)
curve5 = curve(vector(50,0,0), color = color.red)
curve6 = curve(vector(60,0,0), color = color.red)
curve7 = curve(vector(70,0,0), color = color.red)
curve8 = curve(vector(80,0,0), color = color.red)
"""

#name_file = bodies[4].get_name()

#data_trayectory = pd.read_csv(f"simulation/{name_file}.csv")
trayectories = []
for body in bodies:
    name_file = body.get_name()
    data_trayectory = pd.read_csv(f"simulation/{name_file}.csv")
    trayectories.append(data_trayectory)

limit = len(trayectories[0].index)
i = 0
while program_exec:
    if i < limit:
        rate(sl.value*5)

        for j in range(len(bodies)):
            df_pos = trayectories[j].loc[i]
        
            position = np.array([df_pos["Position X (m)"],
                             df_pos["Position Y (m)"],
                             df_pos["Position Z (m)"]]) 
        
            print(position)
        
            bodies[j].update_position(new_position = position)

    i += 1   
    
    
    
    
 
   
"""
    theta += deltaTheta
    xPos = circunference_radius*np.cos(theta)
    yPos = circunference_radius*np.sin(theta)
    curve1.append(vector(xPos,yPos,0))
    curve2.append(vector(2*xPos,2*yPos,0))
    curve3.append(vector(3*xPos,3*yPos,0))
    curve4.append(vector(4*xPos,4*yPos,0))
    curve5.append(vector(5*xPos,5*yPos,0))
    curve6.append(vector(6*xPos,6*yPos,0))
    curve7.append(vector(7*xPos,7*yPos,0))
    curve8.append(vector(8*xPos,8*yPos,0))
    
    
    Mercury.pos=vector(xPos,yPos,0)
    Venus.pos=vector(2*xPos,2*yPos,0)
    Earth.pos=vector(3*xPos,3*yPos,0)
    Mars.pos=vector(4*xPos,4*yPos,0)
    Jupyter.pos=vector(5*xPos,5*yPos,0)
    Saturn.pos=vector(6*xPos,6*yPos,0)
    Uranus.pos=vector(7*xPos,7*yPos,0)
    Neptune.pos=vector(8*xPos,8*yPos,0)
"""
sys.exit()

