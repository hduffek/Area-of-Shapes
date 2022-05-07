from ShapesGUI import *


def main():

    window = Tk()
    window.title('Area of Shapes')
    window.geometry('500x350')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()