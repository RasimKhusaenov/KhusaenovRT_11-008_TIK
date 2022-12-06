class MoveToFront:
    def __init__(self, message, alphabet=None, humanize_index=False):
        self.initial_message = message
        self.sequence = []
        self.alphabet = self._get_alphabet(alphabet)
        self.fee = 1 if humanize_index else 0

    def encode(self):
        current_alphabet = self.alphabet
        for char in self.initial_message:
            current_char_index = current_alphabet.index(char)
            self.sequence.append(current_char_index + self.fee)
            current_alphabet = [current_alphabet.pop(current_char_index)] + current_alphabet
        return int("".join(map(str, self.sequence)))

    def _get_alphabet(self, alphabet):
        if alphabet:
            return list(alphabet)
        return sorted(set(list(self.initial_message)))
