#encoding:utf8
import sys
import random
sets = [line.strip() for line in open(sys.argv[1], "r").readlines()]


for st in sets:
	data = st.split('\t')


len_set = len(sets)

f = open("test_1.tsv", "w")
pos = int(len_set * 0.1)

for i in sets[:pos]:
	f.write(i + '\n')

f.close()
dit = {}
s = open("train_1.tsv", "w")
for i in sets[pos:]:
	data = i.split('\t')
	if int(data[3]) not in dit:
		dit[int(data[3])] = []
	dit[int(data[3])].append(i)
mx = 1000
for i in dit:
	print i
	if mx > len(dit[i]):
		mx = len(dit[i])
out = []
for i in dit:
	out.extend(random.sample(dit[i], mx))
for line in out:
	s.write(line + '\n')
s.close()
