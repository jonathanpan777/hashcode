import numpy as np
import math
class Intersection:
	def __init__(self, incoming, outgoing, num):
		self.incoming = incoming
		self.outgoing = outgoing
		self.weights = None
		self.num = num
		self.counts = None


	def init(self):
		self.counts = np.zeros(len(self.incoming))	
	def init_weights(self):
		self.weights = np.ones(len(self.incoming))/len(self.incoming)

	def set_weights(self, weights):
		self.weights = weights
		
	def get_cycle_from_weights(self, outfile):
		self.max_cycle_len = 1000000000#can be changed later
		#if(not self.weights):
		#	self.init_weights()
		l = len(self.weights)
		i = 0
		b = 1

		self.weights = self.weights.tolist()

		while(i < l):
			if self.weights[i] == 0:
				self.weights.pop(i)
				b = self.incoming.pop(i)
				i -= 1
				l-=1
			i += 1
			if(len(self.weights) == 0):
				outfile.write(str(self.num))
				outfile.write('\n')
				outfile.write(str(1))
				outfile.write('\n')
				outfile.write(str(b.name) + " " + str(1))
				outfile.write('\n')
				return


		print(self.weights)
		self.weights = np.array(self.weights)/sum(self.weights)
		cycle_len = min(self.max_cycle_len, 1/min(self.weights))

		self.weights *= cycle_len

		outfile.write(str(self.num))
		outfile.write('\n')
		outfile.write(str(len(self.weights)))
		outfile.write('\n')
		for i in range(len(self.weights)):
			outfile.write(self.incoming[i].name + " " + str(math.ceil(self.weights[i])))
			outfile.write('\n')
