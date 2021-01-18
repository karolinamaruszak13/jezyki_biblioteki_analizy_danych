class OptionNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)   # w Pythonie wyjątek może być pusty - ten konstruktor nic nowego nie wnosi


class IDNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PublishmentYearError(Exception):
    def __init__(self, message):
        super().__init__(message)
