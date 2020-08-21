"""
Given a list of Car objects that have a 'color' attribute, transfrom that list into a dictionary with the colors as the keys and a list of the objects with that color as the values.
car.color
=> "blue"


input:
=> [blue_car, green_car1, yellow_car, green_car2]

output:
=> {
       "blue": [blue_car],
       "yellow": [yellow_car],
       "green": [green_car1, green_car2]
   }
"""

# class Car(object):
#     def __init__(self, color, name):
#         self.color = color
#         self.name = name
#         # print(object)
        
#     def get_name(self):
#         return self.name
    
#     def get_color(self):
#         return self.color
    
#     # def __str__(self):
#     #     return self

# blue_car = Car('blue', 'blue_car')
# green_car1 = Car('green', 'green_car1')
# yellow_car = Car('yellow', 'yellow_car')
# green_car2 = Car('green', 'green_car2')

# input = [blue_car, green_car1, yellow_car, green_car2]

# def make_a_dict(input):
#     result = {}
#     # print(input)
#     for car in input:
#         # print(car.__name__)
#         color = car.get_color()
#         name = car.get_name()

#         if color in result:
#             result[color].append(name)
#         else:
#             result[color] = [name]
#     print(result)
    
# make_a_dict(input)



# How would you implement the following code?
# one().plus().two().equals() #=> 3

# To simplify, only implement the numbers 1 and 2 and the operations "equals" and "plus"

# Your code here

# class Number():
    



# def one():
#     return Number(1)

# def two():
#     return 2

# class Number():
#     def __init__(self, number):
#         self.number = number
        
#     def plus(self):
#         temp_str = str(self.number) + '+'
#         return Calculate(temp_str)
        
#     def equals(self):
#         return int(self.number)
        
        
# class Calculate():
#     def __init__(self, string):
#         self.string = string
    
#     def two(self):
#         temp = None
#         ans = None
        
#         for digit in self.string:
#             if digit == '+':
#                 print(digit)
#                 ans = int(temp) + 2
                
#             elif 0 <= int(digit) <= 9:
#                 temp = digit
#         print(temp)
        
            
#         print(ans)
#         return Number(ans)

        
#         # do somethign
        
        
    
# # Test case to satisfy
# print(one().plus().two().equals() == 3)


# 1+

# Blackjack
# 2 people: Player & Dealer
# Played with standard deck of cards
# Each person gets dealt 2 initial cards
# Player is then given the chance to "hit" or "stand"
# Once player stands, the dealer draws cards until their sum goes over 17
# Hit means you draw another card
# Stand stops you drawing cards
# Goal: get as close to 21 as possible without going over
# If you go over, you lose
# Card Values: Face Cards (Jacks, Queens, Kings) are worth 10
# Aces worth 1


class Game:
    def __init__(self):
        pass
    
    def player_won(self, player):
        if player.calculate_sum() > 21:
            print('dealder won')
            return False
        elif player.calculate_sum() == 21:
            # is_playing = False
            # return 'player won'
            return True
        
    def decide_winner(self, player, dealer):
        player_sum = player.calculate_sum()
        dealer_sum = dealer.calculate_sum()
        return player_sum > dealer_sum
        
        
    
    def start_game(self):
        deck = Deck()
        deck.shuffle()
        is_playing = True
        
        player = Player()
        dealer = Player(player = False)
        for card in deck.give_two_initial_cards();
            player.get_card(card)
        
        for card in deck.give_two_initial_cards();
            dealer.get_card(card)
            
            
        if dealer.calculate_sum() == 21:
            is_playing = False
            return 'dealer won'
        
        elif dealder.calculate_sum() > 21:
            is_playing = False
            return 'player won'
        
        # dealer's sum is less than 21
        if player.calculate_sum() > 21:
            is_playing = False
            return 'dealder won'
        elif player.calculate_sum() == 21:
            is_playing = False
            return 'player won'
        
            
        while(is_playing):
            if player.hit_or_stand(deck):
                if player_won(player):
                    is_playing = False
                
                else:
                    pass
                
            while(dealer.calculate_sum() < 17):
                dealer.draw_card()
            
            if decide_winner() :
                print('Player won')
            else:
                print('Dealer won')
            is_playing = False
                
        
        
        
class Player:
    def __init__(self, player = None):
        if player:
            self.player = True
        else:
            self.player = False
        self.cards = []
    
    def get_cards(self, card):
        self.cards.append(card)
    
    def get_initial_cards(self):
        pass

    def hit_or_stand(self, deck):
        # ask player hit or stand
        hit = False
        
        if hit:
            card = deck.give_another_card()
            self.cards.append(card)
        else:
            pass
        
        return hit
                  
    def draw_card(self, deck):
        card = deck.give_another_card()
        self.cards.append(card)
            
    def calculate_sum(self):
        sum = 0
        for card in cards:
            sum += card.get_value()
        
        return sum    
        
    
class Card:
    def __init__(self, number, value):
        self.number = number
        if self.number == 'Jack' or 'Queens' or 'Kings':
            self.value = 10
        else:
            self.value = int(self.number)
            
    def get_value(self):
        return self.value
            
class Deck:
    def __init__(self):
        self.cards = []
    
    def shuffle(self):
        # do something
    
    
    def give_two_initial_cards(self):
        return (self.cards.pop(), self.cards.pop())
    
    def give_another_card(self):
        return self.cards.pop()

            
            

        
        
    
    
