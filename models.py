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
    self.break_ice = 39

    def __init__(self, cards, owner='desk'):
        self.cards = cards
        self.owner = owner

    def is_valid(self, is_First=False):
        prev = self.cards[0]
        num_sum = 0
        if self.owner != 'public':
            return (True, "Not public)"
        elif len(self.cards) < 3:
            return (False, "Too short")
        else:
            for index, card in enumerate(self.cards):
                if prev.color != card.color:
                    if prev.number != card.number:
                        return (False, card.number)

                else:
                    if prev.number != card.number -1 :
                        return (False, card.number)

                prev = card
                num_sum += card.number
            if is_First and num_sum < CardList.break_ice:
                return (False, "Less than break ice number")
            return (True, "All valid")

