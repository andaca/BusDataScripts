def day(n):
    return {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }[n]


def time(dt):
    """Takes a Datetime object, returns the time bin as a string.
    morning_rush : 05:00 - 08:59
    day_time :     09:00 - 16:59
    evening_rush : 16:00 - 18:59
    night_time :   19:00 - 04:59
    """
    if dt.hour > 5 and dt.hour < 9:
        return 'morning_rush'
    if dt.hour >= 9 and dt.hour < 16:
        return 'day_time'
    if dt.hour >= 16 and dt.hour < 19:
        return 'evening_rush'
    return 'night_time'
