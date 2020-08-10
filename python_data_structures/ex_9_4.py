name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email = dict()

for line in handle:
    if line.startswith('From '):
        line_list = line.split()
        email[line_list[1]] = email.get(line_list[1],0) + 1

max_count = None
max_commiter = None

for key,value in email.items():
    if max_count is None or value > max_count:
        max_count = value
        max_commiter = key

print (max_commiter, max_count)
