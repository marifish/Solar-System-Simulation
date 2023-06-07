from CelestialBody import *

class Planet(CelestialBody):
    def __init__(self,
                 name       = "body",
                 shape      = "spherical",
                 position   = np.array([0,0,0]),
                 velocity   = np.array([0,0,0]),
                 radius     = 1000, 
                 mass = 1000,
                 color      = "red",
                 elements   = [],
                 escape_speed = 1000,
                 temperature  = 1000,
                 volume       = 1000,
                 atmosphere   = [],
                 moons        = [],
                 sun_distance = 1000,
                 num_satellites = 0
                 ):
        
        super().__init__(name, shape, position, velocity, radius, mass, color, elements, escape_speed, temperature, volume)
        self._m_atmosphere = atmosphere
        self._m_moons = moons
        self._m_sun_distance = sun_distance
        self._m_num_satellites = num_satellites
        
    #Getter/Setter for m_atmosphere
    def get_atmosphere(self):
        return self._m_atmosphere
    def set_atmosphere(self, atmosphere):
        self._m_atmosphere = atmosphere
    
    #Getter/Setter for moons
    def get_moons(self):
        return self._m_atmosphere
    def set_moons(self, moons):
        self._m_moons = moons
    
    #Print method
    def info(self):
        physical_characteristics = (f'Physical characteristics:\n\n' +
                                    f'Mean radius: {self_m_radius/1000:.2f} km\n'+
                                    f'Mass: {_m_mass:.2f} kg\n'+
                                    f'Escape velocity: %d km/s\n'+
                                    f'Position: %d m \n'+
                                    f'Surface gravity: %d m/s^2\n'+
                                    f'Temperature: 437 K\n'+
                                    f'Satellites: %d')
        
        return physical_characteristics
        
