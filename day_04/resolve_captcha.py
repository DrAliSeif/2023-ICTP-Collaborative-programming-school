"""
The solution to day 1 of the 2017 Advent of Code.

Go to the following website for further information:
https://adventofcode.com/2017/day/1
"""


def read_first_line(file_name):
    """Read the first line of text file.

    Parameters
    ----------
    file_name : str
        The path to the text file.

    Returns
    -------
    str
        The first line.
    """
    with open(file_name, "r") as f:
        line = f.readline()
        # get rid of new line character at the end
        line = line.strip()
    return line


def process_captcha(digit_sequence):
    """Calculate the answer to the captcha.

    Get a sequence of digits and check for a single repeat for consecutive digits.
    Calculate the sum of the repeated digits. Notes: The digit sequence is
    cyclic.

    Parameters
    ----------
    digit_sequence : str
        Sequence of digits.

    Returns
    -------
    int
        Sum of repeated digits.
    """
    sum_of_digits = 0
    for i, digit in enumerate(digit_sequence):
        if digit == digit_sequence[i - 1]:
            sum_of_digits += int(digit)
    return sum_of_digits


def main():
    file_name = "input.txt"
    captcha = read_first_line(file_name)
    answer = process_captcha(captcha)

    assert 1203 == answer
    assert 3 == process_captcha("1122")
    assert 4 == process_captcha("1111")
    assert 0 == process_captcha("1234")
    assert 9 == process_captcha("91212129")

    print(f"The answer is {answer}")


if __name__ == "__main__":
    main()
