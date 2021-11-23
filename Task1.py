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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# texts_set = set()
inverted_text_list=list(zip(*texts))
inverted_calls_list=list(zip(*calls))
total_list_of_nums = inverted_text_list[0]+ inverted_text_list[1]+inverted_calls_list[0]+inverted_calls_list[1]
count=len(set(total_list_of_nums))
print("There are ",count," different telephone numbers in the records.")

#BigO = O(n+m+5) = O(n+m)
