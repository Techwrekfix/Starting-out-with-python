#This GUI program translates latin to english

import tkinter

class LatinTranslator:
    def __init__(self):
        #Calling the root widget
        self.main_window = tkinter.Tk()

        #Creating six frames to handle widgets
        self.header_frame = tkinter.Frame(self.main_window)
        self.line_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.quit_frame = tkinter.Frame(self.main_window)

        #Creating and packing widgets for header frame
        self.latin_label = tkinter.Label(self.header_frame,text='Latin')
        self.english_label = tkinter.Label(self.header_frame,text='\tEnglish')

        self.latin_label.pack(side='left')
        self.english_label.pack(side='right')

        #Creating and packing line frame
        self.line_label = tkinter.Label(self.line_frame,
                                        text='-----------------------')
        self.line_label.pack()

        #Creating and packing widgets for top frame
        self.sinister_button = tkinter.Button(self.top_frame,text='sinister',                                              command=self.sinister)
        self.sinister_string = tkinter.StringVar()  #To associate the label with
        self.sinister_label = tkinter.Label(self.top_frame,
                                            textvariable=self.sinister_string)

        self.sinister_button.pack(side='left')
        self.sinister_label.pack()

        #Creating and packing widgets for middle_frame
        self.dexter_button = tkinter.Button(self.middle_frame,text='dexter',                                              command=self.dexter)
        self.dexter_string = tkinter.StringVar()  #To associate the label with
        self.dexter_label = tkinter.Label(self.middle_frame,
                                            textvariable=self.dexter_string)

        self.dexter_button.pack(side='left')
        self.dexter_label.pack()

        #Creating and packing widgets for bottom_frame
        self.medium_button = tkinter.Button(self.bottom_frame,text='medium',
                                              command=self.medium)
        self.medium_string = tkinter.StringVar()  #To associate the label with
        self.medium_label = tkinter.Label(self.bottom_frame,
                                            textvariable=self.medium_string)

        self.medium_button.pack(side='left')
        self.medium_label.pack()

        #Creating and packing widget for quit frame
        self.quit_button = tkinter.Button(self.quit_frame,text='Quit',
                                          command=self.main_window.destroy)
        
        self.quit_button.pack()

        #Pack the frames
        self.header_frame.pack()
        self.line_frame.pack()
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.quit_frame.pack()

        #call the mainloop
        tkinter.mainloop()

    #The sinister method is a call
    #back fucntion for sinister button
    def sinister(self):
        self.sinister_string.set('\tleft')

    #The dexter method is a call back
    #fucntion for dexter button
    def dexter(self):
        self.dexter_string.set('\tright')

    #The medium method is a call back
    #function for the medium button
    def medium(self):
        self.medium_string.set('\tcenter')

latin_translator = LatinTranslator()
        
