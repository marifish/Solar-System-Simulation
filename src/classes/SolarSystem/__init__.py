# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:32:29 2023

@author: an.medinacolmenero
"""

import os

currentDir  = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)


from CelestialBody import *
from Surface import *
from Ring import *
from Element import * 
from Atmosphere import *
from Planet import *
from Star import *
from Moon import *
from GasPlanet import *
from RockyPlanets import *
