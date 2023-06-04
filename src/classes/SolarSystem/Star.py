from CelestialBody import *

class Star(CelestialBody):
    def __init__(self,
                 name        = "sun",
                 shape       = "spherical",
                 position    = np.array([0,0,0]),
                 velocity    = np.array([0,0,0]),
                 radius      = 1000,
                 mass        = 1000,
                 color       = "red",
                 elements    = [],
                 star_type   = "Yellow dwarf star",
                 brightness  = 4.83,
                 temperature = 15.7e6):
        
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
        self._m_type        = star_type
        self._m_brightness  = brightness
        self._m_temperature = temperature

    # Getters
    def get_type(self):
        return self._m_type
    
    def get_brightness(self):
        return self._m_brightness
    
    def get_temperature(self):
        return self._m_temperature
    
    # Setters
    def set_type(self, star_type):
        self._m_type = star_type
    
    def set_brightness(self, brightness):
        self._m_brightness = brightness
    
    def set_temperature(self, temperature):
        self._m_temperature = temperature
