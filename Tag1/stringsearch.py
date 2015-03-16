import re

def stringsearch(substr, string):
	matches = re.finditer(substr, string)
	k = 0
	for i in matches:
		k += 1
		print "Instance %i: Start: %i, End: %i" %(k, i.start(0) + 1, i.end(0) + 1)
	print "%i Instances of '%s' found" %(k, substr)