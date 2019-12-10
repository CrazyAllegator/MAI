class PolyReg(object):
	def __init__(self,*pargs,**kwargs):
		beta, powers = None, None
	def fit(self, xs, y, deg, model_out=False, powers_out=False):
		y = asarray(y).squeeze()
		rows = y.shape[0]
		xs = asarray(xs)
		num_covariates = xs.shape[1]
		xs = hstack((ones((xs.shape[0], 1), dtype=xs.dtype) , xs))
		generators = [self.basis_vector(num_covariates+1, i)
						for i in range(num_covariates+1)]
		powers = map(sum, itertools.combinations_with_replacement(generators, deg))
		A = hstack(asarray([self.as_tall((xs**p).prod(1)) for p in powers]))
		beta = linalg.lstsq(A, y)[0]
		self.beta = beta
		self.powers = powers
	def predict(self, args):
		if(self.beta == self.powers == None):
			return -1
		num_covariates = len(self.powers[0]) - 1
		if len(args)!=(num_covariates):
			raise ValueError()
		xs = asarray((1,) + tuple(args) )
		return sum([coeff * (xs**p).prod()
		for p, coeff in zip(self.powers, self.beta)])
	def basis_vector(self, n, i):
		x = zeros(n, dtype=int)
		x[i] = 1
		return x
	def as_tall(self, x):
		return x.reshape(x.shape + (1,))