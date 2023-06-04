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
    
dt      = 24*60*60*10
seconds = 24*60*60*100000
for i in range(0,seconds,dt):
    for body in bodies:    
       body.calculate_new_position(dt)
       body.calculate_new_velocity(dt, bodies)
       

import matplotlib.pyplot as plt


#bodies = [bodies[8]]
for body in bodies:
    data = np.transpose(body.get_trayectory())
    plt.plot(data[0], data[1])
plt.show()

