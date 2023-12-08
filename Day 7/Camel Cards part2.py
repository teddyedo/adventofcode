from operator import itemgetter


card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10,
               '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.card_occurencies = {}
        self.bet = bet
        self.rank = 0
        self.calculate_cards_occurencies()
        self.calculate_rank()

    def __str__(self):
        return f"Cards: {self.cards} Bet: {self.bet} Rank: {self.rank} Occurencies: {self.card_occurencies}"

    def calculate_cards_occurencies(self):
        jokers = 0
        for card in self.cards:
            if card == "J":
                jokers += 1
            else:
                if card in self.card_occurencies:
                    self.card_occurencies[card] += 1
                else:
                    self.card_occurencies[card] = 1
                    
        if jokers > 0 and jokers < 5:
            sorted_cards = sorted(self.card_occurencies.items(), key=lambda item: (item[1], card_values[item[0]]), reverse=True)
            # print(sorted_cards[])
            self.card_occurencies[sorted_cards[0][0]] += jokers
        elif jokers == 5:
            self.card_occurencies["J"] = 5

    def calculate_rank(self):
        if 5 in self.card_occurencies.values():
            self.rank = 7
        elif 4 in self.card_occurencies.values():
            self.rank = 6
        elif 3 in self.card_occurencies.values() and 2 in self.card_occurencies.values():
            self.rank = 5
        elif 3 in self.card_occurencies.values():
            self.rank = 4
        elif list(self.card_occurencies.values()).count(2) == 2:
            self.rank = 3
        elif 2 in self.card_occurencies.values():
            self.rank = 2
        else:
            self.rank = 1


def order_hands(hands):
    return sorted(hands, key=lambda hand: (hand.rank, card_values[hand.cards[0]], card_values[hand.cards[1]],
                                           card_values[hand.cards[2]], card_values[hand.cards[3]], card_values[hand.cards[4]]), reverse=True)


hands = []

with open('input.txt', 'r') as file:
    for line in file:
        row = line.split()
        hands.append(Hand(row[0], int(row[1])))

hands = order_hands(hands)

bet_value = 1000
total_bet = 0

for hand in hands:
    total_bet += bet_value * hand.bet
    bet_value -= 1

print(total_bet)
