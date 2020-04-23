import sys

import re

import string

import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer() 

keywords_initial = ['sea', 'fire', 'science']


def lemmatization(n):

	return lemmatizer.lemmatize(n)

keywords = list(map(lemmatization, keywords_initial))

data = []

for line in sys.stdin:

	line = line.strip()

	line = re.sub(r'[^\w\s]','',line)

	line = line.lower()

	words_initial = line.split()

	words = list(map(lemmatization, words_initial))

	#print(words)

	for i in words:

		data.append(i)
	

for i in range(len(data)):

	if data[i] in keywords:

		try:
			ngram1 = data[i - 2] + "_" + data[i - 1] + "_" + "$"
			print(ngram1, '\t', 1)

		except:
			pass


		try:

			ngram2 = data[i - 1] + "_" + "$" + "_" + data[i + 1]
			print(ngram2, '\t', 1)

		except:

			pass

		try:

			ngram3 = "$" + "_" + data[i + 1] + "_" +data[i+ 2]
			print(ngram3, '\t', 1)

		except:

			pass
	else:

		pass













