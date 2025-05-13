import random

class Session():
    """class to manage session play data"""
    def __init__(self):
        self.data = {}
        self.finished = []
        self.done = False

    def insert(self, string_no:str, note: str):
        """
        Check if the string is in the session data.
        if yes, add the note to the list.
        if no, create {string: [] } and add the note.
        Args:
            string_no (int) interger represents the string number only 1-6
            note (str): diatonic note.
        Return: None
        """
        if string_no not in self.data.keys():
            self.data[string_no] = [note]
            return
        if not self._checkFinish(string_no):
            self.data[string_no].append(note)
            return
        if string_no not in self.finished:
            self.finished.append(string_no)
        if len(self.finished) == 6:
            self.done = True

    def _checkFinish(self,string_no:str) -> bool:
        """
        Check if the unique datas in a guitar-string is 7
        Args:
            String_no
        Returns:
            Bool
        """
        length = len(set(self.data[string_no]))
        if length == 7: 
            return True
        return False


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
