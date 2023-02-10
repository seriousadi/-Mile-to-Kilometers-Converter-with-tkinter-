from tkinter import *

screen = Tk()
screen.grid()

label = Label(text="is equals to")
label.grid(row=3, column=1)

input = Entry(width=20)
input.grid(row=2,column=2)

label2 = Label(text= "Miles")
label2.grid(row=2, column=3)

label3 = Label()
label3.grid(row=3, column=2)

label4 = Label(text="KM")
label4.grid(row=3, column=3)

def converter():
    some = float(input.get()) * 1.609
    label3.config(text= round(some))


button = Button(text="Calculate", command=converter)
button.grid(row=4, column=2)





screen.mainloop()
