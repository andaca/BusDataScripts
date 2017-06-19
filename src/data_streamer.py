import csv
from glob import glob
import gzip

from consumer import consume
from config import Conf, feature


class RowRejected(Exception):
    """Raised to break out of nested loop when a row doesn't pass the filter"""
    pass


def files_opener(files_glob):
    """Open files that match the glob. Yields file objects sequentially,
    closing each before opening the next."""
    for filename in glob(files_glob):
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.csv'):
            f = open(filename, 'rt')
        else:
            raise IOError('Unnacceptable file: {}'.format(filename))
        yield f
        f.close()


def lines_reader(files):
    """Iterates over files and yields their contents one line (str) at a time"""
    for f in files:
        for line in f:
            yield line


def rowify(lines):
    """Parses csv lines (strings) and yields lists"""
    reader = csv.reader(lines)
    for row in reader:
        yield row


# TODO: Refactor?
def filter_(rows, filter_spec):
    """Applies the filter specified in the Conf class to the rows.
    Only yields matching rows."""
    for row in rows:
        try:
            for key, val in filter_spec.items():
                if row[feature[key]] != val:
                    raise RowRejected
            yield row
        except RowRejected:
            continue


def main():
    files = files_opener(Conf.files)
    lines = lines_reader(files)
    all_rows = rowify(lines)
    rows = filter_(all_rows, Conf.filter)
    consume(rows)


if __name__ == '__main__':
    main()
