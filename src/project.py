VALID_OPERATORS = ["+", "-", "/", "*", "%"]


def isOperator(val: str) -> bool:
    return val in VALID_OPERATORS


state_table = [
    [1, 1, 18, 18, 18, 18, 18, 18, 18, 18],
    [1, 1, 2, 4, 3, 18, 18, 18, 18, 18, 18],
    [2, 2, 2, 4, 3, 18, 18, 18, 18, 18, 18],
    [18, 18, 18, 4, 3, 18, 18, 18, 18, 18, 18],
    [5, 5, 7, 18, 4, 18, 9, 11, 14, 18, 18],
    [5, 5, 6, 18, 16, 17, 18, 18, 18, 4, 18],
    [6, 6, 6, 18, 16, 17, 18, 18, 18, 4, 18],
    [18, 18, 7, 18, 16, 17, 8, 18, 18, 4, 18],
    [18, 18, 8, 18, 16, 17, 18, 18, 18, 18, 18],
    [18, 18, 10, 18, 18, 18, 18, 18, 18, 18, 18],
    [18, 18, 10, 18, 16, 17, 18, 18, 18, 4, 18],
    [12, 12, 12, 12, 12, 12, 12, 18, 12, 12, 12],
    [18, 18, 18, 18, 18, 18, 18, 13, 18, 18, 18],
    [18, 18, 18, 18, 16, 17, 18, 18, 18, 4, 18],
    [14, 14, 14, 14, 14, 14, 14, 14, 15, 14, 14],
    [18, 18, 18, 18, 15, 17, 18, 18, 18, 4, 18],
    [18, 18, 18, 18, 16, 17, 18, 18, 18, 4, 18],
    [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],
    [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
]


def is_assignment_valid(statement: str) -> bool:
    state = char = 0
    was_semi_colon_seen = False
    is_valid = True
    for character in statement:
        if character == "_":
            char = 0
        elif character.isalpha():
            char = 1
        elif character.isdigit():
            char = 2
        elif character == "=":
            char = 3
        elif character == " ":
            char = 4
        elif character == ";":
            char = 5
            was_semi_colon_seen = True
        elif character == ".":
            char = 6
        elif character == "'":
            char = 7
        elif character == '"':
            char = 8
        elif isOperator(character):
            char = 9
        else:
            char = 10

        state = state_table[state][char]

        if state == 18:
            is_valid = False
            break
        elif state == 17:
            break

    return is_valid and was_semi_colon_seen
