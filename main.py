import random

def main():
    # Unversal Variable
    diatonic_Note = ["C","D","E","F","G","A","B"]
    while True:
        single_note = random.randint(0,7)
        print(f"Note to play on single string: {diatonic_Note[single_note]}")
        # ask if you still want to play
        print("continue (Default Yes)? (Y/N)")
        ans = input()
        if ans.upper() != "N":
            continue
        else:
            break



if __name__ == "__main__":
    main()
