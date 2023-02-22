import re


class TimeParserException(Exception):
    """
    Exception raised when time is not in expected format
    """
    def __init__(self, message="Time not in expected format hh:mm"):
        super().__init__(message)


class Time:
    def __init__(self, hour: int, minute: int, pm: bool):
        self.hour = hour
        self.minute = minute
        self.pm = pm

    @property
    def is_oclock(self):
        return self.minute == 0

    @classmethod
    def from_str(cls, time_as_str: str) -> 'Time':
        """
        Parses a time string from the format hh:mm
        to construct a Time object

        Raises TimeParserException if time not in correct format
        """

        time_re = re.compile("^(?P<hh>\d{2}):(?P<mm>\d{2})$")
        match = time_re.match(time_as_str)
        if not match:
            raise TimeParserException

        hour, minute = int(match.groupdict()['hh']), int(match.groupdict()['mm'])

        pm = 12 <= hour < 24
        hour = hour % 12

        return cls(hour, minute, pm)
