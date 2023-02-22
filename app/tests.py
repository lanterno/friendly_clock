import unittest

from app.time import Time, TimeParserException


class TestHumanizeTimeParser(unittest.TestCase):

    def test_wrong_time_format(self):
        with self.assertRaises(TimeParserException):
            Time.from_str("aa:bb")

        with self.assertRaises(TimeParserException):
            Time.from_str("1:2")

    def test_parse_special_day_times(self):
        # midday
        time = Time.from_str("12:00")
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.pm, True)
        # midnight
        time = Time.from_str("24:00")
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.pm, False)
        # another way to represent midnight
        time = Time.from_str("00:00")
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.pm, False)

    def test_parse_normal_times(self):
        # AM
        time = Time.from_str("04:12")
        self.assertEqual(time.hour, 4)
        self.assertEqual(time.minute, 12)
        self.assertEqual(time.pm, False)
        # PM
        time = Time.from_str("14:35")
        self.assertEqual(time.hour, 2)
        self.assertEqual(time.minute, 35)
        self.assertEqual(time.pm, True)


class TestHumanizeTime(unittest.TestCase):

    def test_special_day_times(self):
        time = Time.from_str("12:00")
        self.assertEqual(time.humanize(), "midday")

        time = Time.from_str("24:00")
        self.assertEqual(time.humanize(), "midnight")

    def test_time_oclock(self):
        time = Time.from_str("04:00")
        self.assertEqual(time.humanize(), "Four o'clock AM")

        time = Time.from_str("14:00")
        self.assertEqual(time.humanize(), "Two o'clock PM")

        time = Time.from_str("23:00")
        self.assertEqual(time.humanize(), "Eleven o'clock PM")

    def test_minutes_above_30(self):
        time = Time.from_str("08:32")
        self.assertEqual(time.humanize(), "Twenty Eight to Nine AM")

    def test_minutes_under_30(self):
        time = Time.from_str("15:17")
        self.assertEqual(time.humanize(), "Seventeen past Three PM")

    def test_minutes_exactly_30(self):
        time = Time.from_str("15:30")
        self.assertEqual(time.humanize(), "Three Thirty PM")

    def test_switch_between_am_to_pm(self):
        time = Time.from_str("11:45")
        self.assertEqual(time.humanize(), "Fifteen to Twelve PM")

    def test_switching_from_pm_to_am(self):
        time = Time.from_str("23:51")
        self.assertEqual(time.humanize(), "Nine to Twelve AM")


if __name__ == '__main__':
    unittest.main()
