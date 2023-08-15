from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.configure(background = "green")

root.minsize(650,650)
root.maxsize(650,650)


open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
    


file_name_label = Label(root, text = "File Name")
file_name_label.place(relx = 0.35, rely = 0.2, anchor = CENTER)

file_input = Entry(root)
file_input.place(relx = 0.42, rely = 0.2, anchor = CENTER)

text_area = Text(root, height = 80, width = 30)
text_area.place(relx = 0.5, rely = 0.3, anchor = CENTER)