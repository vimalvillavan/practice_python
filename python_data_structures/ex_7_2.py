fname = input ("Enter file name: ")
fh = open(fname)
count = 0
tot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    f = line.find(':')
    x = line[f+1:]
    x.strip()
    flt_x = float(x)
    tot = tot + flt_x
print ("Average spam confidence:", tot/count)

