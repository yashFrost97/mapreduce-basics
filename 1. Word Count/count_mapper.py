import sys

import re

for line in sys.stdin:
	
	line=line.strip()

	line = re.sub(r'[^\w\s]','',line)

	line = line.lower()

	words = line.split()

	for word in words: 

		print(word, "\t" , 1)
	 
