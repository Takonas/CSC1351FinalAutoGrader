#!/usr/bin/env python3

import os
import sys
from zipfile import ZipFile
import final_line_grader

path = os.getcwd()
options = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
options.sort()

validchoice = False
while validchoice == False:
	print("="*20+"\n"+"Final Directory Grading\n"+"="*20)
	for i, option in enumerate(options):
		print(f"{i+1}. {option}")
	print("0. Exit")
	
	try:
		choice = int(input("Enter Directory Option: "))
		if isinstance(choice, int) and 0 <= choice <=len(options):
			validchoice = True
	except:
		print("CHOICE ERROR")

path = options[choice-1]
directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
directories.sort()
print("\n" + "=" * 20)
for directory in directories:
	print(f"\n{directory} has the following files:")
	good = False
	pathmod = os.path.join(path, directory)
	files = [f for f in os.listdir(pathmod) if os.path.isfile(os.path.join(pathmod, f))]
	for file in files:
		if file.endswith(".java"):
			good = True
			break
	if good == False:
		for file in files:
			if file.endswith(".zip"):
				zip = ZipFile(os.path.join(pathmod, file))
				zip.extractall(pathmod)
				zip.close()
		zipdirecs = [f for f in os.listdir(pathmod) if os.path.isdir(os.path.join(pathmod, f))]
		if zipdirecs:
			n=len(zipdirecs)
			for i in range(n-1,-1,-1):
			    if zipdirecs[i] == ("__MACOSX"):
			    	zipdirecs.remove(zipdirecs[i])
			pathmod = os.path.join(pathmod, zipdirecs[0])
	final_line_grader.grade(pathmod)
	print("\n" + "="*5)
