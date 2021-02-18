x = 0
cards_rank = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14,

}

count = 0
my_cards = [input() for _ in range(6)]
for card in my_cards:
    count += cards_rank.get(card)

print(count / 6)
