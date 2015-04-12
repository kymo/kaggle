# -*- encoding:utf8 -*-

import sys
from model import RandomForestModel
from feature import extract_feature
from model import LinearRegModel

if __name__ == '__main__':
	
	try:
		if sys.argv[1] == 'feature':
			if len(sys.argv) < 3:
				print 'Usage: python main.py feature [train raw feature] [test raw feature]'
			
			else:
				features = extract_feature(sys.argv[2], sys.argv[3])
				# load train features
		
		elif sys.argv[1] == 'model':
			if len(sys.argv) < 4:
				print 'usage: python main.py model [train_feature] [model_file] [test_file]' 
			model = RandomForestModel(sys.argv[2],
					sys.argv[3],
					n_estimators = 200)
			"""
			model = LinearRegModel(sys.argv[2],
					sys.argv[3],
					alpha = 0.5)
			"""
			"""
			model = GBDTModle(sys.argv[2],
					sys.argv[3],
					n_estimators = 
			"""
			print 'Loading feature...'
			model.load_feature()
			print 'Training...'	
			
			model.train()
			print 'Assessing...'
			model.assess()
			# output the model
			print 'Outputing...'
			out_file = open("sub.csv", "w")
			out_file.write("Id,Prediction\n")
			with open(sys.argv[4], "r") as f:
				for line in f:
					data = [float(v) for v in line.strip().split('\t')]
					val = model.predict(data[1:])
					out_file.write(str(int(data[0])) + "," + str(val[0]) + '\n')
			out_file.close()
		
	except Exception as e:
		print e
		print 'Usage: python main.py feature/model [extra_files]'
    
            
