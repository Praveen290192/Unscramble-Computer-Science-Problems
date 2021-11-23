"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

inverted_calls_list=list(zip(*calls))
total_list_of_nums = set(inverted_calls_list[0]+inverted_calls_list[1])
total_call_time = {}

for num in total_list_of_nums:
    total_call_time[num] = 0
    for row in calls:
        if num in row[0]:
            total_call_time[num]=total_call_time.get(num)+int(row[3])
        if num in row[1]:
            total_call_time[num]=total_call_time.get(num)+int(row[3])

max_call_time = max(total_call_time.values())

tel_number=list(total_call_time.keys())[list(total_call_time.values()).index(max_call_time)]
print(tel_number," spent the longest time, ",max_call_time," seconds, on the phone during September 2016.")

#BigO = O(4*n*m+n+6)= O(n*m)