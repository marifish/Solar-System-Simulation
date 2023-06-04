# py file to run project 

from src.classes.SolarSystem import *
import pandas as pd

currentDir  = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)

print (os.getcwd())

def build_bodies(Body_class, file_name = ""):
    
    df_bodies = pd.read_csv(file_name)

    bodies = []
    for i in df_bodies.index:
        body_data = df_bodies.loc[i]
        
        name   = body_data["Name"]
        mass   = body_data["Mass (kg)"]
        radius = 1000 * body_data["Radius (km)"]
        color  = body_data["Color"]
        
        position = np.array([body_data["Position X (m)"],
                             body_data["Position Y (m)"],
                             body_data["Position Z (m)"]])
        
        velocity = 1000 * np.array([body_data["Velocity X (km/s)"],
                                    body_data["Velocity Y (km/s)"],
                                    body_data["Velocity Z (km/s)"]])
        
        body = Body_class(name     = name,
                          position = position,
                          velocity = velocity,
                          radius   = radius,
                          mass     = mass,
                          color    = color)

        bodies.append(body)
    
    return bodies



planets = build_bodies(Body_class = Planet,
                       file_name = "data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")

sun = build_bodies(Body_class = Star,
                       file_name = "data/sun_data.csv")


solar_system = StellarSystem(stars = sun, planets = planets)


solar_system.gravitational_simulation(days = 1000, dt_days = 10, plot = True)






