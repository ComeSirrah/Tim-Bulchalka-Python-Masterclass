import tkinter
#
#
#
#
main_window = tkinter.Tk()

main_window.title("Hello World")
main_window.geometry('1080x720-8-200')

label = tkinter.Label(main_window, text="Hello World")
label.grid(row=0, column=1)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)
right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky='n')

button_1 = tkinter.Button(right_frame, text='Button 1')
button_2 = tkinter.Button(right_frame, text='Button 2')
button_3 = tkinter.Button(right_frame, text='Button 3')
button_1.grid(row=0, column= 0)
button_2.grid(row=1, column=0)
button_3.grid(row=2, column=0)
# configure the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=1)
right_frame.config(relief='sunken', borderwidth=1)
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')

right_frame.columnconfigure(0, weight=1)
button_1.grid(sticky='ew')
button_2.grid(sticky='ew')
button_3.grid(sticky='ew')
main_window.mainloop()
