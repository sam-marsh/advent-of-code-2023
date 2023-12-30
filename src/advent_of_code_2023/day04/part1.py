from advent_of_code_2023.utils import read_input


def count_value(lines: list[str]):
    t = 0
    for line in lines:
        winningstr, havestr = line.split(':')[1].strip().split('|')
        print(winningstr, havestr)
        winning_numbers = set(int(x) for x in winningstr.strip().split(' ') if x is not '')
        have_numbers = [int(x) for x in havestr.strip().split(' ') if x is not '']
        card_value = 0
        for n in have_numbers:
            if n in winning_numbers:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        t += card_value
    return t

if __name__ == "__main__":
    print(count_value(read_input(day=4)))