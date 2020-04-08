"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

phonenums=set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for t in texts:
        phonenums.add(t[0])
        phonenums.add(t[1])
                 

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        phonenums.add(c[0])
        phonenums.add(c[1])
numOfPhonesNo=len(phonenums)
print("There are {} different telephone numbers in the records.".format(numOfPhonesNo))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
