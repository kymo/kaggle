# -*- encoding:utf8 -*-

import sys

data_cols = dict([(k,[]) for k in range(135)])
print data_cols

with open(sys.argv[1], 'r') as f:
	f.readline()
	for line in f:
		data = line.strip().split(',')
		for i in range(len(data)):
			data_cols[i].append(data[i])

with open(sys.argv[2], 'r') as f:
	f.readline()
	for line in f:
		data = line.strip().split(',')
		for i in range(len(data)):
			data_cols[i].append(data[i])

for i in data_cols:
	print str(i) + '\t' + ','.join(list(set(data_cols[i])))
