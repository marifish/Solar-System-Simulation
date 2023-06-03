from CelestialBody import*

class Moon(CelestialBody):
    def __init__(self, name, shape, position, velocity, radius, mass, color, elements):
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
    
    #Getter/Setter for m_shape
    def get_shape(self):
        return self._m_shape
    def set_shape(self, shape):
        self._m_shape = shape
        
    #Print method
    def printInfo(self):
        print("Planet Information:")
        print(f"Name: {self._m_name.title()}")
        print(f"Shape: {self._m_shape}")
        print(f"Position: {self._m_position}")
        print(f"Velocity: {self._m_velocity}")
        print(f"Radius: {self._m_radius}")
        print(f"Mass: {self._m_mass}")
        print(f"Color: {self._m_color}")
        print(f"Elements: {self._m_elements}")
        
        