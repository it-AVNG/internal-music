import random

from src.mod.session import Session

def play():
    # Common ariable
    diatonic_Note = ["C", "D", "E", "F", "G", "A", "B"]
    session_mem = Session()

    while True:
        single_note = random.randint(0, 6)
        single_string = random.randint(1,6)
        note = diatonic_Note[single_note]
        print(f"Note to play on string {single_string}: {diatonic_Note[single_note]}")
        # add to session_memory
        session_mem.insert(string_no=str(single_string), note=note)
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
