#!/usr/bin/env python3

from sys import stdin
import re
import os
import ntpath

def path_leaf(path):
	head,tail = ntpath.split(path)
	return tail or ntpath.basename(head)

doc_id = ""

for line in stdin:
	path = os.environ["map_input_file"]
	doc_name = path_leaf(path)
	#doc_name = re.findall(r'\w+', doc_name)[-1]
	# if doc_name=="arthur.txt":
	# 	doc_id="1"
	# elif doc_name=="james.txt":
	# 	doc_id="2"
	# elif doc_name=="leonardo.txt":
	# 	doc_id="3"
	words = re.findall(r'\w+',line.strip())
	for word in words:
		print(word.lower()+"\t"+doc_name)

