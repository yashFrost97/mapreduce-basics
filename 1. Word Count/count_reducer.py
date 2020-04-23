from operator import itemgetter
import sys
total_count=0
cword=None 

for line in sys.stdin:
	line=line.strip()
	word,count = line.split('\t',1)
	try:
		count=int(count)
		if cword==word:
			total_count +=count
		else: 
			if cword:
				print(cword, "\t" ,str(total_count))
			total_count=count
			cword=word
	except ValueError:
		continue
	
if cword==word:
	print(cword+"\t"+str(total_count))
