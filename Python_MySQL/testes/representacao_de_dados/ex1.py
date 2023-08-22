Store = dict()

reading = open("16s_bacteria.fasta", "r").read()
reading = reading.split("\n")

for i in range(len(reading)):
    if ">" in reading[i]:
        Store[reading[i]] = reading[i+1]

print(Store)