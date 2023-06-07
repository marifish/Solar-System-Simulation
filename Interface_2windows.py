import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk, Image
import main as m
from src.classes.SolarSystem import *
import subprocess as sp
import threading as td

def run_file():
    # Code to run your Python file
    sp.run(['python', 'animation3D.py'])

m_radio=0
m_volume=0
m_mass=0
m_velocity=0
m_position=0
m_lum=0
m_gravity=0
m_sat=0
m_pressure=0

master = tk.Tk()
master.geometry('300x300')
master.configure(background='black')

def openSimulator():
    #objeto toplevel: nueva ventana
    root = tk.Toplevel(master)
    root.title('Solar System Simulator')
    root.geometry('800x700')
    root.configure(background='black')
    
    image1 = ImageTk.PhotoImage(Image.open('Images/sun.jpg'))
    image2 = ImageTk.PhotoImage(Image.open('Images/mercury.jpg'))
    image3 = ImageTk.PhotoImage(Image.open('Images/venus.jpg'))
    image4 = ImageTk.PhotoImage(Image.open('Images/earth.jpg'))
    image5 = ImageTk.PhotoImage(Image.open('Images/mars.png'))
    image6 = ImageTk.PhotoImage(Image.open('Images/jupiter.jpg'))
    image7 = ImageTk.PhotoImage(Image.open('Images/saturn.jpg'))
    image8 = ImageTk.PhotoImage(Image.open('Images/uranus.jpg'))
    image9 = ImageTk.PhotoImage(Image.open('Images/neptune.jpg'))
    
    #para cambiar frames con c/boton
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

    #sbutton = tk.Button(my_frame1, text='See more', command=webbrowser.open_new_tab(url1)).pack(anchor='sw')
        sun_frame.pack(fill='both',expand=1) 
    
    def mercury_page():
        mercury_frame = tk.Frame(main_frame)
    
    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(mercury_frame)
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
    
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nTemperature: 437 K\nSatellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=20,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: trace (<0.5nPa)\n\nComposition by volume:\n31.7 % potassium\n24.9 % sodium\n9.5 % atomic oxygen\n7.0 % argon\n5.9 % helium\n5.2 % atomic oxygen\n5.2 % nitrogen\n3.6 % carbon dioxide\n3.4 % water\n3.2 % hydrogen\n'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=20,anchor='n')
        label3 = tk.Label(my_frame1, image=image2, height=240, width=240).pack(anchor='se', padx=12)
        label4 = tk.Label(my_frame2, image=image2, height=240, width=240).pack(anchor='se', padx=12)

        mercury_frame.pack(fill='both',expand=1)
    
    def venus_page():
        venus_frame = tk.Frame(main_frame)

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(venus_frame)
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nTemperature: 437 K\nSatellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: 92 atm\n\nComposition by volume:\n96.5% carbon dioxide\n3.5% nitrogen\n0.015% sulfur dioxide\n0.0070% argon\n0.0020% water vapour\n0.0017% carbon monoxide\n0.0012% helium\n0.0007% neon'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image3, height=280, width=280).pack(anchor='se', padx=12)
        label4 = tk.Label(my_frame2, image=image3, height=280, width=280).pack(anchor='se', padx=12)
        venus_frame.pack(fill='both',expand=1)
    
    def earth_page():
        earth_frame = tk.Frame(main_frame)

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(earth_frame)
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
   
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nTemperature: 437 K\nSatellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: 101.32 kPa(at sea level)\n\nComposition by volume:\n78.08% nitrogen\n20.95% oxygen\n~ 1% water vapor (climate variable)\n0.9340% argon\n0.0413% carbon dioxide\n0.00182% neon\n0.00052% helium\n0.00019% methane\n0.00011% krypton\n0.00006% hydrogen'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image4, height=240, width=240).pack(anchor='se', padx=12)
        label4 = tk.Label(my_frame2, image=image4, height=240, width=240).pack(anchor='se', padx=12)
    
        earth_frame.pack(fill='both',expand=1)
    
    def mars_page():
        mars_frame = tk.Frame(main_frame)
    
    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(mars_frame)
        my_notebook.configure()
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')

        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nTemperature: 437 K\nSatellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: 0.00628 atm\n\nComposition by volume:\n95.97% carbon dioxide\n1.93% argon\n1.89% nitrogen\n0.146% oxygen\n0.0557% carbon monoxide\n0.0210% water vapor'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image5, height=240, width=240).pack(anchor='se', padx=12)
        label4 = tk.Label(my_frame2, image=image5, height=240, width=240).pack(anchor='se', padx=12)
    
        mars_frame.pack(fill='both',expand=1)
    
    def jupiter_page():
        jupiter_frame = tk.Frame(main_frame)
        jupiter_frame.configure(background='black')

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(jupiter_frame)
        my_notebook.configure()
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nTemperature: 437 K\nSatellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: 200-600 kPa\n\nComposition by volume:\n89% ± 2.0% hydrogen\n10% ± 2.0% helium\n0.3% ± 0.1% methane\n0.026% ± 0.004% ammonia\n0.0028% ± 0.001% hydrogen deuteride\n0.0006% ± 0.0002% ethane\n0.0004% ± 0.0004% water'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image6, height=230, width=240).pack(anchor='se', padx=12)
        label4 = tk.Label(my_frame2, image=image6, height=230, width=240).pack(anchor='se', padx=12)
    
        jupiter_frame.pack(fill='both',expand=1)
    
    def saturn_page():
        saturn_frame = tk.Frame(main_frame)
        saturn_frame.configure(background='black')

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(saturn_frame)
        my_notebook.configure()
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nKnown satellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: 140 kPa\n\nComposition by volume:\n96.3% ± 2.4% hydrogen\n3.25% ± 2.4% helium\n0.45% ± 0.2% methane\n0.0125% ± 0.0075% ammonia\n0.0110% ± 0.0058% hydrogen deuteride\n0.0007% ± 0.00015% ethane'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image7, height=220, width=310).pack(anchor='se', side='bottom')
        label4 = tk.Label(my_frame2, image=image7, height=220, width=310).pack(anchor='se', side='bottom')
    
        saturn_frame.pack(fill='both',expand=1)

    def uranus_page():
        uranus_frame = tk.Frame(main_frame)
        uranus_frame.configure(background='black')

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(uranus_frame)
        my_notebook.configure()
        my_notebook.pack(pady=5, fill='both', expand=1)
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nMean surface temperature: 76 K\nKnown satellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Surface pressure: below 1.3 bar(130 kPa)\n\nComposition by volume:\n83% ± 3% hydrogen\n15% ± 3% helium\n2.3% methane\n0.009% (0.007–0.015%) hydrogen deuteride\nhydrogen sulfide (trace amount)\nIcy volatiles:\nammonia\nwater ice\nammonium hydrosulfide\nmethane hydrate'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image8, height=240, width=240).pack(anchor='se', side='bottom')
        label4 = tk.Label(my_frame2, image=image8, height=240, width=240).pack(anchor='se', side='bottom')
        uranus_frame.pack(fill='both',expand=1)

    def neptune_page():
        neptune_frame = tk.Frame(main_frame)
        neptune_frame.configure(background='black')

    #añadiendo pestañas de informacion
        my_notebook = ttk.Notebook(neptune_frame)
        my_notebook.configure()
        my_notebook.pack(pady=5, fill='both', expand=1)
        
        my_frame1= tk.Frame(my_notebook, bg='black')
        my_frame2= tk.Frame(my_notebook, bg='black')
        
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_notebook.add(my_frame1, text='Physical characteristics')
        my_notebook.add(my_frame2, text='Atmosphere')
        label1 = tk.Label(my_frame1, text=('Physical characteristics\n\nMean radius: %d km\nVolume: %d km^3\nMass: %d kg\nEscape velocity: %d km/s\nPosition: %d m \nSurface gravity: %d m/s^2\nMean surface temperature: 72 K\nKnown satellites: %d'
                                       % (m_radio,m_volume,m_mass,m_velocity,m_position,m_gravity,m_sat)), font=('OCR A Extended',13), bg='black',fg='white').pack(pady=40,anchor='n',padx=15)
        label2 = tk.Label(my_frame2, text=('Composition by volume:\n80% ± 3.2% hydrogen\n19% ± 3.2% helium\n1.5% ± 0.5% methane\n~0.019% hydrogen deuteride\n~0.00015% ethane\nIcy volatiles:\nammonia\nwater ice\nammonium hydrosulfide\nmethane ice'),
                              font=('OCR A Extended',13),bg='black',fg='white').pack(pady=40,anchor='n')
        label3 = tk.Label(my_frame1, image=image9, height=240, width=240).pack(anchor='se', side='bottom')
        label4 = tk.Label(my_frame2, image=image9, height=240, width=240).pack(anchor='se', side='bottom')
    
        neptune_frame.pack(fill='both',expand=1)

    #para mostrar solo al boton seleccionado
    def hide_indicators():
        sun_indicate.config(bg='black')
        mercury_indicate.config(bg='black')
        venus_indicate.config(bg='black')
        earth_indicate.config(bg='black')
        mars_indicate.config(bg='black')
        jupiter_indicate.config(bg='black')
        saturn_indicate.config(bg='black')
        uranus_indicate.config(bg='black')
        neptune_indicate.config(bg='black')
    
    #para eliminar cada frame de c/planeta al seleccionar otro
    def delete_pages():
        for frame in main_frame.winfo_children(): #metodo para regresar todos los objetos packed de main_frame
            frame.destroy()
    
    #para mostrar que el boton que se ha seleccionado
    def indicate(lb, page): #label argument para indicar el boton elegido
    #page argument para cada pagina del boton elegido
        hide_indicators() # llamando a la funcion hide indicators
        lb.config(bg='white')
        delete_pages()
        page() #llamando a page
    
    options_frame = tk.Frame(root, bg='black')

    #Para intercambiar frames con el menu lateral
    sun_button = tk.Button(options_frame, text='Sun', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(sun_indicate, sun_page))
    sun_button.place(x=10, y=50)
    #color de seleccion del planeta
    sun_indicate = tk.Label(options_frame, text='', bg='black')
    sun_indicate.place(x=3, y=50, width=5, height=40)

    mercury_button = tk.Button(options_frame, text='Mercury', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(mercury_indicate, mercury_page))
    mercury_button.place(x=10, y=100)
    mercury_indicate = tk.Label(options_frame, text='', bg='black')
    mercury_indicate.place(x=3, y=100, width=5, height=40)


    venus_button = tk.Button(options_frame, text='Venus', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(venus_indicate, venus_page))
    venus_button.place(x=10, y=150)
    venus_indicate = tk.Label(options_frame, text='', bg='black')
    venus_indicate.place(x=3, y=150, width=5, height=40)


    earth_button = tk.Button(options_frame, text='Earth', font=('OCR A Extended',15), 
                         fg='white', bd=0, bg='black', 
                         command=lambda:indicate(earth_indicate, earth_page))
    earth_button.place(x=10, y=200)
    earth_indicate = tk.Label(options_frame, text='', bg='black')
    earth_indicate.place(x=3, y=200, width=5, height=40)

    mars_button = tk.Button(options_frame, text='Mars', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(mars_indicate, mars_page))
    mars_button.place(x=10, y=250)
    mars_indicate = tk.Label(options_frame, text='', bg='black')
    mars_indicate.place(x=3, y=250, width=5, height=40)

    jupiter_button = tk.Button(options_frame, text='Jupiter', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(jupiter_indicate, jupiter_page))
    jupiter_button.place(x=10, y=300)
    jupiter_indicate = tk.Label(options_frame, text='', bg='black')
    jupiter_indicate.place(x=3, y=300, width=5, height=40)

    saturn_button = tk.Button(options_frame, text='Saturn', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(saturn_indicate, saturn_page))
    saturn_button.place(x=10, y=350)
    saturn_indicate = tk.Label(options_frame, text='', bg='black')
    saturn_indicate.place(x=3, y=350, width=5, height=40)


    uranus_button = tk.Button(options_frame, text='Uranus', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(uranus_indicate, uranus_page))
    uranus_button.place(x=10, y=400)
    uranus_indicate = tk.Label(options_frame, text='', bg='black')
    uranus_indicate.place(x=3, y=400, width=5, height=40)

    neptune_button = tk.Button(options_frame, text='Neptune', font=('OCR A Extended',15),
                        fg='white', bd=0, bg='black', 
                        command=lambda:indicate(neptune_indicate, neptune_page))
    neptune_button.place(x=10, y=450)
    neptune_indicate = tk.Label(options_frame, text='', bg='black')
    neptune_indicate.place(x=3, y=450, width=5, height=40)


    #Barra lateral
    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=110, height=700)

    main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(heigh=600, width=790)
    
