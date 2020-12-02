from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='git.png').subsample(3)
image = Label(master = root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=('Courier', 13), text='Olá galerinha do youtube')
text.pack(side=BOTTOM)
root.mainloop()
