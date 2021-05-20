# making of a GUI for a chat bot



# libraries
from tkinter import *

# initializing the parent
root = Tk()

# Give the window a title
root.title("Chat Bot")

# giving the geometry
root.geometry("400x500")

# creating of a sub menu
file_menu = Menu(root)
file_menu.add_command(label = "New")
file_menu.add_command(label = "Save as")
file_menu.add_command(label = "Exit")

# creating a main menu bar
main_menu = Menu(root)

main_menu.add_cascade(label = "File", menu = file_menu)
main_menu.add_command(label = "Edit")
main_menu.add_command(label = "Quit")
root.config(menu = main_menu)

# creating of a chat window

chatWindow = Text(root, bd = 1, bg = "pink", width = 50, height = 8)
chatWindow.place(x = 6, y = 6, height = 385, width = 370)

# creating a window for messaging
messageWindow = Text(bg = "pink", width = 30, height = 4)
messageWindow.place(x = 120, y = 400, height= 80, width = 260)

# adding of a button
Button = Button(root, text = "Send", bg = "light blue", activebackground = "light green", width = 12, height = 5, font = ("Arial", 12))
Button.place(x =6, y =400, height = 80, width = 120)

# adding a scroll bar
scrollbar = Scrollbar(root,command = chatWindow.yview())
scrollbar.place( x= 375, y = 5, height = 385, )




root.mainloop()