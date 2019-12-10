class KNN(object):
	def __init__(self,*pargs,**kwargs):
		train_data = []
	def _metric(self, a, b):
		sum_quad = 0
		for i in range(len(a)):
			sum_quad += (b[i]-a[i])**2
		return math.sqrt(sum_quad)
	def fit(self,x,y):
		self.train_data = [i for i in zip(x,y)]
	def predict(self,x, k=10):
		result = []
		for test in x:
			res = {}
			testRes = [(self._metric(i[0], test), i[1]) for i in
self.train_data]
			for d in sorted(testRes, key=lambda kk: kk[0])[:k]:
				if d[1] in res:
					res[d[1]] += 1
				else:
					res[d[1]] = 1
			result.append(max(res.items(), key=lambda x: x[1])[0])
	return(result)
