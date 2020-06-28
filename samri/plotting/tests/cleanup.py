import os, re

def cleanup():
	'''
	Removes files created by tests.
	'''
	directory = os.path.abspath('')
	to_del = []
	pattern = '(.*)\.(png|pdf)$'
	for i in os.listdir(directory):
		obj = re.search(pattern, i)
		if obj:
			to_del.append(obj.group())
	for i in to_del:
		os.remove(i)
	print('File(s) removed:', *to_del)

cleanup()
