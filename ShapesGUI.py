from tkinter import *
from Shapes import *

class GUI:
    def __init__(self, window):

        self.window = window

            # Circle label and radius entry

        self.frame_circ = Frame(self.window)
        self.label_circ = Label(self.frame_circ, text='Circle')
        self.label_rad = Label(self.frame_circ, text='Radius')
        self.label_circ_area = Label(self.frame_circ, text='')
        self.entry_circ = Entry(self.frame_circ)

        self.label_circ.pack(padx=5, side='top')
        self.label_rad.pack(padx=5, side='left')
        self.entry_circ.pack(padx=6, side='left')
        self.label_circ_area.pack(padx=5, side='left')
        self.frame_circ.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

            # Square label and side entry

        self.frame_sq = Frame(self.window)
        self.label_sq = Label(self.frame_sq, text='Square')
        self.label_side = Label(self.frame_sq, text='Side')
        self.label_sq_area = Label(self.frame_sq, text='')
        self.entry_sq = Entry(self.frame_sq)

        self.label_sq.pack(padx=5, side='top')
        self.label_side.pack(padx=6, side='left')
        self.entry_sq.pack(padx=15, side='left')
        self.label_sq_area.pack(padx=5, side='left')
        self.frame_sq.pack(anchor='w', pady=10)

            # Rectangle label and variable entry (length, width)

        self.frame_rect = Frame(self.window)
        self.label_rect = Label(self.frame_rect, text='Rectangle')
        self.label_len = Label(self.frame_rect, text='Length')
        self.label_wid = Label(self.frame_rect, text='Width')
        self.label_rect_area = Label(self.frame_rect, text='')
        self.entry_rect_len = Entry(self.frame_rect)

        self.entry_rect_wid = Entry(self.frame_rect)

        self.label_rect.pack(padx=4, side='top')
        self.label_len.pack(padx=5, side='left')
        self.entry_rect_len.pack(padx=2, side='left')
        self.label_wid.pack(padx=5, side='left')
        self.entry_rect_wid.pack(padx=10, side='left')
        self.label_rect_area.pack(padx=5, side='left')
        self.frame_rect.pack(anchor='w', pady=10)

            # Triangle label and variable entry (base, height)

        self.frame_tri = Frame(self.window)
        self.label_tri = Label(self.frame_tri, text='Triangle')
        self.label_base = Label(self.frame_tri, text='Base')
        self.label_height = Label(self.frame_tri, text='Height')
        self.label_tri_area = Label(self.frame_tri, text='')
        self.entry_tri_base = Entry(self.frame_tri)

        self.entry_tri_height = Entry(self.frame_tri)

        self.label_tri.pack(padx=9, side='top')
        self.label_base.pack(padx=9, side='left')
        self.entry_tri_base.pack(padx=5, side='left')
        self.label_height.pack(padx=3, side='left')
        self.entry_tri_height.pack(padx=10, side='left')
        self.label_tri_area.pack(padx=5, side='left')
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


    def clicked(self):
        global circ, sq, rect_length, rect_width, tri_base, tri_height
        try:
            circ = int(self.entry_circ.get())
            sq = int(self.entry_sq.get())
            rect_length = int(self.entry_rect_len.get())
            rect_width = int(self.entry_rect_wid.get())
            tri_base = int(self.entry_tri_base.get())
            tri_height = int(self.entry_tri_height.get())
        except ValueError:
            print('not integer')

        c = Circle(circ)
        self.label_circ_area = Label(self.frame_circ, text=(c.circ_area()))
        self.label_circ_area.pack()
        s = Square(sq)
        self.label_sq_area = Label(self.frame_sq, text=(s.sq_area()))
        self.label_sq_area.pack()
        r = Rectangle(rect_length, rect_width)
        self.label_rect_area = Label(self.frame_rect, text=(r.rect_area()))
        self.label_rect_area.pack()
        t = Triangle(tri_base, tri_height)
        self.label_tri_area = Label(self.frame_tri, text=(t.tri_area()))
        self.label_tri_area.pack()


    def clear(self):
        self.label_circ_area.destroy()
        self.label_sq_area.destroy()
        self.label_rect_area.destroy()
        self.label_tri_area.destroy()

