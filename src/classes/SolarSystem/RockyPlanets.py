from CelestialBody import *
from Surface import *

class RockyPlanets(CelestialBody):
    def __init__(self, name, shape, position, velocity, radius, mass, color, elements, surface):
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
        self._m_surface = surface
    
    #Getter/Setter for m_surface
    def get_surface(self):
        return self._m_surface
    def set_atmosphere(self, surface):
        self._m_surface = surface
        
    #Print method
    def printInfo(self):
        print("Rocky Planet Information:")
        print(f"Name: {self._m_name.title()}")
        print(f"Shape: {self._m_shape}")
        print(f"Position: {self._m_position}")
        print(f"Velocity: {self._m_velocity}")
        print(f"Radius: {self._m_radius}")
        print(f"Mass: {self._m_mass}")
        print(f"Color: {self._m_color}")
        print(f"Elements: {self._m_elements}")
        print(f"Surface: {self._m_surface}")
