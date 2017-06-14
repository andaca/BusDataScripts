import csv
from itertools import count
import os


class Config:
    src_file = 'siri.20130101.csv'
    out_file = 'output.csv'

    @staticmethod
    def filter(row):
        """
        Takes an row as input. If returns True, row is written to new file.
        See feature dictionary below for options.
        @params: row (list)
        @returns: boolean
        """
        return row[feature['lineId']] == '40'


# map feature name to column number for easier access
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


if os.path.exists(Config.out_file):
    print('File {} already exists. Exiting.'.format(Config.out_file))
    raise SystemExit

with open(Config.src_file, newline='') as r:
    n_written = 0
    reader = csv.reader(r)
    with open(Config.out_file, 'w', newline='') as w:
        writer = csv.writer(w)
        for row in reader:
            if Config.filter(row):
                writer.writerow(row)
                n_written += 1
                print('\r {} rows written'.format(n_written), end='')


# the outfile is created, even if no rows were written
if n_written == 0:
    print('{} matching rows found.'.format(n_written))
    os.remove(Config.out_file)

print("\n Done.")
