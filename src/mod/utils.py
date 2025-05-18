"""
Create a random play
+ In which each string will be randomly generated.
+ In which each notes will be randomly picked from a list.
"""
import logging
import random

module_logger = logging.getLogger(__name__)

def randomizeStringNotes(
    string_list: list[str], note_list: list[str]
) -> tuple[str, str]:
    logger = logging.getLogger(f"{module_logger.name}.randomizeStringNotes")
    logger.info("select a random string from pool")
    gstring = random.choice(string_list)
    logger.info("select a random tone from pool")
    notes = random.choice(note_list)
    logger.info("return selected combination")
    return gstring, notes
