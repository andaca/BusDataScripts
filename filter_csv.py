import csv
from itertools import count
import os
from glob import glob
import gzip


class Config:
    src_files = 'siri*.gz'  # Only .gz and .csv files accepted.
    out_file = 'output.csv'

    @staticmethod
    def filter(row):
        """
        Takes a row as input. If returns True, row is written to new file.
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


n_written = 0
out_file = open(Config.out_file, 'w', newline='')
writer = csv.writer(out_file)

files = glob(Config.src_files)

for i, filename in enumerate(files):
    print('\n Processing file {} of {}...'.format(i + 1, len(files)))

    extension = filename.split('.')[-1]

    if extension == 'gz':
        in_file = gzip.open(filename, 'rt', newline='')
    elif extension == 'csv':
        in_file = open(filename, newline='')
    else:
        out_file.close()
        raise SystemExit(
            'Unrecognised extension: {}. Exiting'.format(filename))

    reader = csv.reader(in_file)
    for row in reader:
        if Config.filter(row):
            writer.writerow(row)
            n_written += 1
            print('\r {} rows written'.format(n_written), end='')

    in_file.close()
out_file.close()


# the outfile is created, even if no rows were written
if n_written == 0:
    print('{} matching rows found.'.format(n_written))
    os.remove(Config.out_file)

print("\n Done.")
