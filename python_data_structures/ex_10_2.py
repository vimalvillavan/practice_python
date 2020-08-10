name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour = dict()

for line in handle:
    if line.startswith('From '):
        line_list = line.split()
        time = line_list[5].split(':')
        hour[time[0]] = hour.get(time[0], 0) + 1

for key,value in sorted(hour.items()):
    print(key,value)
