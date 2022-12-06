class BTW:
    def __init__(self, message: str, humanize_index=False):
        self.initial_message = message
        self.table = [message]
        self.fee = 1 if humanize_index else 0
        self._fill_table()

    def encode(self):
        return self._get_last_column(), self._get_initial_message_index()

    def _fill_table(self) -> None:
        message = self.initial_message
        for _ in range(len(self.initial_message)):
            message = message[1:] + message[0]
            if message == self.initial_message:
                break
            self.table.append(message)
        self.table.sort()

    def _get_initial_message_index(self):
        return self.table.index(self.initial_message) + self.fee

    def _get_last_column(self):
        last_chars_list = [row[-1:] for row in self.table]
        return "".join(last_chars_list)
