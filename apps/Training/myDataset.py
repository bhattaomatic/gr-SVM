import numpy as np

class myDataset:
	""" This class defines the loading of the Datasets and
		returns the reshaped dataset. 
		
				Author	:	Abhishek Bhatta
		
		The parameters for loadDataset are:
		data	=	Input data array that needs to be reshaped
		length	=	Length of the desired output data * nparams
		nparams	=	number of columns for the required reshaped 
					data
	"""
		
	def reshapeData(self, data, length=None, nparams=48, norm=0):
		if length is None:
			length=len(data) - np.mod(len(data),nparams)
		data = np.reshape(data[0:length], (length/nparams,nparams))
		print length
		# Normalize the data
		if norm == 1:
			data = data - np.mean(data, 0)/ np.std(data,0)
		return data
