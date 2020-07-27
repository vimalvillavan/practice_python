
fname = input("Enter file name: ")
fh = open(fname)
read = fh.read()
read.rstrip()
print(read.upper())
