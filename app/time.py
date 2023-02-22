import re

from app.helpers import TimeConstants, stringify_number


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
        """
        Returns True if minute is zero
        """
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

    def humanize(self):
        """
        Displays the time in a human-friendly format
        """
        if self.hour == 0 and self.is_oclock:  # midday or midnight
            return TimeConstants.MIDDAY if self.pm else TimeConstants.MIDNIGHT

        pm = self.pm
        if self.minute == 0:
            display = f"{stringify_number(self.hour)} {TimeConstants.OCLOCK}"
        elif self.minute < 30:
            display = f"{stringify_number(self.minute)} {TimeConstants.OVER_HOUR} {stringify_number(self.hour)}"
        elif self.minute == 30:
            display = f"{stringify_number(self.hour)} {stringify_number(self.minute)}"
        else:
            # adjusting for when minutes are over 30, and we want
            # to show something like 10 to 2 PM
            hour = (self.hour + 1) % 12  # if time passes the 12 o'clock point, we switch the PM status
            minute = 60 - self.minute
            pm = pm if hour else not pm
            display = f"{stringify_number(minute)} {TimeConstants.UNDER_HOUR} {stringify_number(hour)}"

        return f"{display} {TimeConstants.PM if pm else TimeConstants.AM}"
