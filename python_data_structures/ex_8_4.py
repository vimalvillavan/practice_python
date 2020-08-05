fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    str_line = line.rstrip()
    newline_lst = str_line.split()
    for new_word in newline_lst:
        if new_word not in lst:
            lst.append(new_word)

lst.sort()
print(lst)



