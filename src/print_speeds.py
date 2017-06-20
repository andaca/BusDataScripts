from datetime import datetime

from geopy.distance import distance

from utils.data_descriptors import CITY_CENTRE, FEATURES as F
from utils.stream import data_stream, filter_rows
from utils import bins
from utils.calcs import mps_to_MPH


def consume(rows, time_interval):
    """takes an iterable object (rows) as input and does something with it.
    @returns None
    """
    row = next(rows)
    dt = datetime.fromtimestamp(int(int(row[F['timestamp']]) / 1000000))

    s = '\nBus {} on journey {}, line {}, during {} on a {}\n'
    print(s.format(row[F['vehicleId']],
                   row[F['vehicleJourneyId']],
                   row[F['lineId']],
                   bins.time(dt), bins.day(dt.weekday())))
    prev = row
    for row in rows:
        t = int(row[F['timestamp']]) - int(prev[F['timestamp']])
        t = int(t / 1000000)    # convert value into seconds

        if t < time_interval:
            continue

        dist = distance((row[F['lat']], row[F['lon']]),
                        (prev[F['lat']], prev[F['lon']])).meters

        speed = mps_to_MPH((dist / t))

        dist_from_centre = distance((row[F['lat']], row[F['lon']]),
                                    CITY_CENTRE).miles

        s = "Interval (s) -> {:>4} \t Distance (m) -> {:>8.2f} \t Speed (MPH) -> {:>8.2f} \t Dist from CITY_CENTRE (M) -> {:>8.2f}"
        print(s.format(t, dist, speed, dist_from_centre))

        prev = row


if __name__ == '__main__':

    time_interval = 60 * 3
    files = '../data/siri*gz'

    filter_ = {
        F['vehicleId']: '33096',
        F['vehicleJourneyId']: '14267'
    }

    ds = data_stream(files)
    rows = filter_rows(ds, filter_)
    consume(rows, time_interval)
