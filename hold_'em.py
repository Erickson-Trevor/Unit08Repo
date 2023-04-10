import random as r
import deck as d
import sys

def turn(starting_position):
    global pot
    global bet
    round_boolean = True
    player_response_boolean = True
    p = starting_position
    j = 0
    while round_boolean == True:
        while p < 6:
            while j < len(players):
                if player.position == p and player.fold == False:
                    while player_response_boolean == True:
                        print("")
                        print("It's your turn!")
                        player_response_boolean = player_response()
                elif players[j].position == p and players[j].fold == False:
                    non_player_response(j)
                j+=1
            j=0
            p+=1
        p=0
        i = 0
        round_boolean = False
        while i < 6:
            if players[i].ante<bet and players[i].fold == False:
                o = True
                i += 1
            else:
                i += 1
        print('')
        print("The pot is " + str(pot))
        print("The ante is " + str(bet))
        print('')

def player_response():
    if player.ante < bet and player.fold == False:
        print('You can either CALL, RAISE, or FOLD')
    elif player.ante == bet and player.fold == False:
        print("You can either CHECK, RAISE, or FOLD")
    response = input("")
    if response == "CALL":
        call_response()
        return False
    elif response == "RAISE":
        raise_response(response)
        return False
    elif response == "CHECK":
        check_response()
        return False
    elif response == "FOLD":
        fold_response()
        return False
    else:
        print('Command not recognized. Please try again.')
        return True

def check_response():
    if player.ante != bet:
        print("You cannot check this turn.")
    else:
        print("You've checked this turn.")

def raise_response(response):
    while True:
        response = flexible_response("How much would you like to raise?","int")
        if int(response) > bet:
            player.player_bet(int(response))
            print("You've raised " + response)
            break
        else:
            print("Please enter a number higher than", bet)
    
def call_response():
    player.player_bet(bet)
    print("You've called " + str(bet))

def fold_response():                            
    player.fold = True
    print("You've folded this turn!")

def flexible_response(prompt,data_type):
    print(prompt)
    while True:
        print()
        response = input()
        quit(response)
        
        if str(type(response)) == data_type:
            return response
        elif response.isdigit() == True:
            return response
        else:
            print("Invalid input! Please type a " + data_type)
    
def non_player_response(j):
    if r.randint(0,14) == 0:
        players[j].fold = True
        print(players[j].name + " has folded.")
    elif r.randint(0,9) == 0:
        players[j].player_bet(bet+100)
        print(players[j].name + " raised to " + str(players[j].ante))
    elif players[j].ante < bet:
        players[j].player_bet(bet)
        print(players[j].name + " called.")
    elif players[j].ante == bet:
        print(players[j].name + " checked.")

class Player():

    def __init__(self,name,card1,card2,chips,position,fold,ante) -> None:
        self.name = name
        self.card1 = card1
        self.card2 = card2
        self.chips = chips
        self.position = position
        self.fold = fold
        self.ante = ante

    def player_bet(self,value_of_bet):
        global pot
        global bet
        pot -= self.ante
        self.chips -= int(value_of_bet) - self.ante
        self.ante = int(value_of_bet)
        pot += self.ante
        bet = self.ante

    def show_cards(self):
        print(self.card1.name)
        print(self.card2.name)

def deal_community_cards():
    global community_cards
    community_cards = []
    i=0
    while i < 5:
        community_cards.append(deal_card())
        i+=1

def quit(response):
    if response == 'END':
        sys.exit()

def intialize(): 
    print("Hello! Welcome to Texas Hold'em.")
    print('You are playing against 5 others to win.')
    print('Type "BEGIN" to get started. Type "END" at any time to exit the program')

    # Creating each character from the Player class, 
    # and making a list to connect and access them in a while loop.

    while True:
#        response = input()
        response = 'BEGIN'
        print('')
        quit(response)
        if response == "BEGIN":
            global player 
            player = Player('Player',0,0,10000,0,False,0)
            global ben 
            ben = Player('Ben',0,0,10000,1,False,0)
            global joe 
            joe = Player('Joe',0,0,10000,2,False,0)
            global samuel 
            samuel = Player('Samuel',0,0,10000,3,False,0)
            global rob 
            rob = Player('Rob',0,0,10000,4,False,0)
            global peter
            peter = Player('Peter',0,0,10000,5,False,0)
            global pot 
            pot = 0
            global players
            players = [player,ben,joe,samuel,rob,peter]

            # Radomizing each players' postiion; 
            # every time you start there will be a new big and small blind.

            i=0
            position_list = [0,1,2,3,4,5]
            while i<6:
                players[i].position = position_list[i]
                i+=1
            break
        else:
            print('')
            print("Invalid Input!")
            print('Try again.')
            print('')
        
def deal_card():
    global deck
    card = deck[r.randint(0,len(deck)-1)]
    deck.remove(card)
    return card

