"""
Create a random play
+ In which each string will be randomly generated.
+ In which each notes will be randomly picked from a list.
"""

from typing import Union
import random


def randomizeStringNotes(
    string_list: list[str], note_list: list[str]
) -> Union[tuple[str, str], tuple[None, None]]:
    gstring = random.choice(string_list)
    notes = random.choice(note_list)

    return gstring, notes
