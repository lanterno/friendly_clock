class TimeConstants:
    PM = "PM"
    AM = "AM"
    OCLOCK = "o'clock"
    MIDDAY = "midday"
    MIDNIGHT = "midnight"
    OVER_HOUR = "past"
    UNDER_HOUR = "to"


NUMERIC_WORD_MAP = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
}


def convert_number_to_str(num: int) -> str:
    """
    converts a number from numeric representation to string representation
    example 19 -> Nineteen
    Only accepts values between 0 -> 30
    """
    if num > 30:
        raise Exception(f"Only accepts number between 0 to 30. got {num}")

    if num < 20:
        return NUMERIC_WORD_MAP[num]

    tens = (num // 10) * 10
    return f"{NUMERIC_WORD_MAP[tens]}{' ' if num % 10 else ''}{NUMERIC_WORD_MAP[num % 10]}"
