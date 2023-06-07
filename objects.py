# py file to run project 

from src.classes.SolarSystem import *
import pandas as pd

currentDir  = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)

print (os.getcwd())

def build_planets(Body_class, file_name = ""):
    
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
        
        sun_distance = body_data["Distance from Sun (km)"]
        
        num_satellites = body_data["Number of Satellites"]
        
        escape_speed = body_data["Escape Velocity (km/s)"]
        
        temperature = body_data["Temperature (°C)"]
        
        volume = body_data["Volume (10^10 km^3)"]
        
        print(name)
        df_atm_composition = pd.read_csv(f"data/elements/{name.lower()}_composition.csv")
        elements = []
        for i in df_atm_composition.index:
            atm_element = df_atm_composition.loc[i]
            
            element = Element(name = atm_element["Element"], percentage  = atm_element["Volume"])
            elements.append(element)
        atmosphere = Atmosphere(elements)
        
        body = Body_class(name     = name,
                          position = position,
                          velocity = velocity,
                          radius   = radius,
                          mass     = mass,
                          color    = color,
                          escape_speed = escape_speed,
                          temperature  = temperature,
                          volume       = volume,
                          atmosphere   = atmosphere,
                          sun_distance = sun_distance,
                          num_satellites = num_satellites)

        bodies.append(body)
    
    return bodies

def build_star(Body_class, file_name = ""):
    
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
        
      #  sun_distance = body_data["Distance from Sun (km)"]
        
       # num_satellites = body_data["Number of Satellites"]
        
        escape_speed = body_data["Escape Velocity (km/s)"]
        
        temperature = body_data["Temperature (°C)"]
        
        volume = body_data["Volume (10^18 m^3)"]
        
        corona_temperature = body_data["Corona Temperature (°C)"]
        
        luminosity = body_data["Luminosity (L☉)"]
        
        print(name)
        df_photo_composition = pd.read_csv(f"data/elements/{name.lower()}_composition.csv")
        elements = []
        for i in df_photo_composition.index:
            photo_element = df_photo_composition.loc[i]
            
            element = Element(name = photo_element["Element"], percentage  = photo_element["Mass"])
            elements.append(element)
        photosphere = Photosphere(elements)
        
        body = Body_class(name     = name,
                          position = position,
                          velocity = velocity,
                          radius   = radius,
                          mass     = mass,
                          color    = color,
                          escape_speed = escape_speed,
                          temperature  = temperature,
                          volume       = volume,
                          photosphere  = photosphere,
                          luminosity   = luminosity,
                          temp_corona  = corona_temperature,
                          )
 

        bodies.append(body)
    
    return bodies

"""
planets = build_planets(Body_class = Planet,
                       file_name = "data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")

sun = build_star(Body_class = Star,
                   file_name = "data/sun_data.csv")

for planet in planets:
    print(planet.info())
    print(planet.get_atmosphere().info_elements())
    
print(sun)
print(sun[0].info())
print(sun[0].get_photosphere().info_elements())
  """  

"""
planets = build_bodies(Body_class = Planet,
                       file_name = "data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")

sun = build_bodies(Body_class = Star,
                   file_name = "data/sun_data.csv")

solar_system = StellarSystem(stars = sun, planets = planets)

solar_system.gravitational_simulation(days = 100000, dt_days = 10, plot = True)
"""





