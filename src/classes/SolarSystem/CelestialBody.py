import numpy as np

G = 6.67430e-11

class CelestialBody:
    def __init__(self, 
                 name     = "body",
                 shape    = "spherical",
                 position = np.array([0,0,0]),
                 velocity = np.array([0,0,0]),
                 radius   = 1000, 
                 mass     = 1000,
                 color    = "red",
                 elements = []):
        
        # Initialize the attributes of the celestial body
        self._m_name       = name
        self._m_shape      = shape
        self._m_position   = position
        self._m_velocity   = velocity
        self._m_radius     = radius
        self._m_mass       = mass
        self._m_color      = color
        self._m_elements   = elements
        self._m_trayectory = [position]

    # Getters
    def get_name(self):
        return self._m_name
    
    def get_shape(self):
        return self._m_shape
    
    def get_position(self):
        return self._m_position
    
    def get_velocity(self):
        return self._m_velocity
    
    def get_radius(self):
        return self._m_radius
    
    def get_mass(self):
        return self._m_mass
    
    def get_color(self):
        return self._m_color
    
    def get_elements(self):
        return self._m_elements
    
    def get_trayectory(self):
        return self._m_trayectory
    
    # Setters
    def set_name(self, name):
        self._m_name = name
    
    def set_shape(self, shape):
        self._m_shape = shape
    
    def set_position(self, position):
        self._m_position = position
    
    def set_velocity(self, velocity):
        self._m_velocity = velocity
    
    def set_radius(self, radius):
        self._m_radius = radius
    
    def set_mass(self, mass):
        self._m_mass = mass
    
    def set_color(self, color):
        self._m_color = color
    
    def set_elements(self, elements):
        self._m_elements = elements

    # Member functions
    
    def calculate_acceleration(self, bodies):
        
        acceleration = np.array([0,0,0])
        
        for body in bodies:
            if  body != self:
                vec_body_self = body.get_position() - self.get_position()
                distance = np.linalg.norm(vec_body_self)
                accel_body_self = (G * body.get_mass() * vec_body_self) / (distance ** 3)
                acceleration = acceleration + accel_body_self
    
        return acceleration
    
    def calculate_new_position(self, dt):
        # Perform calculation to update the position
        self._m_position = self._m_position + self._m_velocity*dt
        self._m_trayectory.append(self._m_position)
        
    def calculate_new_velocity(self, dt, bodies):
        acceleration = self.calculate_acceleration(bodies)
        self._m_velocity = self._m_velocity + acceleration * dt

    def print_info(self):
        # Print information about the celestial body
        pass
