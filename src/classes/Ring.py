class Ring:
    def __init__(self, name, radius):
        self._m_name = name
        self._m_radius = radius

    # Getters
    def get_name(self):
        return self._m_name
    
    def get_radius(self):
        return self._m_radius
    
    # Setters
    def set_name(self, name):
        self._m_name = name
    
    def set_radius(self, radius):
        self._m_radius = radius
