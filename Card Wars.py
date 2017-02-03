import random


def function():
    name = input("Hello, what is your username going to be?:")
    computer = "computer"
    decksize = input("Hello and welcome to card wars what kind of deck size are you going to play with 3,6,10 or 13?:")
    if decksize == '3' or decksize == '6' or decksize == '10' or decksize == '13':
        print("Ok so you are going to play with a deck size of", (decksize),"...cool.")
        player = input("Would you like to play with another person or with the computer?(person,computer):")
        if player == 'person':
            nametwo = input("Ok so you are going to play with another person. What will his/her username be?:")
            print("Welcome", (nametwo))
            if decksize == '3':
                namecard = random.randint(1,3)
                print("Ok", name,"your card is", namecard)
                nametwocard = random.randint(1,3)
                print("Ok", nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    print(name,"wins!")
                elif namecard == nametwocard:
                    print("It's a tie!")
                else:
                    print(nametwo,"wins!")
            elif decksize == '6':
                namecard = random.randint(1,6)
                print("Ok", name,"your card is", namecard)
                nametwocard = random.randint(1,6)
                print("Ok", nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    print(name,"wins!")
                elif namecard == nametwocard:
                    print("It's a tie!")
                else:
                    print(nametwo,"wins!")
            elif decksize == '10':
                namecard = random.randint(1,10)
                print("Ok", name,"your card is", namecard)
                nametwocard = random.randint(1,10)
                print("Ok", nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    print(name,"wins!")
                elif namecard == nametwocard:
                    print("It's a tie!")
                else:
                    print(nametwo,"wins!")


            elif decksize == '13':
                namecard = random.randint(1,13)
                print("Ok", name,"your card is", namecard)
                nametwocard = random.randint(1,13)
                print("Ok", nametwo,"your card is", nametwocard)
                if namecard > nametwocard:
                    print(name,"wins!")
                elif namecard == nametwocard:
                    print("It's a tie!")
                else:
                    print(nametwo,"wins!")
    
             


        
        elif player == 'computer':
            print("Why are you not playing with any of your friends? Are you lonely? If so, call this number for a night of fu-... Nevermind have fun with the computer nerd.")
            if decksize == '3':
                namecard = random.randint(1,3)
                print("Ok", name,"your card is", namecard)
                computercard = random.randint(1,3)
                print("Ok the computers card is", computercard)
                if namecard > computercard:
                    print(name,"wins!")
                elif namecard == computercard:
                    print("It's a tie!")
                else:
                    print("Computer wins!")
            elif decksize == '6':
                namecard = random.randint(1,6)
                print("Ok", name,"your card is", namecard)
                computercard = random.randint(1,6)
                print("Ok the computers card is", computercard)
                if namecard > computercard:
                    print(name,"wins!")
                elif namecard == computercard:
                    print("It's a tie!")
                else:
                    print("Computer wins!")
            elif decksize == '10':
                namecard = random.randint(1,10)
                print("Ok", name,"your card is", namecard)
                computercard = random.randint(1,10)
                print("Ok the computers card is", computercard)
                if namecard > computercard:
                    print(name,"wins!")
                elif namecard == computercard:
                    print("It's a tie!")
                else:
                    print("Computer wins!")

            elif decksize == '13':
                namecard = random.randint(1,13)
                print("Ok", name,"your card is", namecard)
                computercard = random.randint(1,13)
                print("Ok the computers card is", computercard)
                if namecard > computercard:
                    print(name,"wins!")
                elif namecard == computercard:
                    print("It's a tie!")
                else:
                    print("Computer wins!")
        playagain = input("Do you want to play again?:")
        if playagain == 'yes':
            function()
        
        
function()

