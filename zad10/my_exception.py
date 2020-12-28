class OptionNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

class IDNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)