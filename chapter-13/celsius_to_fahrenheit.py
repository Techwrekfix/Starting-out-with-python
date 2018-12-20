#This GUI program converts Celsius temperatures
#to fahrenheit temperatures

import tkinter

class Temperature:
    def __init__(self):
        #Creating the root widget
        self.main_window = tkinter.Tk()

        #Creating four frames to handle widget
        self.header_frame = tkinter.Frame()
        self.temperature_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        #Creating and packing widget for header_frame
        self.header_label = tkinter.Label(self.header_frame,
                                          text='Celsius to Fahrenheit')
        self.header_label.pack()

        #Creating and packing widgets for the temperature_frame
        self.celsius_label = tkinter.Label(self.temperature_frame,text='Enter'
                                           ' Celsius Temperature:')
        self.celsius_entry = tkinter.Entry(self.temperature_frame,width=10)

        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        #Creating and packing widgets for the bottom_frame
        self.display_label = tkinter.Label(self.bottom_frame,
                                          text='Fahrenheit =')
        self.fahren_value = tkinter.StringVar()
        self.fahren_label = tkinter.Label(self.bottom_frame,
                                          textvariable=self.fahren_value)

        self.display_label.pack(side='left')
        self.fahren_label.pack(side='left')

        #Creating and packing the widgets for the button_frame
        self.calc_fahren = tkinter.Button(self.button_frame,
                text='Calcualte Fahrenheit',command=self.calc_fahrenheit)
        self.quit_button = tkinter.Button(self.button_frame,text='Quit',
                                          command=self.main_window.destroy)

        self.calc_fahren.pack(side='left')
        self.quit_button.pack(side='left')

        #Packing the frames
        self.header_frame.pack()
        self.temperature_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()

        #Calling the mainloop
        tkinter.mainloop()

    #The Calc_fahrenheit method is a call
    #back fucntion to the Calculate Fahrenheit button
    def calc_fahrenheit(self):
        celsius = float(self.celsius_entry.get())
        fahrenheit = float(format(((9/5)*celsius) + 32,'.2f'))

        self.fahren_value.set(fahrenheit)

temp = Temperature()
