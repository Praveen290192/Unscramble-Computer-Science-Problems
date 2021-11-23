"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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
num_without_tele = []
no_received_calls = []
no_text_msg = []

for num in calls:
    for row in calls:
        if num[0] == row[1]:
            break
    else:
        no_received_calls.append(num[0])
# print(no_received_calls)
no_received_calls = set(no_received_calls)

for num in no_received_calls:
    for row in texts:
        if num == row[0] or num == row[1]:
            break
    else:
        no_text_msg.append(num)
no_text_msg = set(no_text_msg)

print("These numbers could be telemarketers: ")      
for num in sorted(no_text_msg):
    print(num)

#BigO = O(8n^2+n*log n+7) = O(n*log n)