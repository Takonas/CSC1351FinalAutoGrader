#!/usr/bin/env python3

import os
import sys
import re

def grade(path):
	if path is None:
	    path = os.getcwd()

	onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	

	regexList = ['^\\s*$', '^\\s*//.*', '^\\s*\\*\\/', '^\\s*\\/\\*', '^\\s*\\*.*$', '^\\s*import\\s', '^\\s*\\{\\s*$', '^\\s*\\}\\s*$']

	line_count = 0
	
	print(onlyfiles)
	
	n=len(onlyfiles)
	for i in range(n-1,-1,-1):
	    if onlyfiles[i].endswith(".java"):
	    	pass
	    else:
	    	print(f"REMOVING FILE: {onlyfiles[i]}")
	    	onlyfiles.remove(onlyfiles[i])
		
	file_line_count = [0] * len(onlyfiles)
	for i,file in enumerate(onlyfiles):
	    with open(os.path.join(path, file), 'r') as file:
	    	for line in file:
	    		match = 1
	    		for regex in regexList:
	    			s = re.search(regex, line)
	    			if s:
	    				match = 0
    			file_line_count[i] = file_line_count[i] + match
	for i in range(len(file_line_count)):
		print(f"{onlyfiles[i]} is {file_line_count[i]}")
		line_count = line_count + file_line_count[i]
	print(line_count)
