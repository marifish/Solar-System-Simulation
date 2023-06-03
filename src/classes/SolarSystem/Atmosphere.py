class Atmosphere:
    def __init__(self, elements):
        self._m_elements = elements
        
    #Getter/Setter for elements
    def get_elements(self):
        return self._m_elements
    def set_elements(self, elements):
        self._m_elements = elements

    #Print method
    def printElements(self):
        print(f"Elementos: {self._m_elements}")
        