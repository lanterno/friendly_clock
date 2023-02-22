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

        Uses a simplified template system.
        """

        TEMPLATE_BUILDERS = {
            # example: "Five o'clock"
            "no_minutes": lambda _hour, _pm: f"{stringify_number(_hour)} o'clock {'PM' if _pm else 'AM'}",
            # example: "Fifteen past Ten PM"
            "over_hour": lambda _hour, _minute, _pm: f"{stringify_number(_minute)}"
                                                     f" past {stringify_number(_hour)}"
                                                     f" {'PM' if _pm else 'AM'}",

            # example: "Fifteen Thirty"
            "mid_hour": lambda _hour, _pm: f"{stringify_number(_hour)} Thirty {'PM' if _pm else 'AM'}",
            # example: "Nine to Two AM"
            "under_hour": lambda _hour, _minute, _pm: f"{stringify_number(_minute)}"
                                                      f" to {stringify_number(_hour)}"
                                                      f" {'PM' if _pm else 'AM'}",

            # special cases: midday and midnight
            "0:0-PM:True": lambda: TimeConstants.MIDDAY,
            "0:0-PM:False": lambda: TimeConstants.MIDNIGHT,
        }

        # cover special cases
        if template_builder := TEMPLATE_BUILDERS.get(f"{self.hour}:{self.minute}-PM:{self.pm}"):
            return template_builder()

        if self.minute == 0:
            return TEMPLATE_BUILDERS['no_minutes'](self.hour, self.pm)
        elif self.minute < 30:
            return TEMPLATE_BUILDERS['over_hour'](self.hour, self.minute, self.pm)
        elif self.minute == 30:
            return TEMPLATE_BUILDERS['mid_hour'](self.hour, self.pm)
        else:
            # adjusting for when minutes are over 30, and we want
            # to show something like "ten to two PM"
            hour = (self.hour + 1) % 12  # if time passes the 12 o'clock point, we switch the PM status
            minute = 60 - self.minute
            pm = self.pm if hour else not self.pm
            return TEMPLATE_BUILDERS['under_hour'](hour, minute, pm)
