from ShapesGUI import *


def main():

    window = Tk()
    window.title('Area of Shapes')
    window.geometry('300x300')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()