from tkinter import *
from Shapes import *

class GUI:
    def __init__(self, window):

        self.window = window

            # Circle label and radius entry

        self.frame_circ = Frame(self.window)
        self.label_circ = Label(self.frame_circ, text='Circle')
        self.entry_circ = Entry(self.frame_circ)
        #self.entry_circ.insert(0, 'Enter Radius')
        #self.entry_circ.bind('<FocusIn>', self.temp_text_circ)
        self.label_circ.pack(padx=5, side='left')
        self.entry_circ.pack(padx=21, side='left')
        self.frame_circ.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

            # Square label and side entry

        self.frame_sq = Frame(self.window)
        self.label_sq = Label(self.frame_sq, text='Square')
        self.entry_sq = Entry(self.frame_sq)
        self.label_sq.pack(padx=5, side='left')
        self.entry_sq.pack(padx=15, side='left')
        self.frame_sq.pack(anchor='w', pady=10)

            # Rectangle label and variable entry (length, width)

        self.frame_rect = Frame(self.window)
        self.label_rect = Label(self.frame_rect, text='Rectangle')
        self.entry_rect_len = Entry(self.frame_rect)
        self.entry_rect_wid = Entry(self.frame_rect)
        self.label_rect.pack(padx=4, side='left')
        self.entry_rect_len.pack(padx=2, side='left')
        self.entry_rect_wid.pack(padx=10, side='left')
        self.frame_rect.pack(anchor='w', pady=10)

            # Triangle label and variable entry (base, height)

        self.frame_tri = Frame(self.window)
        self.label_tri = Label(self.frame_tri, text='Triangle')
        self.entry_tri_base = Entry(self.frame_tri)
        self.entry_tri_height = Entry(self.frame_tri)
        self.label_tri.pack(padx=9, side='left')
        self.entry_tri_base.pack(padx=2, side='left')
        self.entry_tri_height.pack(padx=10, side='left')
        self.frame_tri.pack(anchor='w', pady=10)

            # Calculate button

        self.frame_bottom = Frame(self.window)
        self.button_calc = Button(self.frame_bottom, text='CALCULATE', command=self.clicked)
        self.button_calc.pack()
        self.frame_bottom.pack()

            # Clear button

        self.frame_clear = Frame(self.window)
        self.button_clear = Button(self.frame_clear, text='CLEAR', command=self.clear)
        self.button_clear.pack()
        self.frame_clear.pack()

    #def temp_text_circ(self):
        #self.entry_circ.delete(0, END)

    def clicked(self):
        global circ, sq, rect_length, rect_width, tri_base, tri_height
        try:
            circ = int(self.entry_circ.get())
        except ValueError:
            print('not integer')

        try:
            sq = int(self.entry_sq.get())
        except ValueError:
            print('not integer')

        try:
            rect_length = int(self.entry_rect_len.get())
        except ValueError:
            print('not integer')

        try:
            rect_width = int(self.entry_rect_wid.get())
        except ValueError:
            print('not integer')

        try:
            tri_base = int(self.entry_tri_base.get())
        except ValueError:
            print('not integer')

        try:
            tri_height = int(self.entry_tri_height.get())
        except ValueError:
            print('not integer')
        #circ = self.entry_circ.get()
        #sq = self.entry_sq.get()
        #rect_length = self.entry_rect_len.get()
        #rect_width = self.entry_rect_wid.get()
        #tri_base = self.entry_tri_base.get()
        #tri_height = self.entry_tri_height.get()

        c = Circle(circ)
        self.entry_circ = c.circ_area()
        s = Square(sq)
        self.entry_sq = s.sq_area()
        r = Rectangle(rect_length, rect_width)
        self.entry_rect_len = r.rect_area()
        t = Triangle(tri_base, tri_height)
        self.entry_tri_base = t.tri_area()


    def clear(self):
        self.entry_circ.delete(0, END)
        self.entry_sq.delete(0, END)
        self.entry_rect_len.delete(0, END)
        self.entry_rect_wid.delete(0, END)
        self.entry_tri_base.delete(0, END)
        self.entry_tri_height.delete(0, END)
