import random
import tkinter


def load_cards(card_images):
    suits = ['heart', 'club', 'spade', 'diamond']
    face_cards = ['jack', 'queen', 'king']
    extension = 'png'

    # for each suit retrieve the image for the cards
    for suit in suits:
        # first the number cards
        for card in range(1, 11):
            name = f'./cards_png/cards/{str(card)}_{suit}.{extension}'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = f'./cards_png/cards/{str(card)}_{suit}.{extension}'
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    # pop a card from the deck
    next_card = deck.pop(0)
    # add image to a label and display them
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def first_deal():
    global dealer_score, player_score
    card_value = deal_card(dealer_card_frame)[0]
    if card_value == 1:
        dealer_score += 11
        if dealer_score > 21:
            dealer_score -= 10
    else:
        dealer_score += card_value
    dealer_score_label.set(dealer_score)

    card_value = deal_card(player_card_frame)[0]
    if card_value == 1:
        player_score += 11
        if player_score > 21:
            player_score -= 10
    else:
        player_score += card_value

    card_value = deal_card(player_card_frame)[0]
    if card_value == 1:
        player_score += 11
        if player_score > 21:
            player_score -= 10
    else:
        player_score += card_value
    player_score_label.set(player_score)

    if player_score == 21:
        result_text.set("Blackjack! Player wins!")


def deal_dealer():
    global dealer_score
    while 0 < dealer_score < 17:
        card_value = deal_card(dealer_card_frame)[0]
        dealer_card_amount = []
        dealer_card_amount.append(card_value)
        dealer_blackjack = len(dealer_card_amount)
        if card_value == 1:
            dealer_score += 11
            if dealer_score > 21:
                dealer_score -= 10
        else:
            dealer_score += card_value
        dealer_score_label.set(dealer_score)
        if dealer_score == 21:
            if dealer_blackjack == 2:
                result_text.set("Blackjack! Dealer wins!")
        elif dealer_score > 21:
            result_text.set("Player wins!")
        elif dealer_score > player_score:
            result_text.set("Dealer wins!")
        elif dealer_score < player_score:
            result_text.set("Player wins!")
        elif dealer_score == player_score:
            result_text.set("Tie!")


def deal_player():
    global player_score
    card_value = deal_card(player_card_frame)[0]
    if card_value == 1:
        player_score += 11
        if player_score > 21:
            player_score -= 10
    else:
        player_score += card_value
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer wins!")


def new_game():
    global cards, deck, dealer_card_frame, player_card_frame, dealer_score, player_score

    dealer_card_frame.destroy()
    player_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    player_hand.clear()
    dealer_hand.clear()
    deck.clear()
    deck = list(cards)
    random.shuffle(deck)
    dealer_score = 0
    player_score = 0
    dealer_score_label.set(dealer_score)
    player_score_label.set(player_score)
    result_text.set("Welcome to the table!")


main_window = tkinter.Tk()
# set up screen and frame for dealer and player

main_window.title('Blackjack')
main_window.geometry('2160x1440')
main_window.config(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2, )

dealer_score_label = tkinter.IntVar()
dealer_score = 0
tkinter.Label(card_frame, text='Dealer', background='green', foreground='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text='Player', background='green', foreground='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', foreground='white').grid(row=3,
                                                                                                        column=0)
# embedded frame to hold the player card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

start_button = tkinter.Button(button_frame, text='Start game', command=first_deal)
start_button.grid(row=0, column=0)

dealer_finish_button = tkinter.Button(button_frame, text='Try your luck', command=deal_dealer)
dealer_finish_button.grid(row=0, column=2)

player_button = tkinter.Button(button_frame, text='Hit', command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=1, column=0, columnspan=3, sticky='ew')

player_score = 0
cards = []
load_cards(cards)

# create a new deck of cards and shuffle it
deck = list(cards)
random.shuffle(deck)

# create the list to sort the dealer's and player's hands
dealer_hand = []
player_hand = []

result_text.set("Welcome to the table!")

main_window.mainloop()
