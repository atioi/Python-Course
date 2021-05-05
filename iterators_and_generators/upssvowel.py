class UpssVowel:
    """
    Simply class that implement iterator that return 'Upps' when find vowel in given text
    """
    # Polish alphabet
    vowels = {'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y'}

    def __init__(self, text: str):
        self.text = text
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != len(self.text) - 1:
            self.index = self.index + 1
            if self.text[self.index] in self.vowels:
                return 'Upss'
            else:
                return self.text[self.index]
        raise StopIteration
