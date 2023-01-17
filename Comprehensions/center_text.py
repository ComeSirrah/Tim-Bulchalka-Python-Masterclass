def center_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"
    text = "-".join([str(arg) for arg in args])
    left_margin = 80 - len(text) // 2
    print(' ' * left_margin, text)


center_text("This is centered text.")