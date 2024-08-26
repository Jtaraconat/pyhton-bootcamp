from tkinter import *

def convert():
    miles = user_entry.get()
    result = int(miles ) * 1.609
    result_label.config(text=result)


window = Tk()
window.title("Miles to Kms converter")
window.config(padx=20, pady=20)

user_entry = Entry()
user_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kms_label = Label(text="Kms")
kms_label.grid(row=1, column=2)
   

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)












window.mainloop()