def preflop():
    global pot
    global bet
    global players
    global deck

    deck = d.deck
    print('PREFLOP')


    # Dealing cards to each player

    j=0
    while j<6:
        players[j].card1 = deal_card()
        players[j].card2 = deal_card()
        j+=1

    print('Your cards are: ')
    player.show_cards()

    deal_community_cards()

    if player.position == 0:
        print("You are the small blind!")
        ante = flexible_response("Type in your bet.", "int")
        player.player_bet(ante)
    else:
        i=0
        while True:
            x = players[i].position
            if x == 0:
                break
            i+=1
        players[i].player_bet(100)
        print('')
        print('The small blind is ' + players[i].name)

    if player.position == 1:
        print("You are the big blind! Your bet will be twice the small blind.")
        player.player_bet(bet*2)
    else:
        i = 0
        while True:
            x = players[i].position
            if x == 1:
                break
            i+=1
        print(players[i].name + " is the big blind!")
        players[i].player_bet(bet * 2)
    
    turn(2)

def flop():
    global community_cards
    print("The flop is: ")
    i=0
    while i < 3:
        print(community_cards[i].name)
        i+=1
    print('')
    turn(0)

def river1():
    global community_cards
    print("The community cards are: ")
    i=0
    while i < 4:
        print(community_cards[i].name)
        i+=1
    print('')
    turn(0)

def river2():
    global community_cards
    print("The community cards are: ")
    i=0
    while i < 5:
        print(community_cards[i].name)
        i+=1
    print('')
    turn(0)

def calculate_hand(card1,card2):

    global community_cards
    d = community_cards
    d.append(card1,card2)

    pair = check_pair(d)
    two_pair = check_pair(d)
    three_of_a_kind = check_three_of_a_kind(d)
    flush = check_flush(d)
    straight = check_straight(d)[0]
    straight_flush = check_straight_flush(d)
    royale_flush = check_royale_flush(d)


def check_flush(d):
    flush_list = [0,0,0,0]
    for card in d:
        if card.suit == 's':
            flush_list[0] += 1
        elif card.suit == 'c':
            flush_list[1] += 1
        elif card.suit == 'd':
            flush_list[2] += 1
        elif card.suit == 'h':
            flush_list[3] += 1
    flush_list.sort()
    if flush_list[0] > 4:
        return True
    else:
        return False

def check_straight(d):
    potentional_straight = False
    straight_list = []

    for compare_card in d:
        card = 2
        for contrast_card in d:
            if compare_card.value == contrast_card.value:
                continue
            elif compare_card.value - contrast_card.value == 1 or -1:
                straight_list.append(contrast_card)
                potentional_straight = True

    if potentional_straight == True:
        for compare_card in d:
            if compare_card == straight_list[0] or compare_card == straight_list[len(straight_list)-1]:
                continue
            elif compare_card.value - straight_list[0].value == -1:
                straight_list.insert(0,compare_card)
            elif compare_card.value - straight_list[len(straight_list)-1] == 1:
                straight_list.append(compare_card)
    if len(straight_list) > 4:
        straight_list.insert(0,True)
    else:
        straight_list.insert(0,False)
    return straight_list
    
def check_pair(d):
    pair_count = 0
    for compare_card in d:
        for contrast_card in d:
            if compare_card == contrast_card:
                continue
            elif compare_card.value == contrast_card.value:
                pair_count += 1
                continue
    if pair_count < 1:
        return False
    else:
        return True

def check_two_pair(d):
    pair_count = 0
    for compare_card in d:
        for contrast_card in d:
            if compare_card == contrast_card:
                continue
            elif compare_card.value == contrast_card.value:
                pair_count += 1
                continue
    if pair_count < 5:
        return False
    else:
        return True          

def check_three_of_a_kind(d):
    for compare_card in d:
        for contrast_card in d:
            if compare_card == contrast_card:
                continue
            elif compare_card.value == contrast_card.value:
                for contest_card in d:
                    if contest_card == compare_card or contest_card == contrast_card:
                        continue
                    elif contest_card.value == compare_card.value:
                        return True
    return False

def check_straight_flush(d):
    if check_straight(d)[0] == True and check_flush(d) == True:
        return True
    else:
        return False

def check_royale_flush(d):
    if check_straight_flush(d) == True:
        if check_straight(d)[1].value == 10:
            return True

def showdown():
    global pot
    global bet
    global players

    print("Show your cards!")
    for player in players:
        if player.fold == False:
            print(player.name + "'s cards are the", player.card1.name, 'and the', player.card2.name)
    i=0
    winner = []

        

    if len(winner) > 1:
        print("It's a tie! The winners are:")
        for player in winner:
            print(player)
    else:
        print("The winner is " + winner[0].name)
        winner[0].chips += pot

    pot = 0
    bet = 0

    i = 0
    while i > len(players):
        players[i].postion += 1
        if players[i].postion == len(players):
            players[i].postion = 0
        i+=1

    while True:
        print("Would you like to play again?")
        print("PLAY AGAIN or END")
        response = input("")
        if response == 'PLAY AGAIN':
            players
            return True
        elif response == 'END':
            quit(response)
        else:
            print('Invalid Input! Please try again.')
            print('')


        
    

def main():
    intialize()
    game_end_boolean = False
    while game_end_boolean == False:
        preflop()
        flop()
        river1()
        river2()
        game_end_boolean = showdown()
        break


    

main()