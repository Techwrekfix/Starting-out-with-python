#This program displays a name and address
#when a button is clicked.

import tkinter

class MyDetails:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Creating two frames to contains widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #Creating and packing widget into top_frame
        self.string = tkinter.StringVar()  #TO associate the label widget
        self.top_label = tkinter.Label(self.top_frame,
                                       textvariable=self.string)
        self.top_label.pack()

        #Creating and packing widget into button frame
        self.show_info_button = tkinter.Button(self.button_frame,
                                               text='Show Info',
                                               command=self.show_info)
        self.quit_button = tkinter.Button(self.button_frame,text='Quit',
                                          command=self.main_window.destroy)
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        #Packing the frames
        self.top_frame.pack()
        self.button_frame.pack()
        
        #Calling the mainloop
        tkinter.mainloop()

    #The show_info method is a callback function
    #for the Show Info button
    def show_info(self):
        self.string.set('Kwabena Yeboah\n'
                        '274 Baily Drive\n'
                        'Waynesville, NC 2799')
        
my_details = MyDetails()
