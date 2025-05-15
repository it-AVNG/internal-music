"""
Create a random play
+ In which each string will be randomly generated.
+ In which each notes will be randomly picked from a list.
"""

from typing import Union
import random


def randomizeStringNotes() -> Union[tuple[str, str], tuple[None, None]]:
    # create a random string
    string_no = random.randint(1, 6)
    # list of diatonic notes
    diatone = ["C", "D", "E", "F", "G", "A", "B"]
    ## Random selection
    notes = diatone[random.randint(0, 6)]
    return str(string_no), notes
