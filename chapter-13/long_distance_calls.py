#This GUI Program displays charges
#for long distance calls

import tkinter
import tkinter.messagebox

class LongDistanceCalls:
    def __init__(self):
        #Calling the root widget
        self.main_window = tkinter.Tk()

        #Creating four frames to handle widgets
        self.header_frame = tkinter.Frame()
        self.category_frame = tkinter.Frame()
        self.input_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        #Creating and packing widget for header_frame
        self.header_label = tkinter.Label(self.header_frame,
                                          text='Long-Distance Calls')
        self.header_label.pack()

        #Creating an IntVar object to use with Radiobuttons
        self.radio_var = tkinter.IntVar()

        #Setting the IntVar Object to 1
        self.radio_var.set(0)

        #Creating and packing Radiobutton widgets into category_frame
        self.daytime = tkinter.Radiobutton(self.category_frame,
                        text='Daytime(6:00 A.M. through 5:59 p.m.)',
                variable=self.radio_var,value=1,command=self.day_charge)
        self.evening = tkinter.Radiobutton(self.category_frame,
                        text='Evening(6:00 p.m. through 11:59 p.m.)',
                variable=self.radio_var,value=2,command=self.evening_charge)
        self.off_peak = tkinter.Radiobutton(self.category_frame,
                         text='Off-Peak(Midnight through 5:59 a.m.)',
                variable=self.radio_var,value=3,command=self.off_peak_charge)

        self.daytime.pack()
        self.evening.pack()
        self.off_peak.pack()

        #Creating and packing widgets for the input_frame
        self.charge_label = tkinter.Label(self.input_frame,
                            text='Enter the number of call minutes:')
        self.charge_entry = tkinter.Entry(self.input_frame,width=10)

        self.charge_label.pack(side='left')
        self.charge_entry.pack(side='right')

        #Creating and packing widgets for the button_frame
        self.quit_button = tkinter.Button(self.button_frame,text='Quit',
                                          command= self.main_window.destroy)
        self.quit_button.pack()

        #Pack the frames
        self.header_frame.pack()
        self.category_frame.pack()
        self.input_frame.pack()
        self.button_frame.pack()

        #call the mainloop
        tkinter.mainloop()

    #The day_charge method is call back
    #function for Daytime calls
    def day_charge(self):
        if (self.charge_entry.get()) == '':
            tkinter.messagebox.showinfo('Call Charge',
                        'Please Enter number of minutes and select call plan')
        else:
            minute_entry = float(self.charge_entry.get())
            total_charge = format(minute_entry * 0.07,'.2f')

            tkinter.messagebox.showinfo('Call Charge',
            'Total charge for the call = $'+ str(total_charge))

    #The evening_charge is call back
    #function for evening calls
    def evening_charge(self):
        if (self.charge_entry.get()) == '':
            tkinter.messagebox.showinfo('Call Charge',
                        'Please Enter number of minutes and select call plan')
        else:
            minute_entry = float(self.charge_entry.get())
            total_charge = format(minute_entry * 0.12,'.2f')

            tkinter.messagebox.showinfo('Call Charge',
                            'Total charge for the call = $'+ str(total_charge))

    #The off_peak_charge is call back
    #function for off_peak calls
    def off_peak_charge(self):
        if (self.charge_entry.get()) == '':
            tkinter.messagebox.showinfo('Call Charge',
                        'Please Enter number of minutes and select call plan')
        else:
            minute_entry = float(self.charge_entry.get())
            total_charge = format(minute_entry * 0.05,'.2f')

            tkinter.messagebox.showinfo('Call Charge',
                            'Total charge for the call = $'+ str(total_charge))

calls = LongDistanceCalls()
