

# def deckgen():
#     value = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
#     suit = ['spades','clubs','diamonds','hearts']
#     suit_value = ['s','c','d','h']
#     i=0
#     j=0
#     card = ""
#     while i < 13:
#         while j < 4:
#             card = value[i] + "_of_" + suit[j]  + ' = ("' + value[i] + "_of_" + suit[j] + '",' + str(i) +',"'+suit_value[j]+'")'
#             # card = value[i] + "_of_" + suit[j]  + ","
#             print(card)
#             j+=1
#         j = 0
#         i+=1

# deckgen()

class Card():
    def __init__(self,name,value,suit) -> None:
        self.name = name
        self.value = value
        self.suit = suit

two_of_spades = Card("Two of Spades",2,"s")
two_of_clubs = Card("Two of Clubs",2,"c")
two_of_diamonds = Card("Two of Diamonds",2,"d")
two_of_hearts = Card("Two of Hearts",2,"h")
three_of_spades = Card("Three of Spades",3,"s")
three_of_clubs = Card("Three of Clubs",3,"c")
three_of_diamonds = Card("Three of Diamonds",3,"d")
three_of_hearts = Card("Three of Hearts",3,"h")
four_of_spades = Card("Four of Spades",4,"s")
four_of_clubs = Card("Four of Clubs",4,"c")
four_of_diamonds = Card("Four of Diamonds",4,"d")
four_of_hearts = Card("Four of Hearts",4,"h")
five_of_spades = Card("Five of Spades",5,"s")
five_of_clubs = Card("Five of Clubs",5,"c")
five_of_diamonds = Card("Five of Diamonds",5,"d")
five_of_hearts = Card("Five of Hearts",5,"h")
six_of_spades = Card("Six of Spades",6,"s")
six_of_clubs = Card("Six of Clubs",6,"c")
six_of_diamonds = Card("Six of Diamonds",6,"d")
six_of_hearts = Card("Six of Hearts",6,"h")
seven_of_spades = Card("Seven of Spades",7,"s")
seven_of_clubs = Card("Seven of Clubs",7,"c")
seven_of_diamonds = Card("Seven of Diamonds",7,"d")
seven_of_hearts = Card("Seven of Hearts",7,"h")
eight_of_spades = Card("Eight of Sades",8,"s")
eight_of_clubs = Card("Eight of Clubs",8,"c")
eight_of_diamonds = Card("Eight of Diamonds",8,"d")
eight_of_hearts = Card("Eight of Hearts",8,"h")
nine_of_spades = Card("Nine of Spades",9,"s")
nine_of_clubs = Card("Nine of Clubs",9,"c")
nine_of_diamonds = Card("Nine of Diamonds",9,"d")
nine_of_hearts = Card("Nine of Hearts",9,"h")
ten_of_spades = Card("Ten of Spades",10,"s")
ten_of_clubs = Card("Ten of Clubs",10,"c")
ten_of_diamonds = Card("Ten of Diamonds",10,"d")
ten_of_hearts = Card("Ten of Hearts",10,"h")
jack_of_spades = Card("Jack of Spades",11,"s")
jack_of_clubs = Card("Jack of Clubs",11,"c")
jack_of_diamonds = Card("Jack of Diamonds",11,"d")
jack_of_hearts = Card("Jack of Hearts",11,"h")
queen_of_spades = Card("Queen of Spades",12,"s")
queen_of_clubs = Card("Queen of Clubs",12,"c")
queen_of_diamonds = Card("Queen of Diamonds",12,"d")
queen_of_hearts = Card("Queen of Hearts",12,"h")
king_of_spades = Card("King of Spades",13,"s")
king_of_clubs = Card("King of Clubs",13,"c")
king_of_diamonds = Card("King of Diamonds",13,"d")
king_of_hearts = Card("King of Hearts",13,"h")
ace_of_spades = Card("Ace of Spades",14,"s")
ace_of_clubs = Card("Ace of Clubs",14,"c")
ace_of_diamonds = Card("Ace of Diamonds",14,"d")
ace_of_hearts = Card("Ace of Hearts",14,"h")

deck = [two_of_spades,
two_of_clubs,
two_of_diamonds,
two_of_hearts,
three_of_spades,
three_of_clubs,
three_of_diamonds,
three_of_hearts,
four_of_spades,
four_of_clubs,
four_of_diamonds,
four_of_hearts,
five_of_spades,
five_of_clubs,
five_of_diamonds,
five_of_hearts,
six_of_spades,
six_of_clubs,
six_of_diamonds,
six_of_hearts,
seven_of_spades,
seven_of_clubs,
seven_of_diamonds,
seven_of_hearts,
eight_of_spades,
eight_of_clubs,
eight_of_diamonds,
eight_of_hearts,
nine_of_spades,
nine_of_clubs,
nine_of_diamonds,
nine_of_hearts,
ten_of_spades,
ten_of_clubs,
ten_of_diamonds,
ten_of_hearts,
jack_of_spades,
jack_of_clubs,
jack_of_diamonds,
jack_of_hearts,
queen_of_spades,
queen_of_clubs,
queen_of_diamonds,
queen_of_hearts,
king_of_spades,
king_of_clubs,
king_of_diamonds,
king_of_hearts,
ace_of_spades,
ace_of_clubs,
ace_of_diamonds,
ace_of_hearts]

