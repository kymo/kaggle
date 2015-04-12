# -*- encoding:utf8 -*-

from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import linear_model

import numpy as np

class Model(object):
	def __init__(self, *argv):
		# load the model and test features vector
		self.x = []
		self.y = []
		self.test_x = []
		self.test_y = []
		self.feature_file = argv[0]
		self.model_file = argv[1]
        
	def load_feature(self):
		# load feature from the feature file
		
		with open(self.feature_file, "r") as f:
			for line in f:
				data = line.strip().split('\t')
				self.x.append([float(i) for i in data[:-1]])
				self.y.append(float(data[-1]))
		n = int(len(self.x) * 0.8)
		
		self.test_x = self.x[n : ]
		self.test_y = self.y[n : ]
		self.x = np.array(self.x[ : n])
		self.y = np.array(self.y[ : n])
	
	def pretreat_feature(self):
		pass

	def train(self):
		pass

	def assess(self):
		pass
	
	def test(self):
		pass
    
	def validation(self):
		pass

	def predict(self, feature):
		pass


# random forest model inherited from class Model
# and implementing the load_feature, train, predict method

class RandomForestModel(Model):
	""" random forest model """
	def __init__(self, *argv, **args):
		super(RandomForestModel, self).__init__(*argv)
        
		self.rf = RandomForestRegressor(**args)
	
	def pretreat_feature(self):
		# pre-handle about the feature data
		pass

	def train(self):
		# train the samples
		self.rf.fit(self.x, self.y)
	
	def assess(self):
		# assess the regression model
		error = 0.0
		for j in range(len(self.test_x)):
			pre_val = self.predict(self.test_x[j])
			error += (pre_val - self.test_y[j]) ** 2
		print 'Training Error: ', error
		
    
	def predict(self, x):
		# predic the output of the x		
		return self.rf.predict(x)

	def validate(self):
		# use cross-validation to choose the best meta-parameter
		pass

class LinearRegModel(Model):
	""" linear regression model """
	def __init__(self, *argv, **args):
		super(LinearRegModel, self).__init__(*argv)
		self.linear_reg_model = linear_model.Ridge(**args)
	
	def train(self):
		# train the samples
		self.linear_reg_model.fit(self.x, self.y)
	
	def assess(self):
		# assess the regression model
		error = 0.0
		for j in range(len(self.test_x)):
			pre_val = self.predict(self.test_x[j])
			error += (pre_val - self.test_y[j]) ** 2
		print 'Testing Error: ', error

	def predict(self, x):
		# predict the output of the x
		return self.linear_reg_model.predict(x)

class GBDTModel(Model):
	
	""" gbdt model """
	def __init__(self, *argv, **args):
		super(GBDTModel, self).__init__(*argv)
		self.gbdt = GradientBoostingClassifier(**args)
	
	def train(self):
		# train the samples
		self.gbdt.fit(self.x, self.y)
		# assess the model
	
	def predict(self, x):
		# predict the output given the test feature
		return self.gbdt.predict(x)


class SVMModel(Model):

	""" svm model """
	def __init__(self, *argv, **args):
		super(SVMModel, self).__init__(*argv)
		self.svm = svm.SVC(**args)
	
	def train(self):
		self.svm.fit(self.x, self.y)
	
	def predict(self, x):
		return self.svm.predict(x)

class SVRModel(Model):
	pass


