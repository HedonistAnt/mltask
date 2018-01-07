import numpy as np
import time
import datetime
from matplotlib import  pyplot as plt

def plot_classes (class_0,class_1,class_2,undefined,validation):
    area = np.pi * 1

    """x0 = list(map(lambda data: data["longitude"],class_0))
    y0 = list(map(lambda data: data["latitude"],class_0))
    plt.scatter(x0, y0, s = area,c = "red",alpha=0.5)

    x1= list(map(lambda data: data["longitude"], class_1))
    y1 = list(map(lambda data: data["latitude"], class_1))
    plt.scatter(x1, y1, s=area, c="green",alpha=0.5)

    x2 = list(map(lambda data: data["longitude"], class_2))
    y2 = list(map(lambda data: data["latitude"], class_2))
    plt.scatter(x2, y2, s=area, c="blue",alpha=0.5)
    """
    xv = list(map(lambda data: data["longitude"], class_2))
    yv = list(map(lambda data: data["latitude"], class_2))
    plt.scatter(xv, yv, s=area, c="black", alpha=0.5)


    plt.show()


def time_to_seconds(unixtime):
    hms = time.strptime(datetime.datetime.fromtimestamp(
        int(unixtime)
    ).strftime('%H:%M:%S'), '%H:%M:%S')

    d  = time.strptime(datetime.datetime.fromtimestamp(
        int(unixtime)
    ).strftime('%Y-%m-%d'), '%Y-%m-%d').tm_mday


    toseconds = datetime.timedelta(hours=hms.tm_hour, minutes=hms.tm_min, seconds=hms.tm_sec).total_seconds()

    return  toseconds ,d

def parse_classes ():

    dataset = np.loadtxt("transport_data.csv", dtype={'names': ('longitude', 'latitude', 'request_ts','trans_ts','label'),
                                        'formats': ('f8', 'f8', 'i8','i8','S1')}, delimiter=",")

    dataset = dataset[[b for b in list(dataset.dtype.names) if b != 'requests_ts']]


    X=[]
    Y=[]
    UX =[]
    for data in dataset :

        data['trans_ts'],d= time_to_seconds(data['trans_ts'])

        if data['label']==b'0':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(0)
        if data['label']==b'1':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(1)

        if data['label']==b'2':
            X.append((data['longitude'], data['latitude'], data['trans_ts']))
            Y.append(2)

        if data['label']==b'?':

            UX.append((data['longitude'], data['latitude'], data['trans_ts']))
        #data = np.array(data).reshape(-1, 1)

    return X,Y,UX




if __name__=="__main__":
    class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
    #plot_classes(class_0, class_1, class_2, undefined,validation)
    X, Y, UX, VX, VY,traindates,vdates,udates = parse (class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates)