# py file to run project 

from src.classes.SolarSystem import *
import pandas as pd

currentDir  = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)

print (os.getcwd())

df = pd.read_csv("data/bodies_mass_position_velocities.csv")
print(df.columns)


# Build celestial bodies
bodies = []
for i in df.index:
    body_data = df.loc[i]
    
    name   = body_data["Name"]
    mass   = body_data["Mass (kg)"]
    radius = 1000 * body_data["Radius (km)"]
    color  = body_data["Color"]
    
    
    position = np.array([body_data["Position X (km)"],
                                body_data["Position Y (km)"],
                                body_data["Position Z (km)"]])
    
    velocity = 1000 * np.array([body_data["Velocity X (km/s)"],
                                body_data["Velocity Y (km/s)"],
                                body_data["Velocity Z (km/s)"]])
    
    #print(name, mass, position, velocity, "\n\n")
    
    body = Planet  (name   = name,
            #shape      = "spherical",
            position   = position,
            velocity   = velocity,
            radius     = radius,
            mass       = mass,
            color      = color,
            #elements   = [],
            #atmosphere = [],
            #moons      = [])
            )
    
    bodies.append(body)
    
"""    
body1 = Planet  (#name   = name,
        #shape      = "spherical",
        position   = np.array([-3.14e9,-1.50e11,0]),
        velocity   = np.array([-29.4e3,0,0]),
        #radius     = radius,
        mass       = 5.9722e24,
        #color      = color,
        #elements   = [],
        #atmosphere = [],
        #moons      = [])
        )
#print(len(bodies))
#print(bodies[0].get_trayectory())
"""


#bodies = [body1, bodies[8]]
"""
dt   = 24*60*60
seconds = 24*60*60*365
for i in range(0,seconds,dt):
    for body in bodies:    
       # print("velocidad ", body.get_velocity())
        #print("posicion", body.get_position())
        #print("aceleracion",body.calculate_acceleration(bodies))
       # print("\n")
       print(body.get_name())
       body.calculate_new_position(dt)
       body.calculate_new_velocity(dt, bodies)
"""
#import matplotlib.pyplot as plt

#print("\n\n")

#data = np.transpose(bodies[0].get_trayectory())
#print(np.shape(data))
#print(np.count_nonzero(np.isnan(data[0])), np.count_nonzero(np.isnan(data[1])))
#print(data[0])
#plt.plot(data[0], data[1])
#plt.show()


#print(np.linalg.norm(np.array([-3.14e9,-1.50e11,0])/1e9))


# simulation

#bodies = [bodies[0], bodies[8]]

dt      = 24*60*60*10
seconds = 24*60*60*100000
for i in range(0,seconds,dt):
    for body in bodies:    
       body.calculate_new_position(dt)
       body.calculate_new_velocity(dt, bodies)
       
      
#data = np.transpose(bodies[0].get_trayectory())
#print(data)
#print(len(data))

import matplotlib.pyplot as plt

#print("\n\n")


#print(data[0])
for body in bodies:
    data = np.transpose(body.get_trayectory())
    plt.plot(data[0], data[1])
plt.show()

#plt.plot(data[0], data[1])
#plt.show()

"""
# Create bodies
Planet  (name      = " ",
        #shape      = "spherical",
        position   = np.array([0,0,0]),
        velocity   = np.array([0,0,0]),
        radius     = 1000, mass = 1000,
        color      = "red",
        #elements   = [],
        #atmosphere = [],
        #moons      = [])
        )
"""
"""
luna = Moon(1,1,1,1,1,1,1,1)
print(luna)
"""