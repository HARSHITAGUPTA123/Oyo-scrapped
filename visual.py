import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('/home/harshita/web_scrapping/oyo/oyorooms.csv')

room_types = []
address = []
# room_type=['premium','flagship','apartment']
# print data['HOTEL NAME']

for row in data['HOTEL NAME']:

    _, room_type, add = row.split(' ', 2)
    room_types.append(room_type)
    address.append(add)

data['ADDRESS'] = address
data['ROOM TYPE'] = room_types
x = data['ROOM TYPE'].value_counts()

fig = plt.figure()
width = 0.35

roomtype = []
count = []

for key, value in x.iteritems():
    roomtype.append(key)
    count.append(value)
#print roomtype,count
#print data
ypos = np.arange(len(roomtype))
plt.bar(ypos, count, align='center', alpha=1, facecolor='r')
plt.xticks(ypos, roomtype)
plt.title(r'Services by oyo rooms in Delhi')
plt.show()



