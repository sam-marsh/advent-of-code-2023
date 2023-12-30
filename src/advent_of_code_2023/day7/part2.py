from advent_of_code_2023.utils import read_input

power = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': -1,
    'Q': 10,
    'K': 11,
    'A': 12,
}

def kind(card: str) -> int:
    frequencies = {}
    for c in card:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    
    if 'J' in frequencies:
        j_count = frequencies['J']
        if j_count == 5:
            return 0
        best_option = max(
            (c for (c, f) in frequencies.items() if c != 'J'),
            key=lambda x: (frequencies[x], power[x])
        )
        del frequencies['J']
        frequencies[best_option] += j_count
    if len(frequencies) == 1:
        return 0 # five of a kind
    if len(frequencies) == 2:
        for c, freq in frequencies.items():
            if freq == 1:
                return 1 # four of a kind
            if freq == 2:
                return 2 # full house
    if len(frequencies) == 3:
        for c, freq in frequencies.items():
            if freq == 3:
                return 3 # three of a kind
            if freq == 2:
                return 4 # two pair
    if len(frequencies) == 4:
        return 5 # one pair
    return 6 # high card

# sorting function from weakest to strongest
def compare(card1, card2):
    if card1 == card2:
        return 0
    k1, k2 = kind(card1), kind(card2)
    if k1 < k2:
        # first card more powerful
        return 1
    if k1 > k2:
        # second card more powerful
        return -1
    for c1, c2 in zip(card1, card2):
        if power[c1] > power[c2]:
            # first card more powerful
            return 1
        if power[c1] < power[c2]:
            # second card more powerful
            return -1
    raise AssertionError()

from functools import cmp_to_key

def solve(lines: list[str]) -> int:
    card_bids = []
    for line in lines:
        split = line.strip().split(' ')
        card_bids.append((split[0], int(split[1])))
    for card, _ in card_bids:
        print(card, kind(card))
    card_bids = sorted(card_bids, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
    
    return sum(a[1] * (b + 1) for a, b in zip(card_bids, range(len(card_bids))))

if __name__ == "__main__":
    print(solve(read_input(day=7)))