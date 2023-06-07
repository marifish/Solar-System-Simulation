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
                 temperature  = 1000,
                 volume       = 1000,
                 star_type    = "G",
                 brightness   = 4.83,
                 photosphere  = [],
                 temp_nucleus = 2e6,
                 luminosity   = 1000,
                 temp_corona  = 1000
                 ):
        
        super().__init__(name, shape, position, velocity, radius, mass, color, elements, escape_speed, temperature, volume)
        self._m_type        = star_type
        self._m_brightness  = brightness
        self._m_temp_corona = temp_corona
        self._m_temp_nucleus     = temp_nucleus
        self._m_luminosity       = luminosity
        self._m_photosphere      = photosphere
        
    # Getters
    def get_type(self):
        return self._m_type
    
    def get_brightness(self):
        return self._m_brightness
    
    def get_temperature(self):
        return self._m_temperature
    
    def get_photosphere(self):
        return self._m_photosphere
    
    # Setters
    def set_type(self, star_type):
        self._m_type = star_type
    
    def set_brightness(self, brightness):
        self._m_brightness = brightness
    
    def set_temperature(self, temperature):
        self._m_temperature = temperature
        
    def info(self):
        physical_characteristics = (f'Physical characteristics:\n\n' +
                                    f'Mean radius: {self._m_radius/1000:.2f} km\n'+
                                    f'Mass: {self._m_mass} kg\n'+
                                    f'Escape velocity: {self._m_escape_speed} km/s\n'+
                                    f'Temperature: {self._m_temperature} °C\n'+
                                    f'Corona temperature: {self._m_temp_corona} °C\n' +
                                    f'Nucleus temperature: {self._m_temp_nucleus} °C\n'+
                                    f'Luminosity: {self._m_luminosity} L\n')#f'Satellites: {}')
                                    
        return physical_characteristics


