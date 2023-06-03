# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:55:28 2023

@author: an.medinacolmenero
"""

import os
os.chdir("..")
os.chdir("..")

from src.classes.SolarSystem import *

os.chdir("..")

luna = Moon(1,1,1,1,1,1,1,1)
print(luna)

mercurio = Planet("Mercurio", 3.3011e23, [0, 0, 57.9e6], [0, 47.87, 0])
"""
venus = Planet("Venus", 4.8675e24, [0, 0, 108.2e6], [0, 35.02, 0])
tierra = Planet("Tierra", 5.97237e24, [0, 0, 149.6e6], [0, 29.78, 0])
marte = Planet("Marte", 6.4171e23, [0, 0, 227.9e6], [0, 24.07, 0])
jupiter = Planet("Júpiter", 1.8982e27, [0, 0, 778.3e6], [0, 13.07, 0])
saturno = Planet("Saturno", 5.6834e26, [0, 0, 1.429e9], [0, 9.69, 0])
urano = Planet("Urano", 8.6810e25, [0, 0, 2.871e9], [0, 6.81, 0])
neptuno = Planet("Neptuno", 1.02413e26, [0, 0, 4.498e9], [0, 5.43, 0])
"""

#from  import *

"""
from src.classes.CelestialBody import *
from src.classes.Planet import *
luna = CelestialBody(1,1,1,1,1,1,1,1)
planeta = m 
print(luna)
"""
"""
Note change directories on inheritance of classes
"""



"""

#from src.classes.Planet import *
#from src.classes.Atmosphere import *
from src.classes.CelestialBody import *
#from src.classes.Element import *

from src.classes.GasPlanet import *
#from src.classes.Moon import *
#from src.classes.Ring import *
#from src.classes.Star import *
#from src.classes.Surface import *
 
luna = CelestialBody(1,1,1,1,1,1,1,1)
print(luna)

"""