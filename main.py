from src.mod.session import Session
import pprint

'''
TODO: 
+ [ ] Write Tests for all the current features
+ [x] Write docstrings for all the current methods and classes
+ [ ] create logging methods using the following format:

<"severity" - "scope" : "message" - "timestamp:2022-05-14T14:16:15+00:00">

'''

def play():
    session_mem = Session()

    while True:
        res = session_mem.randomize()
        print(f"current random {res}")
        single_string = res[0]
        note = res[1]
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


from typing import Union
if __name__ == "__main__":
    play()
