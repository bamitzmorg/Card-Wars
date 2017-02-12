import random
import time

name = input("Hello, what is your username going to be?:")
#computer = "computer" is a variable 
computer = "computer"
decksize = input("Hello and welcome to card wars what kind of deck size are you going to play with 3,6,10 or 13?:")
#if decsize == '3' or decksize == '6' or decksize == '10' or decksize =='13' is an if statement
if decksize == '3' or decksize == '6' or decksize == '10' or decksize == '13':
    print("You are going to play with a deck size of", (decksize),"...That's cool I guess...")
#def function(): is a function          
def function():
        player = input("Would you like to play with another person or with the computer?(person,computer):")
        if player == 'person':
            time.sleep(1)
            nametwo = input("So you are going to play with another person, what will his/her username be?:")
            time.sleep(1)
            print("Welcome", (nametwo))
            if decksize == '3':
                namecard = random.randint(1,3)
                time.sleep(1)
                print(name,"your card is", namecard)
                nametwocard = random.randint(1,3)
                time.sleep(1)
                print(nametwo,"your card is", nametwocard)
                # if namecard > nametwocard: is a comparative operator
                if namecard > nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(nametwo,"wins!")
            elif decksize == '6':
                namecard = random.randint(1,6)
                time.sleep(1)
                print(name,"your card is", namecard)
                nametwocard = random.randint(1,6)
                time.sleep(1)
                print(nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(nametwo,"wins!")
            elif decksize == '10':
                namecard = random.randint(1,10)
                time.sleep(1)
                print(name,"your card is", namecard)
                nametwocard = random.randint(1,10)
                time.sleep(1)
                print(nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(nametwo,"wins!")
            elif decksize == '13':
                namecard = random.randint(1,13)
                time.sleep(1)
                print(name,"your card is", namecard)
                nametwocard = random.randint(1,13)
                time.sleep(1)
                print(nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == nametwocard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(nametwo,"wins!")
        elif player == 'computer':
            print("Why are you not playing with any of your friends? Are you lonely? If so, call this number for a night of fu-... Nevermind have fun with the computer nerd.")
            if decksize == '3':
                namecard = random.randint(1,3)
                time.sleep(1)
                print(name,"your card is", namecard)
                computercard = random.randint(1,3)
                time.sleep(1)
                print("The computers card is", computercard)
                if namecard > computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")      
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("Computer wins!")
            elif decksize == '6':
                namecard = random.randint(1,6)
                time.sleep(1)
                print(name,"your card is", namecard)
                computercard = random.randint(1,6)
                time.sleep(1)
                print("The computers card is", computercard)
                if namecard > computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("Computer wins!")
            elif decksize == '10':
                namecard = random.randint(1,10)
                time.sleep(1)
                print(name,"your card is", namecard)
                computercard = random.randint(1,10)
                time.sleep(1)
                print("The computers card is", computercard)
                if namecard > computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                elif namecard == computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("Computer wins!")
            elif decksize == '13':
                namecard = random.randint(1,13)
                time.sleep(1)
                print(name,"your card is", namecard)
                computercard = random.randint(1,13)
                time.sleep(1)
                print("The computers card is", computercard)
                if namecard > computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print(name,"wins!")
                elif namecard == computercard:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    print("It's a tie!")
                else:
                    for x in range(0, 3):
                        time.sleep(1)
                        print("...")
                    time.sleep(1)
                    print("Computer wins!")
        time.sleep(1)
        playagain = input("Do you wish to play again?:")
        if playagain == 'yes':
            function()
        else:
            time.sleep(1)
            print("Hope you had a great time playing this boring game. But if you do want to have a night of fun call this nu... Nevermind goodbye!")
        
function()
