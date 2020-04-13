"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
prefixCalledToSet=set()
noOfCallsToBang=0
TotNoOfCalls=0
for call in calls:
    calledBy=call[0]
    calledTo=call[1]
    if(calledBy.startswith("(080)")):
        TotNoOfCalls+=1
        if(calledTo.startswith("(080)")):
            noOfCallsToBang+=1
            prefixCalledToSet.add("(080)")
        elif(calledTo.startswith("(")):
            areacode=calledTo.split(")")[0]+")"
            prefixCalledToSet.add(areacode)
        elif(calledTo.find(" ")  and (calledTo.startswith("7") or calledTo.startswith("8") or calledTo.startswith("9"))):
            prefixCalledToSet.add(calledTo[0:4])
        elif(calledTo.startswith("140")):
            prefixCalledToSet.add("140")
areacodes=sorted(prefixCalledToSet)
percCallsToBang=float(noOfCallsToBang)/float(TotNoOfCalls)
print("The numbers called by people in Bangalore have codes:")
for code in areacodes:
    print(code)
print("{0:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percCallsToBang))
        
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
