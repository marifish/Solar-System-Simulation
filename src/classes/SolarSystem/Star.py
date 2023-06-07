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
                 escape_speed = 1000,
                 temperature    = 1000,
                 volume         = 1000,
                 star_type      = "G",
                 brightness     = 4.83,
                 temp_photosphere = 1000,
                 temp_nucleus     = 2e6,
                 luminosity       = 1000
                 ):
        
        super().__init__(name, shape, position, velocity, radius, mass, color, elements, escape_speed, temperature, volume)
        self._m_type        = star_type
        self._m_brightness  = brightness
        self._m_temp_photosphere = temp_photosphere
        self._m_temp_nucleus     = temp_nucleus
        self._m_luminosity       = luminosity
    
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
        
    def info():
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
