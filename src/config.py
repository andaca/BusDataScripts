from itertools import count


class Conf:
    files = 'siri*gz'

    filter = {
        'vehicleId': '33096',
        'vehicleJourneyId': '14267'
    }

    centre = ('53.346375', '-6.263111')  # Ha'penny bridge

    # calculate distance moved only at intervals of >= (time_interval) in seconds
    time_interval = 60 * 3


feature = dict(zip([
    'timestamp',
    'lineId',
    'direction',
    'journeyPatternId',
    'timeFrame',
    'vehicleJourneyId',
    'operator',
    'congestion',
    'lon',
    'lat',
    'delay',
    'blockId',
    'vehicleId',
    'stopId',
    'atStop'
], count()))
