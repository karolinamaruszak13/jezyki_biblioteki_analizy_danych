class CommandNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class FigureNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ColorNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidNameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)