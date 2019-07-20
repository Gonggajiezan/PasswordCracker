from enum import Enum

class Option(Enum):
    num = 0
    letter = 1
    spec_char = 2
    num_letter = 3
    num_spec_char = 4
    letter_spec_char = 5
    num_letter_spec_char = 6

# test
# for option in Option:
#     if option.value == 0:
#         print(option)