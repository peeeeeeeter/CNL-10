import unittest

from models import Card, CardList, User

#ToDo : send cards, withdraw card, initial_send card tests
class CardListTest(unittest.TestCase):

    def setUp(self):
        self.max_num = 13
        self.valid_color = ['red', 'blue', 'black', 'green']

    def test_check_valid_same_number_different_colors(self):
        cards = [
            Card(1, 'red'), Card(1, 'blue'), Card(1, 'black'), Card(1, "green")
        ]
        card_list = CardList(cards, "public")

        expect_response = (True, "Valid")

        response = card_list.is_valid()
        self.assertEqual(response, expect_response)

    def test_check_valid_same_number_duplicate_colors(self):
        cards = [
            Card(1, "red"), Card(1, "blue"), Card(1, "green"), Card(1, "black"), Card(1, "green")
        ]
        card_list = CardList(cards, "public")

        expect_response = (False, "The color repeated in illegal way.")

        response = card_list.is_valid()
        self.assertEqual(response, expect_response)

    def test_check_valid_smae_number_same_colors(self):
        cards = [
            Card(1, "red"), Card(1, "red"), Card(1, "red"), Card(1, "red")
        ]
        card_list = CardList(cards, "public")

        expect_response = (False, "The card has wrong number.")

        resposne = card_list.is_valid()
        self.assertEqual(resposne, expect_response)


    def test_check_valid_same_color_correct_sequence(self):
        cards = [
            Card(1, 'red'), Card(2, 'red'), Card(3, 'red'), Card(4, 'red')
        ]
        card_list = CardList(cards, "public")

        expect_response = (True, "Valid")

        response = card_list.is_valid()
        self.assertEqual(response, expect_response)

    def test_check_valid_same_color_wrong_sequence(self):
        cards = [
            Card(1, 'red'), Card(2, 'red'), Card(3, 'red'), Card(5, 'red')
        ]
        card_list = CardList(cards, "public")

        expect_response = (False, "The card has wrong number.")

        response = card_list.is_valid()
        self.assertEqual(response, expect_response)

    def test_check_valid_not_same_color_valid_sequence(self):
        pass

    def test_check_valid_not_same_color_invalid_sequence(self):
        pass

    def test_check_valid_number_lt_zero(self):
        pass

    def test_check_valid_number_gt_max(self):
        pass

    def test_check_valid_invalid_color(self):
        pass
