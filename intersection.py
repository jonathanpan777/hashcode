import numpy as np

class Intersection:
  def __init__(self, incoming, outgoing, num):
    self.incoming = incoming
    self.outgoing = outgoing
    self.weights = None
    self.num = num
    self.counts = [0] * len(incoming)

def init_weights(self):
	self.weights = np.ones(len(self.incoming))/len(incoming)

def set_weights(self, weights):
	self.weights = weights
	
def get_cycle_from_weights(self, outfile):
	self.max_cycle_len = 1000000000#can be changed later
	if(self.weights == None):
		self.init_weights()
	l = len(self.weights)
	i = 0

	while(i < l):

		if self.weights[i] == 0:
			self.weights.pop(i)
			self.incoming.pop(i)
			i -= 1
			l-=1
		i += 1

	self.weights = np.array(weights)/sum(self.weights)
	print(self.weights, self.incoming)
	cycle_len = min(self.max_cycle_len, 1/min(self.weights))

      if self.weights[i] == 0:
        self.weights.pop(i)
        self.incoming.pop(i)
        i -= 1
        l-=1
      i += 1

    self.weights = np.array(self.weights)/sum(self.weights)
    cycle_len = min(self.max_cycle_len, 1/min(self.weights))

    self.weights *= cycle_len

    outfile.write(str(self.num))
    outfile.write('\n')
    outfile.write(str(len(self.weights)))
    outfile.write('\n')
    for i in range(len(self.weights)):
      outfile.write(self.incoming[i].name + " " + str(ceil(self.weights[i])))
      outfile.write('\n')
