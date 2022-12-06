class ArithmeticCoding:
    def __init__(self, alphabet, p, encoded_number=None, length=None):
        self.alphabet = alphabet
        self.p = p
        self.encoded_number = encoded_number
        self.length = length

    def decode(self):
        encoded_number = self.encoded_number
        decoded_msg = ""

        for _ in range(self.length):
            for i, letter in enumerate(self.alphabet):
                left_bound = sum(self.p[:i])
                right_bound = sum(self.p[:i + 1])
                interval = (left_bound, right_bound)

                if interval[0] <= encoded_number < interval[1]:
                    decoded_msg += letter
                    encoded_number = (encoded_number - interval[0]) / (interval[1] - interval[0])
                    encoded_number = round(encoded_number, 10)
                    break

        return decoded_msg
