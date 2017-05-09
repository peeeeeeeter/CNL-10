
import tkinter as tk
import copy
from random import shuffle

#ToDo :  punish


class Banker:
    valid_colors = ['red', 'blue', 'green', 'black']

    def __init__(self):
        all_cards = [Card(j+1, self.valid_colors[i%4]) for _ in range(2) for i in range(4) for j in range(4)]
        all_cards.append(Card(1, 'red', True))
        all_cards.append(Card(2, 'red', True))

        shuffle(all_cards)
        self.all_card_list = CardList(cards=all_cards, owner='banker')

        self.public_table = [[] for _ in range(4)]
        self.try_table = [[] for _ in range(4)]
        self.temp_save_talbe = []

    def send_one_card(self, user):
        try:
            card =  self.all_card_list.cards.pop()

        except Exception:
            raise Exception("Run out of card.")
        # Directly modify user's card list
        user.card_list.cards.append(card)
        user.card_list.cards.sort(key=lambda x:(x.is_special, x.color, x.number))
        return card

    def send_initial_cards(self, num_to_send=14, user):
        to_send = [self.all_card_list.cards.pop() for i in range(num_to_send)]
        to_send.sort(key=lambda x: (x.is_special, x.color, x.number))
        to_send_card_list = CardList(cards=to_send, owner=user.name)
        # Directly modify the user's card list
        user.card_list = to_send_card_list
        return to_send_card_list

    def receive_card(self, line, position, card):
        self.try_table[line].insert(position, card)
        temp_card_list = CardList(cards=self.try_table[line], owner="public")
        return temp_card_list


    def put_to_temp_table(self, line, position):
        try:
            card = self.try_table[line].pop(position)
        except Exception:
            raise Exception("No such card")
        self.temp_save_talbe.append(card)
        return card

    def select_from_temp_table(self, index, line, position):
        try:
            card = self.temp_save_talbe.pop(index)
        except Exception:
            raise Exception("No such card")
        self.try_table[line].insert(position, card)
        return card

    def check_and_update(self, is_First=False):
        if self.temp_save_talbe:
            result = {
                "valid": False,
                "reason": "Temp table not empty."
            }
            return result

        for i in self.try_table:
            card_list = CardList(cards=[card for c in self.try_table[i]], owner="public")
            response = card_list.is_valid(is_First=is_First)
            if response["valid"] == False:
                return response

        # Need deep copy
        self.public_table = copy.deepcopy(self.temp_save_talbe)
        result = {
            "valid": True,
            "reason": "Valid"
        }
        return result

    def check_line_valid(self, line, is_First=False):
        card_list = CardList(cards=[card for c in self.try_table[line]], owner="public")
        response = card_list.is_valid(is_First=is_First)
        return response

    def start_game(self, users):
        sent_cards = []
        for i in users:
            sent_cards.append(self.send_initial_cards(owner_name=i).cards)
        return sent_cards



    def accept_command(self, command, **kwargs):
        pass

    def display_table(self, cards_on_desk):
        for i in cards_on_desk:
            print(i)
        return cards_on_desk




class User:
    def __init__(self, name, card_list):
        self.name = name
        self.card_list = card_list
        self.is_first = True


    pass

class Card:
    def __init__(self, number, color, is_speical=False):
        self.color = color
        self.number = number
        self.is_special = is_speical

    pass

class CardList:
    break_ice = 39
    max_card_num = 13
    valid_colors = ['red', 'blue', 'green', 'black']

    def __init__(self, cards, owner='banker'):
        # cards is a list of cards
        self.cards = cards
        self.owner = owner

    def is_valid(self, is_First=False):
        unused_color = ['red', 'blue', 'green', 'black']
        first_card = self.cards[0]
        second_card = self.cards[1]
        num_sum = 0
        is_same_number = False
        is_same_color = False

        result = {}
        if first_card.color == second_card.color:
            is_same_color = True
        if first_card.number == second_card.number:
            is_same_number = True

        if self.owner != 'public':
            result["valid"] = True
            result["reason"] = "Not public"
            return result
        elif len(self.cards) < 3:
            result["valid"] = False
            result["reason"] = "Too short"
            return result
        else:
            for index, card in enumerate(self.cards):
                if card.number > self.max_card_num or card.number < 0:
                    result["valid"] = False
                    result["reason"] = "The number is not valid."
                    return result
                if card.color not in self.valid_colors:
                    result["valid"] = False
                    result["reason"] = "The color is not valid."
                    return result
                if index > 1:
                    if is_same_color:
                        if prev.number != card.number-1:
                            result["valid"] = False
                            result["reason"] = "The card has wrong number."
                            return result
                        elif prev.color != card.color:
                            result["valid"] = False
                            result["reason"] = "The card has wrong color."
                            return result
                    elif is_same_number:
                        if prev.color in unused_color:
                            unused_color.remove(prev.color)
                        if prev.number != card.number:
                            result["valid"] = False
                            result["reason"] = "The card has wrong number, same color."
                            return result
                        try:
                            unused_color.remove(card.color)
                        except Exception:
                            result["valid"] = False
                            result["reason"] = "The color repeated in illegal way."
                            return result
                    else:
                        result["valid"] = False
                        result["reason"] = "The color and number are both wrong."
                        return result
                num_sum += card.number
                prev = card
            if is_First and num_sum < self.break_ice:
                result["valid"] = False
                result["reason"] = "Number sum is less than {}.".format(self.break_ice))
                return result
        result["valid"] = True
        result["reason"] = "Valid"
        return result

