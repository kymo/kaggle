# -*- encoding:utf8 -*-
# author : aron
# date   : 2014-12-08
# desc   : navie bayes for classification

import sys

class NavieBayes:

	def __init__(self):
		self.p_class_prop = {}
		self.p_word_prop = {}
		self.p_word_class_prop = {}
		self.stop_word_dict = {}
		pass
	
	def clean_sentence(self, sentence):
		""" clean sentence and return the words' list 

		Args:
			sentence: a str indicating the sentence which's gona to be cleaned
		
		Return:
			a list indicating the words illegal in the sentence
		"""
		words_list = [w.lower() for w in sentence.strip().split(' ')  if w not in self.stop_word_dict]
		return words_list

	def train(self, file_name):
		""" train the model used naive bayes, and save the model

		Args:
			file_name: a str indicating the trainning file
		
		Return:
			None
		"""
		# load stop words
		"""
		with open("stop_word_dict", "r") as f:
			for line in f:
				self.stop_word_dict[line.strip()] = 0
		"""
		# train the model
		tot_word_cnt, tot_cls_cnt = 0, 0
		tot_cls_word_cnt = {}
		with open(file_name, "r") as f:
			for line in f:
				data = line.strip().split('\t')
				sentence, cls = data[2], int(data[3])
				words = self.clean_sentence(sentence)
				if not words:
					continue
				
				if cls not in self.p_class_prop:
					self.p_class_prop[cls] = {'cnt' : 0, 'prop' : 0.0}
					tot_cls_cnt += 1
				self.p_class_prop[cls]['cnt'] += 1
				
				if cls not in self.p_word_class_prop:
					self.p_word_class_prop[cls] = {}

				for w in words:
					if w not in self.p_word_class_prop[cls]:
						self.p_word_class_prop[cls][w] = {'cnt' : 0, 'prop' : 0.0}
					self.p_word_class_prop[cls][w]['cnt'] += 1
					
					if w not in self.p_word_prop:
						self.p_word_prop[w] = {'cnt' : 0, 'prop' : 0.0}
					self.p_word_prop[w]['cnt'] += 1
					tot_word_cnt += 1
				
				if cls not in tot_cls_word_cnt:
					tot_cls_word_cnt[cls] = 0
				tot_cls_word_cnt[cls] += len(words)

		print self.p_class_prop
		# calc the probabilities
		for cls in self.p_class_prop:
			self.p_class_prop[cls]['prop'] = (self.p_class_prop[cls]['cnt'] + 1) * 1.0\
				/ (tot_cls_cnt + 1)
		for w in self.p_word_prop:
			self.p_word_prop[w]['prop'] = (self.p_word_prop[w]['cnt'] + 1) * 1.0 \
				/ (tot_word_cnt + 1)
		for cls in self.p_word_class_prop:
			for w in self.p_word_class_prop[cls]:
				self.p_word_class_prop[cls][w]['prop'] = (self.p_word_class_prop[cls][w]['cnt'] + 1) * 1.0\
					/ (tot_cls_word_cnt[cls] + 1.0)


	def save_model(self):
		pass
	
	def predict(self, doc):
		""" predict the class type of the doc

		Args:
			doc: a str indicating the sentence gona to be predicted

		Return:
			class_type, propability

		"""
		words = self.clean_sentence(doc)
		max_prop, pre_cls = -1.0, 0
		for cls in self.p_class_prop:
			p_word_class, p_word = 1.0, 1.0
			for w in words:
				
				if w not in self.p_class_prop:
					p_word *= 0.00001
				else:
					p_word *= self.p_class_prop[w]['prop']
				
				try:
					if w not in self.p_word_class_prop[cls]:
						p_word_class *= 0.00001
					else:
						p_word_class *= self.p_word_class_prop[cls][w]['prop']
				except Exception as e:
					print e

			p_class_doc = p_word_class * self.p_class_prop[cls]['prop'] / p_word
			if max_prop < p_class_doc:
				max_prop = p_class_doc
				pre_cls = cls

		return pre_cls, max_prop
	
	def test(self, file_name):
		right_cnt, tot_cnt = 0, 0
		with open(file_name, "r") as f:
			for line in f:
				data = line.strip().split('\t')
				sentence, cls = data[2], int(data[3])
				pre_cls, prop = self.predict(sentence)
				if cls == pre_cls:
					right_cnt += 1
				tot_cnt += 1
		print 'right ratio: %s' % (right_cnt * 1.0 / tot_cnt)

	def submit(self, test_file_name):
		submit_f = open("out", "w")
		with open(test_file_name) as f:
			for line in f:
				data = line.strip().split('\t')
				if len(data) < 3:
					submit_f.write(data[0] + ',3\n')
					continue
				sentence = data[2]
				pre_cls, prop = self.predict(sentence)
				submit_f.write(data[0] + ',' + str(pre_cls) + '\n')
		submit_f.close()

if __name__ == '__main__':
	navie_bayes = NavieBayes()
	print 'Usage : [train file] [test file]'
	navie_bayes.train(sys.argv[1])
	navie_bayes.test(sys.argv[2])
	navie_bayes.submit(sys.argv[3])
