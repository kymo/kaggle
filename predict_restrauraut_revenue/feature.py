# -*- encoding:utf8 -*-

# extract feature from raw files, use a dict to store the extracted
# features


def extract_feature(train_raw_file, test_raw_file):
	# extract feature
	# version 1: raw feature with out transferation
	train_feature_file = open("train_feature", "w")
	test_feature_file = open("test_feature", "w")
	# load feature lisan dict
	feat_lisan_dit = {}
	with open("feature_lisan_dic", "r") as f:
		for line in f:
			feat_idx, values = line.strip().split('\t')
			vals = [float(v) for v in values.split(',')]
			if sum(vals)
			feat_lisan_dit[int(feat_idx)] = values.split(',')

	with open(train_raw_file) as f:
		f.readline()
		for line in f:
			cur_feature_vec = []
			data = line.strip().split(',')
			for i in range(3, 41):
				
				if i >= 5:
					val = float(data[i])
					if int(val) != val:
						cur_feature_vec.append(val)
						continue
				for j in range(len(feat_lisan_dit[i])):
					if feat_lisan_dit[i][j] == data[i]:
						cur_feature_vec.append(j)
						break
			cur_feature_vec.append(data[-1])
			train_feature_file.write('\t'.join([str(v) for v in cur_feature_vec]) + '\n')
	train_feature_file.close()

	with open(test_raw_file) as f:
		f.readline()
		for line in f:
			cur_feature_vec = []
			data = line.strip().split(',')
			cur_feature_vec.append(data[0])
			for i in range(3, 41):
				if i >= 5:
					val = float(data[i])
					if int(val) != val:
						cur_feature_vec.append(val)
						continue
				for j in range(len(feat_lisan_dit[i])):
					if feat_lisan_dit[i][j] == data[i]:
						cur_feature_vec.append(j)
						break
			test_feature_file.write('\t'.join([str(v) for v in cur_feature_vec]) + '\n')
	test_feature_file.close()

