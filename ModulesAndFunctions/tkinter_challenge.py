import tkinter

main_window = tkinter.Tk()

# initialize and pad main window
main_window.title("Calculator")
main_window.geometry('1080x720+200+500')
main_window['padx'] = 8

# add results UI widget
results = tkinter.Entry(main_window)
results.grid(row=0, column=0,)

# add button frame to calculator UI
button_frame = tkinter.Frame(main_window)
button_frame.grid(row=1, column=0, sticky='we')
button_frame.config(border=2, relief='sunken')

# add Clear and CE buttons to top left button positions
clear_button = tkinter.Button(button_frame, text='C')
clear_button.config(border=3, relief='raised')
clear_button.grid(row=0, column=0)
CE_button = tkinter.Button(button_frame, text='CE')
CE_button.config(border=3, relief='raised')
CE_button.grid(row=0, column=1)

# map number buttons
BUTTON_LIST = [1,2,3,'*',4,5,6,'-',7,8,9,'+']
BUTTON_LIST_BOTTOM = [0, '=', '/' ]
change = 0
loop_row = 4
loop_column = 0
for i in BUTTON_LIST:
    button = tkinter.Button(button_frame, text=f"{i}")
    button.config(border=3, relief='raised')
    button.grid(row=loop_row, column=loop_column)
    loop_column += 1
    if loop_column > 3:
        loop_column = 0
        loop_row -= 1
loop_column = 0
for i in BUTTON_LIST_BOTTOM:
    button = tkinter.Button(button_frame, text=f"{i}")
    button.config(border=3, relief='raised')
    if i == '=':
        button.grid(row=5, column=loop_column, columnspan=2, sticky='ew')
    elif i == '/':
        loop_column += 1

    button.grid(row=5, column=loop_column)
    loop_column += 1

main_window.mainloop()
