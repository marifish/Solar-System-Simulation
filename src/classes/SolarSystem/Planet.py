from CelestialBody import*

class Planet(CelestialBody):
    def __init__(self, name, shape, position, velocity, radius, mass, color, elements, atmosphere, moons):
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
        self._m_atmosphere = atmosphere
        self._m_moons = moons
        
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
        print(f"Atmosphere: {self._m_atmosphere}")
        print(f"Moons: {self._m_moons}")
