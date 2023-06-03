from CelestialBody import *

class GasPlanet(CelestialBody):
    def __init__(self, name, shape, position, velocity, radius, mass, color, elements, rings):
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
        self._m_rings = rings

    # Getter and setter for m_rings
    def get_rings(self):
        return self._m_rings
    
    def set_rings(self, rings):
        self._m_rings = rings
    
    # Public method
    def printInfo(self):
        print("Gas Planet Information:")
        print(f"Name: {self._m_name}")
        print(f"Shape: {self._m_shape}")
        print(f"Position: {self._m_position}")
        print(f"Velocity: {self._m_velocity}")
        print(f"Radius: {self._m_radius}")
        print(f"Mass: {self._m_mass}")
        print(f"Color: {self._m_color}")
        print(f"Elements: {self._m_elements}")
        print(f"Rings: {self._m_rings}")

