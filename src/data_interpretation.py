from glob import glob
from collections import namedtuple

from analysis_tools import dist_time_increments
from row_generator import get_rows

CITY_CENTRE = ('53.346375', '-6.263111')  # Ha'penny bridge


def filter_func(row):
    return row.vehicleId == '33521' and row.vehicleJourneyId == '3883'


def main():
    files = glob('../data/siri.20130101.csv.gz')
    print('{} files to process'.format(len(files)))
    all_rows = get_rows(files)
    rows = filter(filter_func, all_rows)
    cleaned = ((r.timestamp, r.lat, r.lon) for r in rows)
    for c in cleaned:
        print(c)
        input()


if __name__ == '__main__':
    main()
