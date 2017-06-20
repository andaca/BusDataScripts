from itertools import count

FEATURES = dict(zip([
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

CITY_CENTRE = ('53.346375', '-6.263111')  # Ha'penny bridge
