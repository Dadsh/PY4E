# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = []

# pull out lines
for line in handle:
    if not line.startswith('From '):
        continue
    # pull out words
    line = line.split()
    # pull out hours
    time = line[5]
    hour = time[:2]
    hours.append(hour)
#print(hours)

distr = dict()

# count emails from each hour
for hour in hours:
    distr[hour] = distr.get(hour,0) + 1

# create list of tuples from dictionary, sort it, and print hours and count
for hour,count in sorted(distr.items()):
    print(hour, count)
