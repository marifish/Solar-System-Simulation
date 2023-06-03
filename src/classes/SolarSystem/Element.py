class Element:
    def __init__(self, name, symbol):
        self._m_name = name
        self._m_symbol = symbol
    
    #Getters
    def get_name(self):
        return self._m_name
    def get_symbol(self):
        return self._m_symbol
    
    #Setters
    def set_name(self, name):
        self._m_name = name
    def set_symbol(self, symbol):
        self._m_symbol = symbol

