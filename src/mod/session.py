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
