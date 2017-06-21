from geopy.distance import distance


def mps_to_MpH(n):
    """Converts metres/sec to miles/hour"""
    return n / 0.44704


def dist_time_difference():
    """Recieves rows and yields the distance and time elapsed between readings.
    @params : rows (namedtuples)
    @returns: double, int
    """
    prev = yield
    row = yield

    while True:
        d = distance((row.lat, row.lon), (prev.lat, prev.lon)).meters
        t = int(row.timestamp) - int(prev.timestamp)
        prev = row
        row = yield d, int(t / 1000000)
