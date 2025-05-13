import random


def main():
    # Unversal Variable
    diatonic_Note = ["C", "D", "E", "F", "G", "A", "B"]
    session_mem = {}
    while True:
        single_note = random.randint(0, 6)
        single_string = random.randint(1,6)
        print(f"Note to play on string {single_string}: {diatonic_Note[single_note]}")

        # add to session_memory
        if single_string not in session_mem.keys():
            session_mem[single_string] = [single_note]
        else:
            session_mem[single_string].append(single_note)

        # ask if you still want to play
        print(f"current session: {session_mem}")

        print("continue (Default es)? (Y/N)")
        ans = input()
        if ans.upper() != "N":
            continue
        else:
            break


if __name__ == "__main__":
    main()
