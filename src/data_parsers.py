from collections import namedtuple
import csv
import gzip


def get_rows(file_names):
    Row = namedtuple('Row', ['timestamp', 'lineId', 'direction',
                             'journeyPatternId', 'timeFrame', 'vehicleJourneyId', 'operator',
                             'conjestion', 'lon', 'lat', 'delay', 'blockId', 'vehicleId', 'stopId',
                             'atStop'])

    for f_name in file_names:
        if f_name.endswith('csv'):
            f = open(f_name, 'rt', newline='')
        elif f_name.endswith('gz'):
            f = gzip.open(f_name, 'rt')
        else:
            raise IOError('Unnacceptable file: {}'.format(f_name))

        r = csv.reader(f)
        for line in r:
            yield Row(*line)
        f.close()
