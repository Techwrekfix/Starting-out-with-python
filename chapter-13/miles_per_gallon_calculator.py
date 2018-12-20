#This GUI program calculates a car's gas mileage

import tkinter

class MPG:
    def __init__(self):
        #Calling the root widget
        self.main_window = tkinter.Tk()

        #Creating five frames to handle widgets
        self.header_frame = tkinter.Frame()
        self.gallon_frame = tkinter.Frame()
        self.miles_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        #Creating and packing widget for header_frame
        self.mpg_label = tkinter.Label(self.header_frame,text='MPG CALCULATOR')
        self.mpg_label.pack()

        #Creating and packing widgets for gallon_frame
        self.gallons_label = tkinter.Label(self.gallon_frame,text='Enter'
                                    ' the number of gallons of gas of the car:')
        self.gallons_entry = tkinter.Entry(self.gallon_frame,width=10)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        #Creating and packing widgets for miles_frame
        self.miles_label = tkinter.Label(self.miles_frame,text='Enter the'
                                ' number of miles the car drives on full tank:')
        self.miles_entry = tkinter.Entry(self.miles_frame,width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        #Creating and packing widgets for bottom_frame
        self.calc_mpg_label = tkinter.Label(self.bottom_frame,text='MPG = ')
        self.calc_value = tkinter.StringVar()   #to associate the next label
        self.display_label = tkinter.Label(self.bottom_frame,
                                           textvariable=self.calc_value)

        self.calc_mpg_label.pack(side='left')
        self.display_label.pack(side='left')

        #Creating and packing widgets for button_frame
        self.calc_mpg_button = tkinter.Button(self.button_frame,
                        text='Calcuate MPG',command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.button_frame,text='Quit',
                                          command=self.main_window.destroy)

        self.calc_mpg_button.pack(side='left')
        self.quit_button.pack(side='left')

        #packing the frames
        self.header_frame.pack()
        self.gallon_frame.pack()
        self.miles_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()

        #calling the mainloop
        tkinter.mainloop()

    #The Cal_mpg method is a call back for the Calculate MPG button
    def calc_mpg(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        MPG = float(format((miles / gallons),'.2f'))
     
        self.calc_value.set(MPG)

mpg = MPG()
        
        
