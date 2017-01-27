import random

name = input("Hello, what is your username going to be?:")

decksize = input("Hello and welcome to card wars what kind of deck size are you going to play with 3,6,10 or 13?:")
if decksize == '    3' or decksize == '6' or decksize == '10' or decksize == '13':
    print("Ok so you are going to play with a deck size of", (decksize),"cool.")
    player = input("Would you like to play with another person or with the computer?(person,computer):")
    if player == 'person':
        nametwo = input("Ok so you are going to play with another person. What will his/her username be?:")
        print("Welcome", (nametwo))
    elif player == 'computer':
        print("Have fun with the computer.")
     



