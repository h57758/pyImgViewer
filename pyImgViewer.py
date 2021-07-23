from tkinter import *
from PIL import ImageTk,Image
import tkinter.filedialog, tkinter, sys

# Console info
progversion = '1.0.0'

print('Python Image Viewer  v' + progversion)
print('----Made by UnBeatWater----')
print('===========================')


class Window(Frame):
# Menu Commands
    def closeProgram(self):
        print('Closing...')
        sys.exit()

    def openImage(self):
           media = tkinter.filedialog.askopenfilename()
           print('Image loaded: ' + media)

           load = Image.open(media)
           render = ImageTk.PhotoImage(load)

           img = Label(self, image=render)

           img.configure(bg='black')
           img.image = render
           img.place(x=0, y=0)
           print('Image displayed')

# Window Class
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.configure(bg='black')

        self.pack(fill=BOTH, expand=1)


    # Menus
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Open", command=self.openImage)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.closeProgram)
        menu.add_cascade(label="File", menu=fileMenu)

    # Main UI

root = Tk()
app = Window(root)

# set window properties
root.geometry("640x480")
root.wm_title("Python Image Viewer")

# show window
root.mainloop()