import operator

import sys

ngram = {}

for line in sys.stdin:

	#print(line)

	line = line.strip()

	#print(line)

	trigram, count = line.split('\t')


	if trigram in ngram:

		ngram[trigram] += int(count)

	else:

		ngram[trigram] = int(count)


sorted_ngram = dict(sorted(ngram.items(), key=operator.itemgetter(1),reverse=True))

count2 = 1

for key, value in sorted_ngram.items():

	print(key,'\t',value)

	count2 += 1

	if(count2 > 10):
		break




