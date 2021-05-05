class UniqueElements:
    def __init__(self, data: list):
        self.data = data
        self.index = -1

    def __iter__(self):
        """
        From given data list return unique list_iterator
        :return: list_iterator
        """
        return iter(list(set(self.data)))