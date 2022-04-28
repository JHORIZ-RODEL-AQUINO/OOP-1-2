from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

# Creating a function code for changing color
i = 1
def change_color():
    global i
    i += 1
    if i % 2 == 0:
        btn.configure(bg="yellow")
    else:
        btn.configure(bg="white")


# Insert a Button Widget
btn = Button(window, text="Click to Change color", bg="white", height=10, width=30, command=change_color)
btn.place(relx=.5, rely=.5, anchor="center")

window.mainloop()