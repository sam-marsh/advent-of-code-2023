from advent_of_code_2023.utils import read_input


def line_to_calibration_value(line: str):
    first_digit = next(c for c in line if c.isdigit())
    last_digit = next(c for c in reversed(line) if c.isdigit())
    return int(first_digit + last_digit)


def sum_calibration_document(document: list[str]):
    return sum(line_to_calibration_value(line) for line in document)


if __name__ == '__main__':
    print(sum_calibration_document(read_input(day=1)))