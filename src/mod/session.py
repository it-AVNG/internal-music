from .utils import randomizeStringNotes


class PlaySession:
    """A class to manage randomize of strings and note"""
    def __init__(self):
        self.gstrings: list[str] = ["1", "2", "3", "4", "5", "6"]
        self.diatones: list[str] = ["C", "D", "E", "F", "G", "A", "B"]

    def randomize(self):
        """
        Random generate a combination tuple of string and tone to play
        """
        return randomizeStringNotes(string_list=self.gstrings, note_list=self.diatones)

    def _remove_done_string(self, string: str):
        """
        Method to remove string that has fulfilled condition of finished practice.
        Args:
            string (str): string to remove from the random pool.
        Return:
            self
        """
        self.gstrings.remove(string)
        return self

class Session(PlaySession):
    """class to manage session play data, subclass of session.PlaySession"""

    def __init__(self):
        PlaySession.__init__(self)
        self.data: dict[str, dict[str,int]] = {}  # keep track of string : [note]
        self.finished: list[str] = [] # finished strings
        self.done: bool = False # if True, play session ends

    def insert(self, string_no: str, note: str):
        """
        Insert to session data
        Args:
            string_no (str): string to play.
            note (str): tone to play
        Returns:
            None
        """
        # if the string is not played yet, init the string data
        if string_no not in self.data.keys():
            self.data[string_no] = {note: 1}
            return

        # if the string is not finished playing apply update to the data.
        if not self._checkStringNoteFinish(string_no, note):
            # increase the note played on the string
            self.data[string_no][note] += 1
            return
        # if the generated tring has finished playing, append to finished list
        length = len(self.data[string_no])
        if (string_no not in self.finished) and (length == 7):
            self.finished.append(string_no)
            _ = self._remove_done_string(string=string_no)

        # if all strings finished playing, mark the session as done.
        if len(self.finished) == 6:
            self.done = True

    def _checkStringNoteFinish(self, string_no: str, note: str) -> bool:
        """
        Internal class method to check if the string-Note pair is finised playing.
        Args:
            string_no (str): string to check.
            note (str): note to check
        Returns:
            bool
        """
        # if the note has never been played in
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
