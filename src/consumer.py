from datetime import datetime

from geopy.distance import distance

from config import Conf, feature


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


def time_bin(dt):
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


def mps_to_MPH(n):
    """Does what it says on the tin. metres/sec to miles/hour."""
    return n / 0.44704


def consume(rows):
    """takes an iterable object (rows) as input and does something with it.
    @returns None
    """
    row = next(rows)
    dt = datetime.fromtimestamp(int(int(row[feature['timestamp']]) / 1000000))

    s = '\nBus {} on journey {}, line {}, during {} on a {}\n'
    print(s.format(row[feature['vehicleId']],
                   row[feature['vehicleJourneyId']],
                   row[feature['lineId']],
                   time_bin(dt), day(dt.weekday())))
    prev = row
    for row in rows:
        t = int(row[feature['timestamp']]) - int(prev[feature['timestamp']])
        t = int(t / 1000000)    # convert value into seconds

        if t < Conf.time_interval:
            continue

        dist = distance((row[feature['lat']], row[feature['lon']]),
                        (prev[feature['lat']], prev[feature['lon']])).meters

        speed = mps_to_MPH((dist / t))

        dist_from_centre = distance((row[feature['lat']], row[feature['lon']]),
                                    Conf.centre).miles

        s = "Interval (s) -> {:>4} \t Distance (m) -> {:>8.2f} \t Speed (MPH) -> {:>8.2f} \t Dist from centre (M) -> {:>8.2f}"
        print(s.format(t, dist, speed, dist_from_centre))

        prev = row
