#!/usr/bin/python

import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib
from sh import cd
import scipy as sp
from myDataset import myDataset


mdt = myDataset()
cd('/home/abhishek/tmp/Untitled Folder/data')
x = sp.fromfile(open('no_person'), dtype=sp.complex64)
x = np.abs(x)

x = mdt.reshapeData(x, norm=0)

cd('/home/abhishek/Git/gr-SVM/include/models/')
mean = joblib.load('mean.pkl')
standarddev = joblib.load('std.pkl')
x = (x - mean)/standarddev
#X = x.reshape(1,-1)
clf = joblib.load('svm_model.pkl')
output = clf.predict(x)
print sum(output)/len(output)
