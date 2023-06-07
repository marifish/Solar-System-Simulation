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
run = True

# Function to handle button click event
def button_click(evt):
    global run
    if evt.text == "Close":
        print("Button 1 clicked!")
        global program_exec
        program_exec = False
        print("program exec", program_exec)
        pyautogui.hotkey('ctrl', 'w')
        print("close window")
    elif evt.text == "Pause":
        run = False
        print("Button Pause clicked!")
    elif evt.text == "Play":
        run = True
        
        print("Button Play clicked!")
        
        
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
        

# Create a VPython canvas
scene = canvas()

# Create buttons
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
    
#
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
    if (i < limit) and run:
        rate(sl.value*5)

        for j in range(len(bodies)):
            df_pos = trayectories[j].loc[i]
        
            position = np.array([df_pos["Position X (m)"],
                             df_pos["Position Y (m)"],
                             df_pos["Position Z (m)"]]) 
        
            print(position)
        
            bodies[j].update_position(new_position = position)

        i += 1   
    
sys.exit()

