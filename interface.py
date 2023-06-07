import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk, Image
import objects as obj
from src.classes.SolarSystem import *
import subprocess as sp
import threading as td

# building planets
planets = build_bodies(Body_class = Planet,
                       file_name = "data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")

sun = build_bodies(Body_class = Star,
                   file_name = "data/sun_data.csv")

solar_system = StellarSystem(stars = sun, planets = planets)

# concatenate bodies
#bodies = planets + sun


master = tk.Tk()
master.geometry('300x300')
master.configure(background='black')

def timeIntro():
     time=timeInfo.get()
     print(time)

def openSimulator():
    root = tk.Toplevel(master)
    root.title('Solar System Simulator')
    root.geometry('800x700')
    root.configure(background='black')
    
    def sun_page():
        sun_frame = tk.Frame(main_frame)
    
#añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(sun_frame)
        my_notebook.configure(height=600)
        my_notebook.pack(pady=5, fill='both', expand=1)
        
        my_frame1= tk.Frame(my_notebook,bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Photospheric composition')
        
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nTemperature:\nCenter: 1.57×10^7 K\nPhotosphere: 5.772 K\nCorona: ≈ 5×10^6 K\nLuminosity: %d W'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_lum)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Photospheric composition (by mass):\n\n73.46% hydrogen\n24.85% helium\n0.77% oxygen\n0.29% carbon\n0.16% iron\n0.12% neon\n0.09% nitrogen\n0.07% silicon\n0.05% magnesium\n0.04% sulphur'), 
                      font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label3 = tk.Label(my_frame1, image=image1, height=290, width=290).pack(anchor='se',padx=10)
        label4 = tk.Label(my_frame2, image=image1, height=290, width=290).pack(anchor='se',padx=10)
        
        def planet_page(planet_object):
            planet_frame = tk.Frame(main_frame)

        #añadiendo pestañas de informacion
            my_notebook = ttk.Notebook(planet_frame)
            my_notebook.pack(pady=5, fill='both', expand=1)
            my_frame1= tk.Frame(my_notebook, bg='black')
            my_frame2= tk.Frame(my_notebook, bg='black')
            my_frame1.pack(fill='both', expand=1)
            my_frame2.pack(fill='both', expand=1)
            my_notebook.add(my_frame1, text='Physical characteristics')
            my_notebook.add(my_frame2, text='Atmosphere')
            
            
            label1 = tk.Label(my_frame1, text=planet_object.info(), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
            label2 = tk.Label(my_frame2, text=('Surface pressure: 92 atm\n\nComposition by volume:\n96.5% carbon dioxide\n3.5% nitrogen\n0.015% sulfur dioxide\n0.0070% argon\n0.0020% water vapour\n0.0017% carbon monoxide\n0.0012% helium\n0.0007% neon'),
                                  font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
            label3 = tk.Label(my_frame1, image=image3, height=280, width=280).pack(anchor='se', padx=12)
            label4 = tk.Label(my_frame2, image=image3, height=280, width=280).pack(anchor='se', padx=12)
            venus_frame.pack(fill='both',expand=1)

    #sbutton = tk.Button(my_frame1, text='See more', command=webbrowser.open_new_tab(url1)).pack(anchor='sw')
        sun_frame.pack(fill='both',expand=1) 
#para la entrada de tiempo
label1 = tk.Label(text='Enter time set', font=('OCR A Extended',15), bg='black',fg='white').pack(pady=20)

#Adding a textbox entry widget
timeInfo = tk.IntVar()
timeEntered = ttk.Entry(master, width=12, textvariable=timeInfo).pack()

#boton ok introduce el periodo para comenzar la simulacion
button = tk.Button(master,text='Star Simulation',bg='dark gray', fg='white', 
                    command=timeIntro).pack(pady=12)

#boton para abrir ventana de simulador desde ventana inicial
button1 = tk.Button(master, text=' Solar Sistem Info ', bg='dark gray', fg='white', 
                    command=openSimulator).pack(anchor='se',side='bottom')



master.mainloop()

