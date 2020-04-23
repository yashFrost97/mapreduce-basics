import sys
import operator


data = []

for line in sys.stdin:
	line = line.strip()
	data.append(line)

count = 1

for i in data:
	data2 = []
	for val in i:
		if(val.isdigit()):
			data2.append(int(val))

	votes = {}
	
	for k in data2:
		if k in votes.keys():
			votes[k] += 1
		else:
			votes[k] = 1

	sortedVotes = {}
	sortedVotes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
	print("Datarow:", count, "\t", sortedVotes[0][0])

	count += 1


