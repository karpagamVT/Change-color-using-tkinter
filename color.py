import tkinter as tk
def red_colour():
    window['bg']='green'
def green_colour():
    window['bg']='coral'
def blue_colour():
    window['bg']='blue'
window=tk.Tk()
menubar=tk.Menu(window)
dropdown_menu=tk.Menu(menubar)
dropdown_menu.add_command(label='green',command=red_colour)
dropdown_menu.add_command(label='coral',command=green_colour)
dropdown_menu.add_command(label='Blue',command=blue_colour)
menubar.add_cascade(label='color',menu=dropdown_menu)
window.config(menu=menubar)
window.mainloop()
