from utils.data_descriptors import FEATURES as F
from utils.stream import data_stream, filter_rows

files = '../data/*gz'
filter_ = {F['lineId']: '40'}

all_rows = data_stream(files)
rows = filter_rows(all_rows, filter_)
for row in rows:
    print(row)
