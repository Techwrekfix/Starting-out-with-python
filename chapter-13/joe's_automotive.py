#This GUI ia a Checkbutton program which allows
#a user to select maintenance services

import tkinter

class MaintenanceService:
    def __init__(self):
        #Creat the root widget
        self.main_window = tkinter.Tk()

        #Create three frames to hold widgets
        self.header_frame = tkinter.Frame()
        self.services_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.quit_frame = tkinter.Frame()

        #Create six IntVar Objects to use with the check buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        #Set the IntVar object to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        #Create and pack widgets to the header_frame
        self.header_label = tkinter.Label(self.header_frame,
                                    text='Select a Service(s)')
        self.header_label.pack()

        #Create and pack widgets to the serives_frame
        self.oil_change = tkinter.Checkbutton(self.services_frame,
                        text='Oil change--$30.00',variable=self.cb_var1)
        self.lube_job = tkinter.Checkbutton(self.services_frame,
                        text='Lube job--$20.00',variable=self.cb_var2)
        self.radiator_flush = tkinter.Checkbutton(self.services_frame,
                text='Radiator flush--$40.00',variable=self.cb_var3)
        self.trans_flush = tkinter.Checkbutton(self.services_frame,
                text='Transmission flush--$100.00',variable=self.cb_var4)
        self.inspection = tkinter.Checkbutton(self.services_frame,
                        text='Inspection--$35.00',variable=self.cb_var5)
        self.muffler_rep = tkinter.Checkbutton(self.services_frame,
                text='Muffler replacement--$200.00',variable=self.cb_var6)
        self.tire_rotation = tkinter.Checkbutton(self.services_frame,
                text='Tire rotation--$20.00',variable=self.cb_var7)

        self.oil_change.pack()
        self.lube_job.pack()
        self.radiator_flush.pack()
        self.trans_flush.pack()
        self.inspection.pack()
        self.muffler_rep.pack()
        self.tire_rotation.pack()

        #Create and pack widgets for the bottom_frame
        self.total_button = tkinter.Button(self.bottom_frame,
                            text='Total Charge(s) =',command=self.calc_total)
        #Associating a label widget with the Total charges button
        self.total = tkinter.StringVar()
        self.total_label = tkinter.Label(self.bottom_frame,
                                         textvariable=self.total)
        self.total_button.pack(side='left')
        self.total_label.pack(side='left')
        #Create and pack the quit frame
        self.quit_button = tkinter.Button(self.quit_frame,text='Quit',
                                    command=self.main_window.destroy)
        
        self.quit_button.pack()

        #Pack the frames
        self.header_frame.pack()
        self.services_frame.pack()
        self.bottom_frame.pack()
        self.quit_frame.pack()

        #Call the mainloop
        tkinter.mainloop()

    #The calc_total method is a call back
    #function for the Total Charge button
    def calc_total(self):
        #Initialize a total accumulator
        self.value = 0.0

        #Determine which checkbuttons are selected and
        #build the total accordingly
        if self.cb_var1.get() == 1:
            self.value += 30.00 
        if self.cb_var2.get() == 1:
            self.value += 20.00
        if self.cb_var3.get() == 1:
            self.value += 40.00
        if self.cb_var4.get() == 1:
            self.value += 100.00
        if self.cb_var5.get() == 1:
            self.value += 35.00
        if self.cb_var6.get() == 1:
            self.value += 200.00
        if self.cb_var7.get() == 1:
            self.value += 20.00

        #Display the self.value total in a label
        self.total.set('$'+ str(self.value))

automotive = MaintenanceService()

        
