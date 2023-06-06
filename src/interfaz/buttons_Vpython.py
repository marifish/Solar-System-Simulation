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

program_exec = True


# Function to handle button click event
def button_click(evt):
    if evt.text == "Close Simulation":
        print("Button 1 clicked!")
        global program_exec
        program_exec = False
        print("program exec", program_exec)
        pyautogui.hotkey('ctrl', 'w')
        print("close window")
        #stop_server()
        #print("Stop Server")
        #pyautogui.hotkey('ctrl', 'w')
        #print("close window")
        #print("End script")
    elif evt.text == "Pause":
        print("Button 2 clicked!")
    elif evt.text == "Play":
        print("Button 2 clicked!")

# Create a VPython canvas
scene = canvas()

# Create buttons
button1 = button(text="Close Simulation", bind=button_click)
button2 = button(text="Pause", bind=button_click)
button3 = button(text="Play", bind=button_click)


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





while program_exec:
    rate(10)
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
    
sys.exit()

