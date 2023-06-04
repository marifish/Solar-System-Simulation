# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:56:15 2023

@author: an.medinacolmenero
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class StellarSystem:
    
    def __init__(self, stars, planets):
        self._stars = stars
        self._planets = planets
    
    # Getters        
    def get_stars(self):
        return self._stars
    
    def get_planets(self):
        return self._planets
    
    # Setters
    def set_stars(self, stars):
        self._stars = stars
        
    def set_planets(self, planets):
        self._planets = planets
        
    def gravitational_simulation(self, days = 365, dt_days = 1, plot = False):
        bodies = self._planets + self._stars
              
        dt_seconds  = 24*60*60* dt_days
        lim_seconds = 24*60*60* days
        days = [0]
        for i in range(0, lim_seconds, dt_seconds):
            for body in bodies:    
               body.calculate_new_position(dt_seconds)
               body.calculate_new_velocity(dt_seconds, bodies)
            
            days.append(days[-1]+dt_days)
            
        for body in bodies:
            df_temp = pd.DataFrame(body.get_trayectory(), columns=(["Position X (m)","Position Y (m)","Position Z (m)"]))
            df_temp.index = days
            df_temp.index.name = "days"
            
            df_temp.to_csv(f"simulation/{body.get_name()}.csv")
            if plot: 
                data = np.transpose(body.get_trayectory())
                plt.plot(data[0], data[1])
    
        if plot:
            plt.show()
        
               

        
        