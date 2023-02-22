import unittest

from time import Time, TimeParserException


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

    def test_time_oclock(self):
        pass

    def test_special_day_times(self):
        pass

    def test_minutes_above_30(self):
        pass

    def test_minutes_under_30(self):
        pass

    def test_minutes_exactly_30(self):
        pass

    def test_switch_between_am_to_pm(self):
        pass

    def test_switching_from_pm_to_am(self):
        pass


if __name__ == '__main__':
    unittest.main()
