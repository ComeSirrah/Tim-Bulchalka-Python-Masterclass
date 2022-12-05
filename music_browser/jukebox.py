import sqlite3
# try:
import tkinter


# except ImportError:     # Python 2 import compatibility
#     import Tkinter as tkinter


def exercise(*args):
    lengths = []
    for arg in args:
        lengths.append(len(arg))
    return sum(lengths) / len(args)


def ex_2(*args):
    winner = args[0]
    comparison_index = 1
    for arg in args[:-1]:
        if winner < args[comparison_index]:
            winner = args[comparison_index]
            comparison_index += 1
        else:
            comparison_index += 1

    return winner


def ex_3(*args):
    backwards_args = []
    for arg in args[::-1]:
        backwards_word = ""
        for letter in arg[::-1]:
            backwards_word += letter
        backwards_args.append(backwards_word)
    solution = " ".join(backwards_args)
    print(solution)


# conn = sqlite3.connect('music.sqlite')
#
# window_main = tkinter.Tk()a
# window_main.title('Music DB Browser')
# window_main.geometry('1024x768')
#
# window_main.columnconfigure(0, weight=2)
# window_main.columnconfigure(1, weight=2)
# window_main.columnconfigure(2, weight=2)
# window_main.columnconfigure(3, weight=1)    # spacer column on right
#
# window_main.rowconfigure(0, weight=1)
# window_main.rowconfigure(1, weight=5)
# window_main.rowconfigure(2, weight=5)
# window_main.rowconfigure(3, weight=1)
#
# # ==== labels ====
# tkinter.Label(window_main, text='Artists').grid(row=0, column=0)
# tkinter.Label(window_main, text='Albums').grid(row=0, column=1)
# tkinter.Label(window_main, text='Songs').grid(row=0, column=2)
#
# # ==== artists field ====
# artist_list = tkinter.Listbox(window_main)
# artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
# artist_list.config(border=2, relief='sunken')
#
# artist_list_scrollbar = tkinter.Scrollbar(window_main, orient=tkinter.VERTICAL, command=artist_list.yview)
# artist_list_scrollbar.grid(row=1, column=0, sticky='nse', rowspan=2)
# artist_list['yscrollcommand'] = artist_list_scrollbar.set
#
# # ==== albums field ====
# album_list_variable = tkinter.Variable(window_main)
# album_list_variable.set(('Choose an artists',))
# albums_list = tkinter.Listbox(window_main, listvariable=album_list_variable)
# albums_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
# albums_list.config(border=2, relief='sunken')
#
# album_list_scrollbar = tkinter.Scrollbar(window_main, orient=tkinter.VERTICAL, command=albums_list.yview)
# album_list_scrollbar.grid(row=1, column=1, sticky='nse', rowspan=1)
# albums_list['yscrollcommand'] = album_list_scrollbar.set
#
# # ==== songs field ====
# songs_list_variable = tkinter.Variable(window_main)
# songs_list_variable.set(('Choose an album',))
# songs_list = tkinter.Listbox(window_main, listvariable=songs_list_variable)
# songs_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
# songs_list.config(border=2, relief='sunken')
#
# songs_list_scrollbar = tkinter.Scrollbar(window_main, orient=tkinter.VERTICAL, command=songs_list.yview)
# songs_list_scrollbar.grid(row=1, column=2, sticky='nse', rowspan=1)
# songs_list['yscrollcommand'] = songs_list_scrollbar.set
#
# # ==== main loop ====
# test_list = range(150)
# album_list_variable.set(tuple(test_list))
# window_main.mainloop()
# print("closing database connection")
# conn.close()


# print(ex_2(32, 5, 31, 32, 59, 77, 8, 10, 4, 91, 91, 8, 98, 37, 75, 10))


print(ex_3("This", "can", "be", "read", "backwards"))

