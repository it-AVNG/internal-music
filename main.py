# import random
from src.mod.utils import randomizeStringNotes
from src.mod.session import Session


def play():
    session_mem = Session()

    while True:
        res = randomizeStringNotes()
        print(f"current random {res}")
        single_string = res[0]
        note = res[1]
        # add to session_memory
        session_mem.insert(string_no=str(single_string), note=str(note))
        # check if session is done:
        if session_mem.done:
            print("current session:")
            print(f"finished string: {session_mem.finished}")
            print("Thank you for playing")
            break
        # ask if you still want to play
        print("current session:")
        print(f"finished string: {session_mem.finished}")
        print("continue (Default yes)? (Y/N)")
        ans = input()
        if ans.upper() != "N":
            continue
        else:
            break


if __name__ == "__main__":
    play()
