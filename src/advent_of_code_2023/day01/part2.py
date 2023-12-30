from advent_of_code_2023.utils import read_input

word_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_digit(line: str, forward: bool) -> str:
    indices = range(len(line))
    if not forward:
        indices = reversed(indices)
    for i in indices:
        if line[i].isdigit():
            return line[i]
        for word, number in word_map.items():
            if line[i::].startswith(word):
                return number
    raise ValueError('Could not find a digit.')

def line_to_calibration_value(line: str):
    return int(get_digit(line, forward=True) + get_digit(line, forward=False))


def sum_calibration_document(document: list[str]):
    return sum(line_to_calibration_value(line) for line in document)


if __name__ == '__main__':
    print(sum_calibration_document(read_input(day=1)))