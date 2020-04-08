"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

teleNums=set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
for call in calls:
    calledBy=call[0]
    if(calledBy.startswith("140")):
        teleNums.add(calledBy)
    calledTo=call[1]
    if calledTo in teleNums:
        teleNums.remove(calledTo)
for text in texts:
    textBy=text[0]
    if textBy in teleNums:
        teleNums.remove(textBy)
    textTo=text[1]
    if textTo in teleNums:
        teleNums.remove(textTo)
teleNumList=sorted(list(teleNums))
print("These numbers could be telemarketers: ")
for num in teleNumList:
    print(num)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

