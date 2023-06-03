from CelestialBody import *
class Star(CelestialBody):
    def __init__(self, name, shape, position, velocity, radius, mass, color, elements, star_type, brightness, temperature):
        super().__init__(name, shape, position, velocity, radius, mass, color, elements)
        self._m_type = star_type
        self._m_brightness = brightness
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
