class Session:
    """class to manage session play data"""

    def __init__(self):
        self.data: dict[
            str, dict
        ] = {}  # store and keep track of generated random string : [note]
        self.finished = []
        self.done = False

    def insert(self, string_no: str, note: str):
        """
        
        """
        # if the string is not played yet, track it play session
        if string_no not in self.data.keys():
            self.data[string_no] = {note: 1}
            return

        # if the genereated string is not finished playing apply update to the data.
        if not self._checkStringNoteFinish(string_no, note):
            # increase the note played on the string
            self.data[string_no][note] += 1
            return
        # if the generated tring has finished playing, append to finished list
        length = len(self.data[string_no])
        if (string_no not in self.finished) and (length == 7):
            self.finished.append(string_no)

        # if all strings finished playing, mark the session as done.
        if len(self.finished) == 6:
            self.done = True


    def _checkStringNoteFinish(self, string_no: str, note: str) -> bool:
        if note not in self.data[string_no].keys():
            self.data[string_no].update({note: 1})
        note_played_2 = self.__checkNotePlayed(string_no=string_no, note=note)
        if note_played_2:
            return True
        return False

    def __checkNotePlayed(self, string_no: str, note: str) -> bool:
        """
        Returns true if the note on the string is played 2 times.
        """
        if self.data[string_no][note] == 2:
            return True
        return False

