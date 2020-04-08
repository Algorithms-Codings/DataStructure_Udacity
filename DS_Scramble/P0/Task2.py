"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
phoneDetails={}
pNum=""
duration=0
for c in calls:
    if c[0] in phoneDetails:
        phoneDetails[c[0]]+=int(c[3])
    else:
        phoneDetails[c[0]]=int(c[3])
    if(phoneDetails[c[0]]>duration):
        pNum=c[0]
        duration=phoneDetails[c[0]]
    if c[1] in phoneDetails:
        phoneDetails[c[1]]+=int(c[3])
    else:
        phoneDetails[c[1]]=int(c[3])
    if(phoneDetails[c[1]]>duration):
        pNum=c[1]
        duration=phoneDetails[c[1]]
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(pNum,duration))
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

