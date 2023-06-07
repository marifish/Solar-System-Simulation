from Element import *

class Photosphere:
    def __init__(self, elements = []):
        self._m_elements = elements
        
    #Getter/Setter for elements
    def get_elements(self):
        return self._m_elements
    def set_elements(self, elements):
        self._m_elements = elements

    #Print method
    def info_lements(self):
        text_info = "Composition by volume\n\n" 
        for element in self._m_elements:
            text_info += element.get_name() + ": " + element.get_percentage() +" %"
            text_info +="\n"
            
        
        