"""Shared constants from the original EMNIST coursework notebook."""

EMNIST_SELECTED_LABELS: tuple[int, ...] = (1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 17, 20, 24, 26)

INDEX_TO_LETTER: dict[int, str] = {
    0: "A",
    1: "B",
    2: "D",
    3: "E",
    4: "F",
    5: "G",
    6: "I",
    7: "J",
    8: "L",
    9: "N",
    10: "O",
    11: "P",
    12: "Q",
    13: "T",
    14: "X",
    15: "Z",
}

LABEL_TO_INDEX: dict[int, int] = {
    original_label: mapped_index
    for mapped_index, original_label in enumerate(EMNIST_SELECTED_LABELS)
}

LETTER_TO_INDEX: dict[str, int] = {letter: index for index, letter in INDEX_TO_LETTER.items()}
