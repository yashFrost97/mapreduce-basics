#!/usr/bin/env python3
from sys import stdin
from collections import defaultdict
import re

result = {}
for line in stdin:
	line = line.strip()
	word, postings = line.split('\t')
	if word in result.keys():
		b = []
		b = result.get(word)
		if postings not in b:
			b.append(postings)
			result[word] = b
	else:
		b = []
		b.append(postings)
		result[word] = b
for k,v in result.items():
	print(k,'\t',v)
	

		
		
	
