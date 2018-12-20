#This GUI program calcualtes assement value
#and property tax of a property

import tkinter

class Property:
    def __init__(self):
        #Creating the root widget
        self.main_window = tkinter.Tk()

        #Creating four frames to handle widgets
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.quit_frame = tkinter.Frame()

        #Creating and packing widgets for top_frame
        self.value_label = tkinter.Label(self.top_frame,
                    text='Enter the actual vlaue of a property:')
        self.value_entry = tkinter.Entry(self.top_frame,width=10)

        self.value_label.pack(side='left')
        self.value_entry.pack(side='left')

        #Creating and packing widgets for the middle_frame
        self.asses_value = tkinter.Button(self.middle_frame,
                    text='Assesment Value',command=self.assesment_value)
        self.asses_string = tkinter.StringVar()
        self.asses_label = tkinter.Label(self.middle_frame,
                                         textvariable=self.asses_string)
        self.asses_value.pack(side='left')
        self.asses_label.pack(side='left')

        #Creating and packing widgets for the bottom_frame
        self.tax_value = tkinter.Button(self.bottom_frame,text='Property Tax',
                                          command=self.property_tax)
        self.tax_string = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.bottom_frame,
                                         textvariable=self.tax_string)
        self.tax_value.pack(side='left')
        self.tax_label.pack(side='left')

        #Creating and packing widget for the quit_frame
        self.quit_button = tkinter.Button(self.quit_frame,text='Quit',
                                          command=self.main_window.destroy)
        self.quit_button.pack()

        #Packing the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.quit_frame.pack()

        #Calling the mainloop
        tkinter.mainloop()

    #The assesment_value method is a call
    #back function for the Assesment Value button
    def assesment_value(self):
        self.assesment_entry = float(self.value_entry.get())
        self.assesment_value = format(0.6 * self.assesment_entry,',.2f')

        self.asses_string.set(self.assesment_value)

    #The property_tax method is a call
    #back function for the Property Tax button
    def property_tax(self):
        asses_entry = float(self.value_entry.get())
        asses_value = (0.6 * asses_entry)
        property_tax = format((asses_value * 0.75) / 100,',.2f')

        self.tax_string.set(property_tax)

prop = Property()
