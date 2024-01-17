import time
from random import choice
from the_hands import phand, chand
import index


#Resets the deck to noramal
def reset():
    x=0
    file = open('The_deck.py', 'w')
    file.write('Deck = [')
    while x <5:
        #Hearts
        if x == 0:
            for num in range(1, 15):
                if num <=10:
                    file.write('\''+str(num)+ ' of hearts\', ')
                if num == 11:
                    file.write('\'J of hearts\',')
                if num == 12:
                    file.write('\'Q of hearts \',')
                if num == 13:
                    file.write('\'K of hearts\',')
                if num == 14:
                    file.write('\'A of hearts\',')
        #Spades
        if x == 1:
            for num in range(1, 15):
                if num <=10:
                    file.write('\''+str(num)+ ' of spades\', ')
                if num == 11:
                    file.write('\'J of spades\',')
                if num == 12:
                    file.write('\'Q of spades \',')
                if num == 13:
                    file.write('\'K of spades\',')
                if num == 14:
                    file.write('\'A of spades\',')
        #Clovers
        if x == 2:
            for num in range(1, 15):
                if num <=10:
                    file.write('\''+str(num)+ ' of clovers\', ')
                if num == 11:
                    file.write('\'J of clovers\',')
                if num == 12:
                    file.write('\'Q of clovers \',')
                if num == 13:
                    file.write('\'K of clovers\',')
                if num == 14:
                    file.write('\'A of clovers\',')
        #Diamonds
        if x == 3:
            for num in range(1, 15):
                if num <= 10 :
                    file.write('\''+str(num)+ ' of diamonds \', ')
                if num == 11:
                    file.write('\'J of diamonds\',')
                if num == 12:
                    file.write('\'Q of diamonds \',')
                if num == 13:
                    file.write('\'K of diamonds\',')
                if num == 14:
                    file.write('\'A of diamonds\']')
        x+=1
    file.close()




    #Gets the starting hand for bolth the player and computer
def pick_card():
    #Randomly chooses card from deck for player 

    pcard_1=choice(Deck)
    phand.append(pcard_1)
    Deck.remove(phand[0])
    pcard_2=choice(Deck)
    phand.append(pcard_2)
    Deck.remove(phand[1])


    #Randomly chooses random card for computer
    Ccard_1=choice(Deck)
    chand.append(Ccard_1)
    Deck.remove(chand[0])
    Ccard_2=choice(Deck)
    chand.append(Ccard_2)
    Deck.remove(chand[1])

    print('\n\nYour cards are:')
    print('Your First Card is '+phand[0])
    print('Your Second Card is '+phand[1])
    print('\n')
    print('The Dealers faceup card is: \n'+chand[0])
    print('\n\n')



#Counts the players points
def player_points():

    ppoints = 0 #player points
    card = 0 #itration variable 
    card_number = 1 #itration variable 


    # adds the the players cards togehter to check the points 
    

    #Looks at the first card
    while card< len(phand):
        while card_number<11:
            if str(card_number) in phand[card]:
                ppoints+=card_number
                break
            elif 'J' in phand[card] or 'Q' in phand[card] or 'K' in phand[card]:
                ppoints+= 10
                break
            elif 'A' in phand[card]:
                ppoints+=11
            card_number+=1
        card_number = 1
        card+=1

    return ppoints

def Dealer_Point_Counter():
    Dealer_Points = 0 #Computers points
    card = 0 #itration variable 
    card_number = 1 #itration variable 


    # adds the the Dealers cards togehter to check the points 
    

    while card< len(chand):
        while card_number<=10:
            if str(card_number) in chand[card]:
                Dealer_Points+=card_number
                break
            elif 'J' in chand[card] or 'Q' in chand[card] or 'K' in chand[card] or 'A' in chand[card]:
                Dealer_Points+= 10
                break
            card_number+=1
        card_number = 1
        card+=1

    return Dealer_Points





def hit():
    aditional_card=choice(Deck)
    phand.append(aditional_card)
    current = len(phand)
    current -= 1
    Deck.remove(phand[current])
    i = 0
    print('Your Hand\n')
    while i < len(phand):
        print(phand[i])
        i+=1
    print('\nYour points:')
    print(player_points())
    print('\n\n')

def Dealer_Hit():
    print('\nDealer Hits')
    aditional_card=choice(Deck)
    chand.append(aditional_card)
    current = len(chand)
    current -= 1
    Deck.remove(chand[current])

    print('\nDealers hand:\n')
    i = 0
    while i < len(chand):
        print(chand[i])
        i +=1
    print('\nDealers points:')
    print(Dealer_Point_Counter())





def game():
    Dealer_Win = False
    Player_Win = False
    push = False
    pick_card()
    print('Your Points: '+ str(player_points()))
    is_running = True
    while is_running:
        while Dealer_Win == False and Player_Win == False and push == False:
            if player_points() < 22:
                Hit_Stand = input('Do you want to Hit or Stand?: ')
                if Hit_Stand == "Hit":
                    print('You chose to hit\n')
                    hit()
                elif Hit_Stand == "Stand":
                    print('You chose to stand\n')
                    print('\nDealers Turn')
                    print("Dealers Points: "+ str(Dealer_Point_Counter()))
                    dealer_turn = True
                    while dealer_turn:
                        if Dealer_Point_Counter() < player_points():
                            Dealer_Hit()
                            if Dealer_Point_Counter() > player_points() and Dealer_Point_Counter() < 22:
                                dealer_turn = False
                                Dealer_Win = True
                            if Dealer_Point_Counter() == player_points():
                                print('Push')
                                dealer_turn = False
                                Dealer_Win = True
                            if Dealer_Point_Counter() > 21:
                                print("Dealer Bust, You win")
                                dealer_turn = False
                            if Dealer_Win == True:
                                break
                        if Dealer_Point_Counter() == player_points():
                            push = True
                            break
                        if Dealer_Point_Counter() > player_points() and Dealer_Point_Counter()<22:
                            print(Dealer_Point_Counter())
                            Dealer_Win = True
                            break
                        if Dealer_Point_Counter()>22:
                            Player_Win = True
                            break


            
            elif player_points() > 21:
                Dealer_Win = True
        if Dealer_Win == True:
            print('\n\nGame over, Dealer win\n\n')
            is_running = False
        if Player_Win == True:
            print('\n\nYou Win, Good Job\n\n')
            is_running = False
        if push == True:
            print('Push, Noone Wins\n\n')
            is_running = False

x = 0
reset()
from The_deck import Deck as new_Deck
Deck = new_Deck
Star_Events, Start_Values = index.start_window.read()
restar_loop = True
while restar_loop:
    Start_Events, Start_Values = index.start_window.read()
    if Start_Events == 'Start':
        index.start_window.close()
        game()
        x+=1
    if Start_Events in (index.pys.WIN_CLOSED, 'Exit'):
        break

print('end program')