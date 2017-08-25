#!/usr/bin/python

import numpy as np
import scipy as sp
#import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sh import cd
from sklearn.externals import joblib
from myDataset import myDataset
import pmt

mdt = myDataset()

cd('/home/abhishek/tmp')
#cd('/home/abhishek/Masters_and_Phd/201x_CommSense/Capture set 5/Data_Capture_Feb_25_2017/singlePerson_different_location/person_10m/2')
#Trainingdata1 = np.loadtxt('chan_imp_resp_normal_abs.txt') 
Trainingdata1 = sp.fromfile(open('realtimetest3_sephdr'), dtype=sp.complex64)
Trainingdata1 = np.abs(Trainingdata1)

#cd('/home/abhishek/Masters_and_Phd/201x_CommSense/Capture set 5/Data_Capture_Feb_25_2017/singlePerson_different_location/Without person/2/')
#Trainingdata2 = np.loadtxt('chan_imp_resp_normal_abs.txt') 
Trainingdata2 = sp.fromfile(open('realtimetest4_sephdr'), dtype=sp.complex64)
Trainingdata2 = np.abs(Trainingdata2)

# Create the Training data
Trainingdata1 = mdt.reshapeData(Trainingdata1[0:48000], norm=0)
Trainingdata2 = mdt.reshapeData(Trainingdata2[0:48000], norm=0)

# Create the Labels
Labeldata1 = np.ones(len(Trainingdata1))
Labeldata2 = 2*np.ones(len(Trainingdata2))

# Stack the datasets
training = np.vstack((Trainingdata1, Trainingdata2))
label = np.hstack((Labeldata1, Labeldata2))

C = 1 # SVM regularization parameter
clf = SVC(kernel= 'linear', verbose=False, C=C)
output = clf.fit(training, label)
testOutput = clf.predict(training)
print "Prediction output: ", testOutput
print "Length of Prediction Output: ", testOutput.shape

cd('/home/abhishek/GNURadio/python_test/gr-SVM/include/models/')
joblib.dump(output, 'svm_model.pkl')
