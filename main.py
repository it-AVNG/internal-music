from src.mod.utils import randomizeStringNotes
from src.mod.session import Session
import pprint


def generate_play():
    string_list = ["1", "2", "3", "4", "5", "6"]
    diatone = ["C", "D", "E", "F", "G", "A", "B"]
    res = randomizeStringNotes(string_list=string_list, note_list=diatone)
    return res


def play():
    session_mem = Session()

    while True:
        res = generate_play()
        print(f"current random {res}")
        single_string = res[0]
        note = res[1]
        # check if the note has been played, if yes, repeat
        # add to session_memory
        session_mem.insert(string_no=str(single_string), note=str(note))
        # check if session is done:
        if session_mem.done:
            print("current session:")
            pprint.pprint(session_mem.data)
            print(f"finished string: {session_mem.finished}")
            print("Thank you for playing")
            break
        # ask if you still want to play
        print("current session:")
        pprint.pprint(session_mem.data)
        print(f"finished string: {session_mem.finished}")
        print("continue (Default yes)? (Y/N)")
        ans = input()
        if ans.upper() != "N":
            continue
        else:
            break


if __name__ == "__main__":
    play()
