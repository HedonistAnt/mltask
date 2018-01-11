import numpy as np
import time
import datetime


def time_to_seconds(unixtime):
    hms = time.strptime(datetime.datetime.fromtimestamp(
        int(unixtime)
    ).strftime('%H:%M:%S'), '%H:%M:%S')

    d = time.strptime(datetime.datetime.fromtimestamp(
        int(unixtime)
    ).strftime('%Y-%m-%d'), '%Y-%m-%d').tm_mday
    toseconds = datetime.timedelta(hours=hms.tm_hour, minutes=hms.tm_min, seconds=hms.tm_sec).total_seconds()
    return toseconds, d


def parse_classes():
    dataset = np.loadtxt("transport_data.csv",
                         dtype={'names': ('longitude', 'latitude', 'request_ts', 'trans_ts', 'label'),
                                'formats': ('f8', 'f8', 'i8', 'i8', 'S1')}, delimiter=",")
    dataset = dataset[[b for b in list(dataset.dtype.names) if b != 'requests_ts']]
    X = []
    Y = []
    UX = []
    for data in dataset:

        data['trans_ts'], d = time_to_seconds(data['trans_ts'])

        if data['label'] == b'?':
            UX.append((data['longitude'], data['latitude'], data['trans_ts']))

        if data['label'] == b'0':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(0)

        if data['label'] == b'1':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(1)

        if data['label'] == b'2':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(2)

    return X, Y, UX


if __name__ == "__main__":
    X, Y, UX = parse_classes()