#funcion de boton ok
def timeIntro():
     time=timeInfo.get()
     planets = m.build_bodies(Body_class = Planet,
                            file_name = "data/planets_data_june_04_2023_01h_41m_34s_GTM.csv")

     sun = m.build_bodies(Body_class = Star,
                        file_name = "data/sun_data.csv")

     solar_system = StellarSystem(stars = sun, planets = planets)

     solar_system.gravitational_simulation(days = time, dt_days = 1, plot = True)
     
     # Create a new thread
     thread = td.Thread(target=run_file)

     # Start the thread
     thread.start()
     
     print(time)
     
#para la entrada de tiempo
label1 = tk.Label(text='Enter time set', font=('OCR A Extended',15), bg='black',fg='white').pack(pady=20)

#Adding a textbox entry widget
timeInfo = tk.IntVar()
timeEntered = ttk.Entry(master, width=12, textvariable=timeInfo).pack()

#boton ok introduce el periodo para comenzar la simulacion
button = tk.Button(master,text='Star Simulation',bg='dark gray', fg='white', 
                    command=timeIntro).pack(pady=12)

#boton para abrir ventana de simulador desde ventana inicial
button1 = tk.Button(master, text=' Enter ', bg='dark gray', fg='white', 
                    command=openSimulator).pack(anchor='se',side='bottom')



master.mainloop()