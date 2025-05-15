"""
Create a random play
+ In which each string will be randomly generated.
+ In which each notes will be randomly picked from a list.
"""

import random


def randomizeStringNotes(
    string_list: list[str], note_list: list[str]
) -> tuple[str, str]:
    gstring = random.choice(string_list)
    notes = random.choice(note_list)

    return gstring, notes
