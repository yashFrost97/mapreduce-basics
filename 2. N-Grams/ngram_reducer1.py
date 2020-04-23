import operator

import sys

ngram = {}

for line in sys.stdin:

	#print(line)

	line = line.strip()

	#print(line)

	trigram, count = line.split('\t', 1)

	if trigram in ngram:

		ngram[trigram] += 1

	else:

		ngram[trigram] = 1


sorted_ngram = dict(sorted(ngram.items(), key=operator.itemgetter(1),reverse=True))

count = 1

for key, value in sorted_ngram.items():

	print(key,'\t',value)

	count += 1

	if(count > 10):
		break




