import re

from app.helpers import TimeConstants, convert_number_to_str


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
        if self.is_oclock and self.hour == 0:  # midday or midnight
            return TimeConstants.MIDDAY if self.pm else TimeConstants.MIDNIGHT

        pm_str = TimeConstants.PM if self.pm else TimeConstants.AM

        if self.is_oclock:
            return f"{convert_number_to_str(self.hour)} {TimeConstants.OCLOCK} {pm_str}"
        elif self.minute < 30:
            return f"{convert_number_to_str(self.minute)} {TimeConstants.OVER_HOUR} {convert_number_to_str(self.hour)} {pm_str}"
        elif self.minute == 30:
            return f"{convert_number_to_str(self.hour)} {convert_number_to_str(self.minute)} {pm_str}"
        else:
            hour = self.hour + 1
            minute = 60 - self.minute
            if hour % 12 == 0:
                pm = not self.pm
                pm_str = TimeConstants.PM if pm else TimeConstants.AM
            minute_display = convert_number_to_str(minute)
            return f"{convert_number_to_str(minute)} {TimeConstants.UNDER_HOUR} {convert_number_to_str(hour)} {pm_str}"

