class Element:
    def __init__(self, name, percentage):
        self._m_name = name
        self._m_percentage = percentage
    
    #Getters
    def get_name(self):
        return self._m_name
    def get_percentage(self):
        return self._m_percentage
    
    #Setters
    def set_name(self, name):
        self._m_name = name
    def set_percentage(self, percentage):
        self._m_percentage = percentage

