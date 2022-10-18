import math
import pprint

# Read all the records in:
data = []
with open("data-2022-10-16-02.txt") as datafile:
    data = datafile.readlines()

# Time is expected to be integers and in seconds:
def is_over_two_minutes(nowtime, starttime):
     return nowtime - starttime > 120

def get_average(total, number):
    return float(total)/float(number)

# User a dictionary for averages:
averages = {}
# Use a negative start to indicate that we haven't gotten a starting time yet:
start = -1
total = 0
number = 0
for line in data:
    line = line.rstrip('\n')
    record = line.split(' ')
    timestamp = int(float(record[2]))
    pvalue = float(record[1])
    if start < 0:
        start = timestamp
        total = pvalue
        number = 1
    elif is_over_two_minutes(timestamp, start):
        # First save the average:
        # Time to save is the current timestamp - 1:
        savetime = timestamp -1
        averages[savetime] = get_average(total, number)
        # Reset the start to the new timestamp:
        start = timestamp
        total = pvalue
        number = 1
    else:
        # We already have a starting point and not yet two minutes.
        # Just add the pvalue to total:
        total = total + pvalue
        number = number + 1

# pp = pprint.PrettyPrinter()
# pp.pprint(averages)
for timestamp, pvalue in averages.items():
    print(f'{timestamp},{pvalue}')
