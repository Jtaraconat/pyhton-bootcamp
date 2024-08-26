from tkinter import *

window = Tk()

window.title("first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
#my_label.pack() #can change side to left right top or bottom
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#for *args and **kwargs see playground.py




my_label["text"] = "New text" #can use my_label.config(text="New text")


#Button
def clicking():
    button.config(text="button got clicked")
    user_input = input.get()
    my_label.config(text=user_input)

button = Button(text="Click me", command=clicking)
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="new_button")
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)


#Other widgets in tkinter
#see appropriate file


#Tkinter layout pack, place, grid
#pack each widget next to other from top to bottom 
#place precise positionning specifying x and y 
#grid create a grid with rows and columns






#keep window open on screen and listen to user input
window.mainloop()
